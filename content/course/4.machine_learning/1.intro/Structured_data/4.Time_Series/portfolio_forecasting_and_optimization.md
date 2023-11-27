# Portfolio forecasting and optimization, an introduction to Financial Engineering

- Repository: `time-series`
- Type of Challenge: `Learning`
- Duration: `5-7 days with deployment. (Tested with Bouman 5)`
- Deadline: `xx/xx/20xx 17:00` ****(code)****
- Presentation: `xx/xx/20xx 10:00`
- Team challenge : 2-5

## Mission objectives

- Understand time-series manipulations
- Understand time-series forecasting
- Familiarity with basic finance vocabulary
- Experience an optimization problem
- Deploy an app with Gradio

## The Mission

You are in the second round of an interview process with a big financial institution. You're past the HR interview. Congratulations! The real process begins.

They give you a few days to create a web app in which the user can choose a list of stocks, a time range and frequency (days, months, years) and from these inputs calculate the **optimal portfolio** using the most well-known technique, the **mean-variance optimization** method. As is standard in this case, you will need to display the **efficient-frontier** as well the **historical return, volatility, Sharpe and Sortino ratios** for the optimal portfolio.

After a quick search, you find the well-known [Portfolio Visualizer](https://www.portfoliovisualizer.com/) website. The **Porfolio Optimization** section seems the most relevant. You explore the **Historical Efficient Frontier** and the **Portfolio Optimization** tools. Then, because you're curious, you also check the others tools.

It is your time to impress. You think you can do better using your Machine Learning chops. You decide to go the extra mile and not only optimize historical portfolios at the end of the **look back** period but to also:

* forecast future prices over a **new** time range
* find the optimal portfolio over this **new** time range
* find the **actual optimal portfolio** using the actual prices on this **new** time range
* compare the 3 portfolios (return, volatility etc.) **over the new period**

That way, you will be able to show the efficacy of mean-variance optimization using past data as well as the relevance of forecasting solely based on prices. You can also reflect, as a bonus, on the merits of your approach compared to the Black-Litterman optimization.

This should be enough to get to the next interview step in style.

## Roadmap

1. Look-up the finance lingo.
2. Play around with [Portfolio Visualizer](https://www.portfoliovisualizer.com/) keeping an eye on the user-experience.
3. Explore the [Riskfolio-Lib](https://riskfolio-lib.readthedocs.io/en/latest/index.html) and in particular [Tutorial 1](https://github.com/microprediction/Riskfolio-Lib/blob/master/examples/Tutorial%201.ipynb). (This [deprecated, but still fresh, module](https://github.com/robertmartin8/PyPortfolioOpt) could also be used.)
4. Choose between [Kats](https://facebookresearch.github.io/Kats/) and [PyCaret](https://pycaret.org/) for regression.
5. Deploy your app using [Gradio](https://gradio.app/).
6. Present a 5 minutes live-demo.


## Evaluation criteria

| Criteria       | Indicator                                                | Yes/No |
| -------------- | -------------------------------------------------------- | ------ |
| 1. Is complete | Your optimization works.                                 | [ ]    |
|                | The APP is clear and the presentation is understandable. | [ ]    |
|                | README is pimped.                                        | [ ]    |
|                | Your model is trained and can forecast prices .          | [ ]    |
|                | Your APP is deployed on Gradio.                          | [ ]    |
|                | Your MVP meets the client needs **exactly**.             | [ ].   |
| 2. Is good     | The repo doesn't contain unnecessary files.              | [ ]    |
|                | You used typing.                                         | [ ]    |
|                | The presentation is clean.                               | [ ]    |
|                | The web-dev group understood well how your API works.    | [ ]    |

![You've got this!](https://media.giphy.com/media/V9PBVKTzKveVQfDlVp/giphy.gif)


Finance Lingo:  the key financial concepts and lingo related to portfolio optimization. This includes understanding terms like mean-variance optimization, efficient frontier, historical return, volatility, Sharpe ratio, Sortino ratio, and Black-Litterman optimization.

Portfolio Visualizer:   the Portfolio Visualizer website to get a sense of the user experience and understand how it currently handles portfolio optimization and visualization. Pay attention to the features and functionalities it offers.

Riskfolio-Lib:  Riskfolio-Lib library and specifically Tutorial 1. This library can be a valuable resource for portfolio optimization and risk analysis. Additionally, consider checking out the PyPortfolioOpt module.

Choose ML Framework: Decide whether you want to use Kats or PyCaret for time series regression to forecast future prices. Choose the framework that aligns with your project requirements and expertise.