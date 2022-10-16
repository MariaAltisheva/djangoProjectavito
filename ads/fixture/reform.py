"""Преобразованиe csv файлов в json"""
import csv
import json


def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


convert_csv_to_json('ads.csv', 'ads.json')
convert_csv_to_json('categories.csv', 'categories.json')