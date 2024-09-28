import cv2
from matplotlib import pyplot as plt
import os

def change_filename(before):
    ext = os.path.splitext(before)[1]
    path_without_ext = os.path.splitext(before)[0]
    front = path_without_ext[:-3]
    back = int(path_without_ext[-3:])
    print(back)
    if back%2 == 1:
        tag = "problem"
    else :
        tag = "solution"
    problem_num = (back+1)//2
    after = front+f"{problem_num}_{tag}{ext}"
    try: 
        os.rename(before, after)
    except  FileNotFoundError:
        print("변환 불가 파일입니다. 기 변환 파일일 수 있습니다")
        
def crop_to_content(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # Find non-zero (i.e., non-white) pixels
    coords = cv2.findNonZero(255 - image)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        return cv2.imwrite(path, image[y:y+h, x:x+w])
    else:
        return cv2.imwrite(path, image) 

# problems_set_path에 다음과 같은 raw 데이터를 준비합니다.
# 1. 한 쪽에 문제 하나, 하얀 배경, 검은 글씨
# 2. 사전식 정렬을 했을 경우 바로 다음 파일이 이전 문제에 대한 해설이어야 합니다. 물론 하얀 배경에 검은 글씨여야 합니다.
# 3. 그러면 아래 코드를 실행 시에, 문제 번호를 지정한 후, 컨텐츠를 crop 합니다.
image_extensions = ('.jpg', '.jpeg', '.png')
problems_set_path = "./math_problems/data/problems_set/crop_contents"
image_paths = [os.path.join(problems_set_path, file) for file in os.listdir(problems_set_path) if file.lower().endswith(image_extensions)]
for path in image_paths:
    change_filename(path)

image_paths = [os.path.join(problems_set_path, file) for file in os.listdir(problems_set_path) if file.lower().endswith(image_extensions)]
for path in image_paths:
    crop_to_content(path)