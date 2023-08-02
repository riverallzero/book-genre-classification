# 2023-JBNU-SWUniv-AI

- 전북대학교 SW중심대학사업단 | 2023년 인공지능 온라인 경진대회
- 은상 수상(Public 5th, Private 5th)

## 대회 설명
본 대회에는 책 커버(이미지와 제목) 정보가 주어질 때, 책의 장르를 분류하는 문제를 해결합니다.
예를 들어, 아래 책 커버 이미지가 주어지고, 책 제목은 "Collins Touring Map Scotland 2014" 입니다.
이 책의 장르는 "Travel" 카테고리에 포함됩니다.
이미지와 텍스트 분류 문제는 추천 시스템, 상품 카테고리 분류 등 다양한 분야에서 널리 활용되고 있습니다.
본 대회 참여자들은 주어진 학습 데이터를 바탕으로 모델을 구축한 후, 테스트 데이터에 대해 성능을 내서 제출하면 됩니다.

<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5684203%2F824d5257913cdd775c288f67fdb47c7b%2F.JPG?generation=1684581039616516&alt=media" width="20%">

## 평가 지표
본 대회의 평가 지표는 Mean F1-Score입니다.

## 제출 양식
제출 파일은 반드시 두 열(id, label)만 포함하고 있어야 합니다.
테스트 파일에 존재하는 책 커버를 입력으로 책 장르를 예측하면 됩니다. 
제출 파일은 반드시 헤더를 포함하고 있어야 하며, 다음과 같은 형식으로 이뤄져야 합니다.

```text
id,label
1,Calendars
2,"Computers, Technology"
3,"Business, Money"
...
```

## 데이터 셋
- train_data.csv : 학습 데이터셋
- test_data.csv : 평가 데이터셋
- train : 학습 데이터셋과 연관된 이미지 파일들
- test : 평가 데이터셋과 연관된 이미지 파일들
- sample_submission.csv : 샘플 제출 파일

```text
id,Filename,Title,label
0,1101903236.jpg,The Oz Family Kitchen: More Than 100 Simple and Delicious Real-Food Recipes from Our Home to Yours,"Cookbooks, Food, Wine"
1,0804139857.jpg,"Living with Intent: My Somewhat Messy Journey to Purpose, Peace, and Joy",Self Help
2,0765334798.jpg,Redshirts: A Novel with Three Codas,"Science Fiction, Fantasy"
...
```
