# Exercise 2.3 - Tiered Pricing

In this assignment, you will write a program that recommends a price tier that they should choose based on their needs.

## Background

The company Crazy Egg sells services that track user behaviour their clients' webpages.  They have a variety of pricing tiers based on client needs:

![Crazy Egg Price Tiers](/.lesson/assets/pricing.png)

## Requirements

Your program will ask the user for the following:
* The number of pageviews the site has
* The number of snapshots the client would like
* The number of recordings the client would like

The program should then print the recommended tier and its price.  The recommended tier is the lowest cost price which includes all of the client's needs.
* If the client's needs don't fit into the BASIC, STANDARD, PLUS, or PRO tiers, then the recommendation must be the ENTERPRISE tier.  Instead of printing a price, print `Contact us for a quote`.
* If any of the numbers are negative, print the error message `These values can't be negative`.

### Sample Executions

Use these samples to test your code and make sure that your formatting is correct.

*NOTE: These samples are not an exhaustive list of possible cases.  Consider code coverage and edge cases.*

**Sample #1**

```
How many pageviews will your site have? 100000
How many snapshots will you need? 40
How many recordings will you need? 75

You should subscribe to our PLUS tier
The cost is $99 per month
```

**Sample #2**

```
How many pageviews will your site have? 10000
How many snapshots will you need? 10
How many recordings will you need? 100

You should subscribe to our BASIC tier
The cost is $24 per month
```

**Sample #3**

```
How many pageviews will your site have? 50000
How many snapshots will you need? 200
How many recordings will you need? 750

You should subscribe to our ENTERPRISE tier
Contact us for a quote
```

## Submitting

When you are finished, push your code to GitHub.  Submit it on [Gradescope](gradescope.com) where it will be graded:
* Correctness - 70% (automatic)
* Efficiency - 10% (manual)
* Style - 20% (manual - see [Style Guide](https://mrdevet.github.io/ICS3C/assignments/Style-Guide/))

## Resources

The following lessons will be helpful with this exercise:

* **[Advanced Ifs](https://mrdevet.github.io/ICS3C/essentials/2-ifs/2-Advanced-Ifs/)**
  * [Ifs in Ifs](https://mrdevet.github.io/ICS3C/essentials/2-ifs/2a-Nested-Ifs/)
  * [Multiple Alternative](https://mrdevet.github.io/ICS3C/essentials/2-ifs/2b-Multiple-Alternatives/)
  * [Logical Operators](https://mrdevet.github.io/ICS3C/essentials/2-ifs/2c-Logical-Operators/)

* **[Testing](https://mrdevet.github.io/ICS3C/essentials/2-ifs/3-Testing/)**
