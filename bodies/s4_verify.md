# 검증 V1 — 전체 집계 합격률

`analysis.py` 집계 결과:

| 성별 | 합격률 |
|------|--------|
| 여성 (Female) | **30.4%** |
| 남성 (Male)   | **44.5%** |

격차 = 14.1%p. 표면적으로 여성이 크게 불리해 보인다.

```
agg = df.groupby("Gender").apply(lambda g: g.Admitted.sum()/g.Total.sum())
Female  0.304   Male  0.445
```

이 숫자만 보면 H1이 지지되는 듯하다. **그러나** 학과별 지원 분포를 아직 통제하지 않았다.
