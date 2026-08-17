#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""company-brief · 生成检索查询清单（分层查询）

用法：
    python make-queries.py --company "公司名"
输出：检索清单（G1-G5，含分层社媒/招聘平台查询词）
"""
import argparse
import json
from pathlib import Path


def build_queries(company):
    return {
        "G1 定位与主体": [f'"{company}" 简介', f'"{company}" 工商 成立'],
        "G2 融资与数字": [f'"{company}" 融资', f'"{company}" 营收'],
        "G3 产品与竞品": [f'"{company}" 产品', f'"{company}" 竞品'],
        "G4 客户与风险": [f'"{company}" 客户', f'"{company}" 诉讼 OR 处罚'],
        # 招聘：必查 4 平台 + 官网招聘页
        "G5 招聘（必查）": [
            f'"{company}" BOSS直聘', f'"{company}" 猎聘',
            f'"{company}" 智联招聘', f'"{company}" 前程无忧',
            f'"{company}" 官网 招聘',
        ],
        # 社媒：必查 5 平台
        "G6 社媒（必查）": [
            f'"{company}" 官方微博', f'site:douyin.com "{company}"',
            f'site:xiaohongshu.com "{company}"', f'site:linkedin.com "{company}"',
            f'site:x.com "{company}"',
        ],
        # 按行业查（长尾，视行业补充）
        "G7 社媒/招聘（按行业）": [
            f'"{company}" 快手 OR B站 OR 视频号 OR 知乎 OR 脉脉',
            f'"{company}" 58同城 OR 拉勾 OR 牛客',
        ],
    }


def main():
    ap = argparse.ArgumentParser(description="company-brief 检索清单")
    ap.add_argument("--company", required=True)
    ap.add_argument("--out", default="work/queries.json")
    args = ap.parse_args()

    result = {
        "company": args.company,
        "blocks": build_queries(args.company),
        "note": "分层查询：G5/G6 必查；G7 按行业查（命中率高则写，否则如实标注未检索到）。"
                "每平台独立查询，命中写账号名+链接，查无写未检索到+检索记录。",
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
