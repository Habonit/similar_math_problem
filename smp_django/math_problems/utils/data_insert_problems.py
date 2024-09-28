import os
import django
import sys
# # 프로젝트의 최상위 디렉토리를 PYTHONPATH에 추가 : .py 확장자에서
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# # # 아래는 ipynb에서만 가능합니다. 
# sys.path.append(os.path.dirname((os.path.dirname(os.getcwd()))))

# Django 프로젝트의 설정 모듈을 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smp_django.settings")
django.setup()

import pandas as pd
from datetime import datetime
from math_problems.models import Problem

dir_path = './math_problems/data/problems_set'
chapter_num = 45
chapter_problem_path = os.path.join(dir_path, '_'+str(chapter_num))
problem_names = os.listdir(chapter_problem_path)
problem_paths = [os.path.join(chapter_problem_path, name) for name in problem_names]
data_lst = []
for name in problem_names:
    name = os.path.splitext(name)[0]
    chapter = int(name.split("_")[1])
    difficulty_level = int(name.split("_")[2])
    document_id = int(name.split("_")[3])
    temp_id = int(name.split("_")[4])
    type = str(name.split("_")[5])
    if type == 'problem':
        data_lst.append([chapter, difficulty_level,document_id,temp_id,"",""])
    else:
        continue
df = pd.DataFrame(data = data_lst, columns=['chapter','difficulty_level','document_id','temp_id','problem_path','solution_path'])

for name, path in zip(problem_names, problem_paths):
    name = os.path.splitext(name)[0]
    chapter = int(name.split("_")[1])
    difficulty_level = int(name.split("_")[2])
    document_id = int(name.split("_")[3])
    temp_id = int(name.split("_")[4])
    type = str(name.split("_")[5])

    condition = (df['chapter'] == chapter) & \
                (df['difficulty_level'] == difficulty_level) & \
                (df['document_id'] == document_id) & \
                (df['temp_id'] == temp_id)
                
    if type == 'problem':
        df.loc[condition, 'problem_path'] = path
        
    elif type == 'solution':
        df.loc[condition, 'solution_path'] = path
        
df = df.sort_values(by=['chapter', 'difficulty_level', 'document_id', 'temp_id']).reset_index(drop=True)
df['created_at'] = pd.NaT
df.loc[:, 'created_at'] = datetime.now()

for index, row in df.iterrows():
    Problem.objects.create(
        chapter_id=row['chapter'],
        문제_경로=row['problem_path'],
        해설_경로=row['solution_path'],
        난이도=row['difficulty_level'],
        문서_id = row['document_id'],
        created_at=row['created_at'],
    )
print("Data imported successfully!")
