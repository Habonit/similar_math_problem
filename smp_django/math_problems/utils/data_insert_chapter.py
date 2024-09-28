import os
import django
import sys
# 프로젝트의 최상위 디렉토리를 PYTHONPATH에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Django 프로젝트의 설정 모듈을 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smp_django.settings")
django.setup()

import pandas as pd
from datetime import datetime
from math_problems.models import Chapter

## chapter table에 데이터를 삽입합니다.
csv_path = './math_problems/data/chapter.csv'
df = pd.read_csv(csv_path)
# id와 수정 시간 부여
# df.loc[:, 'id']=range(1,len(df)+1)
# df['id']=df['id'].astype(int)
df['created_at'] = pd.NaT
df.loc[:, 'created_at'] = datetime.now()

print(df)

# 데이터베이스에 데이터 삽입
for index, row in df.iterrows():
    Chapter.objects.create(
        학교=row['학교'],
        학년=row['학년'],
        대단원명=row['대단원명'],
        소단원명=row['소단원명'],
        created_at=row['created_at']
    )
print("Data imported successfully!")