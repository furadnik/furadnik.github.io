---
pagetitle: Bachelor Thesis
lang: en
---

# Bachelor Thesis

I did my bachelor thesis on _Balancing Space Complexity and Ambiguity in Superadditive Set Functions_.
My supervisor was [Mgr. David Sychrovský](https://kam.mff.cuni.cz/~sychrovsky/) and my consultant was [RNDr. Martin Černý](https://kam.mff.cuni.cz/~cerny/).

The thesis is an extension of the paper [Reducing Optimism Bias in Incomplete Cooperative Games](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=7AvTiqgAAAAJ&citation_for_view=7AvTiqgAAAAJ:u-x6o8ySG0sC) to a more general setting of set functions.

The original version of the thesis can be found on the [Charles University Digital Repository](http://hdl.handle.net/20.500.11956/193133), or on [Github](https://github.com/furadnik/bakalarka/releases/tag/official).
However, since then, some minor mistakes were discovered.
I have fixed those, and the corrected version can be reached as the latest release on [Github](https://github.com/furadnik/bakalarka/releases/tag/latest).
The Github repository also contains the source code with a record of all changes made since the submitted version.

For this thesis, I received the [Prize of the Learned Society of the Czech Republic](https://www.mff.cuni.cz/cs/verejnost/aktuality/ucena-spolecnost-ocenila-studenty-matfyzu).


## Abstract

> Set functions offer a way to express the relationship between subsets of some finite ground set.
> This is used in countless fields, including explainable AI, combinatorial auctions, and cooperative game theory.
> However, when applying set functions to a real-world problem, there is a significant roadblock: their size grows exponentially in size of the ground set, while finding out the value of even a single subset might be hard---costing, e.g., money, time, or computational power.
> In this thesis, we present a framework for striking a balance between the resources we need to expend, and the amount of information we learn about the set function.
> We frame this as an optimization problem, for which we find both exact solutions as well as approximations via reinforcement learning.
> We establish a measure for the ambiguity arising from the unknown values and study its properties.
> We show the performance of our approaches on simple instances of the problem as well as on the very general class of supermodular functions.
> Further, we define a very simple heuristic which drastically decreases our ambiguity metric on the supermodular class while only requiring a linear number of values to be known.

