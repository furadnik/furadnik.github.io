---
pagetitle: Maximizing Truth Learning in a Social Network is NP-hard
lang: en
---

# Maximizing Truth Learning in a Social Network is NP-hard

This paper is a continuation of my work at [REU 2024](/projects/2024_reu).

We look at the problem of truth learning with unreliable information in a social network.
We analyze the complexity of deciding _how well_ a given network can learn.
We reach the conclusion that this problem is in fact NP-hard.
For more information, see the REU website.

This paper was written by me and [Amanda Wang](https://reu.dimacs.rutgers.edu/~aw1115/) with equal contribution, and by [Jie Gao](https://sites.rutgers.edu/jie-gao/about/).
It was accepted to the [24th International Conference on Autonomous Agents and Multi-Agent Systems](https://aamas2025.org/) in Detroit, United States.

An extended version was invited to the [AAMAS journal](https://link.springer.com/journal/10458), and is currently under review.

The paper can be accessed in the Proceedings [here](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p2078.pdf), as well as on [arXiv](https://arxiv.org/abs/2502.12704).

## Abstract

> Sequential learning studies prediction in social settings, where agents predicting in sequence may leverage not only their own private observations, but also past predictions broadcasted by earlier agents.
> This paper focuses on sequential learning in social networks, where agents only see predictions broadcasted by those in their immediate neighborhood.
> As such, the proportion of agents to successfully predict the ground truth exhibits a careful dependence on both the network topology and the order in which the agents make and announce their predictions. 
> A natural objective in this setting is thus to find an optimal ordering of agents, given a particular network, which maximizes the fraction of agents who make correct predictions.
> We show that absent specific assumptions on network structure, this basic desiderata is unattainable for both networks of fully rational agents and those with bounded rationality. 
> Indeed, we can construct a large class of networks for which it is computationally infeasible to determine an optimal ordering. We conclude by leveraging the same construction to prove a stronger hardness of approximation result.
