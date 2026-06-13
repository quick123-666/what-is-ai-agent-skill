#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
what-is-ai-agent Skill 独立语义检索系统
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List

# 配置
REFERENCES_PATH = Path(__file__).parent.parent / "references"
CHUNK_SIZE = 500
TOP_K = 3

@dataclass
class SearchResult:
    file: str
    chunk_id: int
    content: str
    score: float
    match_keywords: List[str]

class SimpleSearcher:
    def __init__(self):
        self.chunks = []
    
    def load_documents(self, path: Path) -> int:
        if not path.exists():
            print(f"[ERROR] 路径不存在: {path}")
            return 0
        
        chunk_id = 0
        for md_file in sorted(path.glob("*.md")):
            if md_file.name.startswith("."):
                continue
            
            content = md_file.read_text(encoding="utf-8")
            
            paragraphs = []
            current_para = ""
            
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    if current_para:
                        paragraphs.append(current_para)
                        current_para = ""
                else:
                    current_para += " " + line
                    if len(current_para) >= CHUNK_SIZE:
                        paragraphs.append(current_para)
                        current_para = ""
            
            if current_para:
                paragraphs.append(current_para)
            
            for para in paragraphs:
                if len(para) < 50:
                    continue
                self.chunks.append({
                    'file': md_file.name,
                    'chunk_id': chunk_id,
                    'content': para
                })
                chunk_id += 1
        
        print(f"[OK] 加载 {len(list(path.glob('*.md')))} 文件, {len(self.chunks)} 段落")
        return len(self.chunks)
    
    def extract_keywords(self, text: str) -> set:
        text = text.lower()
        text = re.sub(r'[^\w\s\u4e00-\u9fff]', ' ', text)
        
        english = re.findall(r'[a-z]{2,}', text)
        chinese = re.findall(r'[\u4e00-\u9fff]{2,4}', text)
        
        keywords = set(english) | set(chinese)
        
        stopwords = {
            'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            '可以', '这个', '那个', '什么', '怎么', '如何', '为什么',
            '因为', '所以', '但是', '而且', '或者', '如果', '虽然'
        }
        return keywords - stopwords
    
    def search(self, query: str, top_k: int = TOP_K) -> List[SearchResult]:
        query_keywords = self.extract_keywords(query)
        print(f"[QUERY] 关键词: {query_keywords}")
        
        if not query_keywords:
            return []
        
        results = []
        
        for chunk in self.chunks:
            chunk_kw = self.extract_keywords(chunk['content'])
            matches = query_keywords & chunk_kw
            
            if not matches:
                continue
            
            base_score = len(matches)
            content_lower = chunk['content'].lower()
            
            position_bonus = sum(max(0, (1000 - content_lower.find(kw)) / 1000) for kw in matches if kw in content_lower)
            exact_bonus = 2.0 if query.lower() in content_lower else 0
            
            total_score = base_score + position_bonus * 0.5 + exact_bonus
            
            results.append(SearchResult(
                file=chunk['file'],
                chunk_id=chunk['chunk_id'],
                content=chunk['content'][:300] + "..." if len(chunk['content']) > 300 else chunk['content'],
                score=total_score,
                match_keywords=list(matches)
            ))
        
        results.sort(key=lambda x: x.score, reverse=True)
        return results[:top_k]


def search_skill(query: str, top_k: int = TOP_K) -> List[SearchResult]:
    print(f"\n{'='*40}")
    print(f"[SEARCH] {query}")
    print(f"{'='*40}")
    
    searcher = SimpleSearcher()
    searcher.load_documents(REFERENCES_PATH)
    results = searcher.search(query, top_k)
    
    for i, r in enumerate(results, 1):
        print(f"\n[{i}] {r.file} (score: {r.score:.2f})")
        print(f"    keywords: {r.match_keywords}")
        print(f"    content: {r.content[:150]}...")
    
    return results


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI Agent 是什么"
    search_skill(query)
