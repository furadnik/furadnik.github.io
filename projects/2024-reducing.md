---
pagetitle: Reducing Optimism Bias in Incomplete Cooperative Games
lang: en
---

# Reducing Optimism Bias in Incomplete Cooperative Games

In this paper, we investigate how to minimize the amount of information we
learn about a cooperative game, while getting an accurate estimation of the
Shapley value.

This paper was written by me, [David Sychrovský](https://kam.mff.cuni.cz/~sychrovsky/), [Jakub Černý](https://www.cernyjakub.com/) and [Martin Černý](https://kam.mff.cuni.cz/~cerny/).
It was accepted to the [23rd International Conference on Autonomous Agents and Multi-Agent Systems](https://www.aamas2024-conference.auckland.ac.nz/) in Auckland, New Zealand.

For this paper, I received the [Prize of Jirka Matoušek](https://www.mff.cuni.cz/en/kam/research/prize-of-jirka-matousek) 2024.

The paper can be accessed in the Proceedings [here](https://www.ifaamas.org/Proceedings/aamas2024/pdfs/p1847.pdf).
However, we recommend getting the version from [arXiv](https://arxiv.org/abs/2402.01930), in which we fixed some minor mistakes:

1. The error bars were changed to be the _standard error of the mean_, as is more common in literature (previously was the standard deviation of the values).
2. A typo was fixed in the statement of Proposition 3.4 (an extra $-v(N)$ after the second equals sign).


## Abstract

> Cooperative game theory has diverse applications in contemporary artificial
> intelligence, including domains like interpretable machine learning, resource
> allocation, and collaborative decision-making. However, specifying a
> cooperative game entails assigning values to exponentially many coalitions, and
> obtaining even a single value can be resource-intensive in practice. Yet simply
> leaving certain coalition values undisclosed introduces ambiguity regarding
> individual contributions to the collective grand coalition. This ambiguity
> often leads to players holding overly optimistic expectations, stemming from
> either inherent biases or strategic considerations, frequently resulting in
> collective claims exceeding the actual grand coalition value. In this paper, we
> present a framework aimed at optimizing the sequence for revealing coalition
> values, with the overarching goal of efficiently closing the gap between
> players’ expectations and achievable outcomes in cooperative games. Our
> contributions are threefold: (i) we study the individual players’ optimistic
> completions of games with missing coalition values along with the arising gap,
> and investigate its analytical characteristics that facilitate more efficient
> optimization; (ii) we develop methods to minimize this gap over classes of
> games with a known prior by disclosing values of additional coalitions in both
> offline and online fashion; and (iii) we empirically demonstrate the
> algorithms' performance in practical scenarios, together with an investigation
> into the typical order of revealing coalition values.
