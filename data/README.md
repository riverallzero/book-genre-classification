## _p

- 프롬프트 : 소문자 + 불용어 제거 + 중복 단어 제거 + 특수 문자 제거

```python
df["content"] = df["content"].str.lower().apply(remove_stopwords).apply(remove_duplicate_words).apply(re_sub)
```

## _f

- 프롬프트 : 소문자 + 불용어 제거 + 영단어 아닌 것 제거 + 중복 단어 제거 + 특수 문자 제거
- 제목 : 소문자 + 특수 문자 제거

```python
df["content"] = df["content"].str.lower().apply(remove_stopwords).apply(remove_non_english_words).apply(remove_duplicate_words).apply(re_sub)
df["Title"] = df["Title"].str.lower().apply(re_sub)
```
