---
pagetitle: REU 2024
lang: en
bibliography: references.bib
link-citations: true
---

<div id="profilepic_div"><img id="profilepic" src="data/profile_pic.jpg"/></div>
# Filip&nbsp;Úradník
I'm a Bachelor student of Computer Science at&nbsp;[MFF&nbsp;UK](https://mff.cuni.cz/).
For more info about me, take a look at&nbsp;my&nbsp;CV, either in&nbsp;[Czech](https://github.com/furadnik/cv/releases/download/latest/uradnik_cv_cz.pdf)
or&nbsp;[English](https://github.com/furadnik/cv/releases/download/latest/uradnik_cv_en.pdf), or&nbsp;visit my&nbsp;[personal&nbsp;website](https://furadnik.github.io/).

## Contact me

My office is in the CoRE building, room 434.

You can also send me an [email](mailto:uradnik@kam.mff.cuni.cz) or&nbsp;contact me on [Matrix](https://matrix.to/#/@furadnik:matrix.org).

# Truth Learning in Social and Adversarial Setting

At [REU 2024](https://reu.dimacs.rutgers.edu/2024/), I work on _Truth Learning in a Social and Adversarial Setting_ with&nbsp;[Julia Križanová](https://reu.dimacs.rutgers.edu/~jk2238/), [Rhett Olson](https://reu.dimacs.rutgers.edu/~ro330/), and&nbsp;[Amanda&nbsp;Wang](https://reu.dimacs.rutgers.edu/~aw1115/).
Our mentor is Professor [Jie Gao](https://sites.rutgers.edu/jie-gao/about/).
We further collaborate with [Kevin Lu](https://www.math.rutgers.edu/people/department-directory/detail/344-department-directory/1983-lu-kevin).

## Project Description

Let $G = \left( V,E \right)$ be a directed multigraph representing a network of $n := |V|$ agents.
Let $q \in (0,1)$ and $p \in (\frac 12, 1)$. 
We have a *ground truth* $\theta \sim \text{Ber}(q)$, which the agents are trying to learn.
Each agent $v$ has some private information $s_v$, which can have values 0 or 1, such that $\text{Pr}[s_v = 1 \;|\; \theta = 1] = \text{Pr}[s_v = 0 \;|\; \theta = 0] = p$.
The variables $\{s_v \;|\; v \in V\}$ are independent given $\theta$.
Each agent $v$ makes a prediction $a_v$ of the ground truth according to a decision ordering, where predictions are based on both private information and the predictions of in-neighbors earlier in the ordering. 
We denote the sequence of all private signals as $s = (s_v \;|\; v \in V)$.

We consider a *majority vote* setting, where an agent $v$ in some given ordering $\sigma$ can see the neighborhood $N = \{u \;|\; uv \in E \land \sigma(u) < \sigma(v) \}$, and chooses an action  $$
    a_v = \begin{cases}
        1 & \frac 1{|N|+1}(\sum_{u \in N} a_u + s_v) > \frac 12, \\
        0 & \frac 1{|N|+1}(\sum_{u \in N} a_u + s_v) < \frac 12,\\
        s_v & \text{otherwise.}
    \end{cases}
$$

The goal of our project is to find out, if it is NP-hard to decide, whether there exists an ordering of the agents $\sigma$, such that the expected error they make is small, or in other words, $$
		\mathbb{E}_{\theta, s} \left[ \frac{\sum_{v \in V}^{} {[a_v \neq \theta]}}{n} \right] < \varepsilon.
$$

<!-- For further details, see our [final presentation](data/final_prez.pdf). -->

## Week log

* _Week 1_: 05/29--06/02
    - I did research about information cascades and voting [@easley2010networks].
    - I created a website for this project.
    - I started working on the [initial presentation](data/initial_prez.pdf) of the project.

* _Week 2_: 06/03--06/09
    - We have finished and given the [initial presentation](data/initial_prez.pdf).
    - I have read a paper about complexity of a decision process in a similar model to ours [@hazla2019reasoning].
    - We have discussed a statement of a complexity problem regarding optimal learning order.
    - I have started to work on a proof of the complexity problem regarding optimal learning order.

* _Week 3_: 06/10--06/16
    - We have discussed the proof of the complexity problem of deciding the optimal learning order with Kevin Lu.
    - I have started to work on a new problem concerning the comparison of Bayesian and Majority models.
    - We have further discussed adversarial approaches to the sequential learning setting.

* _Week 4_: 06/17--06/23
    - We have discussed the proof of the complexity problem of deciding the optimal learning order with Prof. Gao.
    - I found (and then successfully removed, yay) a bug in our initial computation of probabilities.
    - We have finished write-up of our complexity proof along with (messy) technical details with Amanda.

* _Week 5_: 06/24--06/30
    - We discussed another setting of network learning, this time based on learning from crowds with Prof. Gao.
    - We did some minor edits of the write-up and sent it to the others to read.
    - I've tried to prove that the expected learning rate is always better when using Bayesian learning, compared to majority vote.
    
* _Week 6_: 07/01--07/07
    - We have discussed extending the proof to non-directed graphs without multi-edges.
    - We have discussed the majority vs. Bayesian problem, I have found a counterexample when adversarial players are present.
    - I have examined the possibility of extending the proof to (still directed) graphs without multi-edges.
    - I put together a script for computing the expected learning rate in an arbitrary network.
    - I have found a construction which reduces 3-SAT to our problem without multi-edges, didn't have time to write it down fully, as it is involved and messy.

* _Week 7_: 07/08--07/14
    - I have simplified the structure of the write-up.
    - I started making some of the notation a bit clearer.
    - I added bibliography to the write-up.
    - I worked on the format of the write-up---adding the option to render it in the plain, IEEE, and AAMAS format. 
    - We have discussed the possibilities of publishing our work.
    - We have decided that we will give the final presentation together as a big group.

* _Week 8_: 07/15--07/21
    <!-- - We made the [final presentation](data/final_prez.pdf). -->
    - We made the final presentation.
    - We discussed the generalization of our proof for other settings.
    - We considered notation in our paper.
    <!-- - We gave the [final presentation](data/final_prez.pdf). -->
    - We gave the final presentation.
    - I worked on reports for both DIMACS and CoSP.

* _Week 9_: 07/22--07/28
    - I continued to work on the final DIMACS report.
    - I made and gave a [presentation](https://github.com/furadnik/reu_prez/releases/tag/latest) on Cooperative Game Theory, as a part of the REU Student Workshop seminar in Prague.
    - I attended lectures, which were a part of the REU program at Charles University in Prague.

## Acknowledgments

<div id="eu_div"><img id="eu" src="data/eu.png"/></div>
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 823748.

## References
