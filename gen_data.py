import csv

# 示例数据
data = [
    {"Country": "United States", "Continent": "North America", "GDP": 21433225, "Year": 2022},
    {"Country": "China", "Continent": "Asia", "GDP": 16079731, "Year": 2022},
    {"Country": "Japan", "Continent": "Asia", "GDP": 5372804, "Year": 2022},
    {"Country": "Germany", "Continent": "Europe", "GDP": 4500629, "Year": 2022},
    {"Country": "India", "Continent": "Asia", "GDP": 3126107, "Year": 2022},
    {"Country": "United Kingdom", "Continent": "Europe", "GDP": 3164972, "Year": 2022},
    {"Country": "France", "Continent": "Europe", "GDP": 2991957, "Year": 2022},
    {"Country": "Brazil", "Continent": "South America", "GDP": 1868625, "Year": 2022},
    {"Country": "Italy", "Continent": "Europe", "GDP": 2057113, "Year": 2022},
    {"Country": "Canada", "Continent": "North America", "GDP": 1794182, "Year": 2022},
    {"Country": "South Korea", "Continent": "Asia", "GDP": 1785226, "Year": 2022},
    {"Country": "Australia", "Continent": "Oceania", "GDP": 1528633, "Year": 2022},
    {"Country": "Russia", "Continent": "Europe", "GDP": 1719691, "Year": 2022},
    {"Country": "Spain", "Continent": "Europe", "GDP": 1471819, "Year": 2022},
    {"Country": "Mexico", "Continent": "North America", "GDP": 1303682, "Year": 2022},
    {"Country": "Indonesia", "Continent": "Asia", "GDP": 1239111, "Year": 2022},
    {"Country": "Netherlands", "Continent": "Europe", "GDP": 1045672, "Year": 2022},
    {"Country": "Turkey", "Continent": "Asia", "GDP": 950606, "Year": 2022},
    {"Country": "Saudi Arabia", "Continent": "Asia", "GDP": 793970, "Year": 2022},
    {"Country": "Switzerland", "Continent": "Europe", "GDP": 749777, "Year": 2022},
    # 添加更多国家数据...
]


# 将数据写入CSV文件
csv_filename = "country_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Country", "Continent", "GDP", "Year"])
    writer.writeheader()
    writer.writerows(data)

print(f"CSV文件 {csv_filename} 已生成。")
