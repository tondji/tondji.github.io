---
layout: post
title: "ATP Tennis Analysis, 2006 - 2015: Do Lefties have an Advantage?"
author: "Ethan Wicker"
categories: journal
tags: [tennis, data analysis]
image: tennis-nadal-serving.jpg
---

## Introduction

This post is the third in a series covering an analysis of ATP (Association of Tennis Professionals) tennis matches during the 10-year span between 2006 and 2015.  You can find the first two posts in this series at the following links:

* [ATP Tennis Analysis, 2006 - 2015: An Introduction and Data Cleaning](https://ethanwicker.github.io/journal/atp-tennis-analysis-2006-2015-an-introduction-and-data-cleaning.html).
* [ATP Tennis Analysis, 2006 - 2015: Constructing Useful Data Frames](https://ethanwicker.github.io/journal/atp-tennis-analysis-2006-2015-constructing-useful-data-frames.html)

For anyone interested, my entire R project for this analysis [can also be found here](https://github.com/ethanwicker/atp-tennis-analysis).

In this post I will be discussing whether or not left-handed players have an advantage over their right-handed counterparts.  To provide some context, it has long been thought that lefties have an advantage over righties in various sports, and tennis especially, is no exception.  

In tennis, there are various reasons why left-handed players are thought to have an advantage over right-handed players.  A crucial reason, if not the largest advantage lefties might possess, is that service games in tennis always start in the deuce court (right side) and then serves alternate from there, switching between the ad court (left side) and back to the deuce court until the service game is over.  What this means, is that more often than not, and every time the score of a service game is 40-40 (called deuce), the last serve of the service game will come from the ad court. Due to the manner in which the net in tennis is pulled down from the middle, coupled with how players mechanically serve to produce spin, this is thought to provide an advantage to lefties.

Another typical reason lefties are thought to have an advantage is just that there are less of them.  They're just a rarer breed.  And since players typically play right-handed players, when they face the occasional left-handed player, they're thrown off their game.  For a more tennis exact rational of this, this often has to do with both tennis strategy, and the spin of the ball coming off different shots.  In short, when playing a leftie, a player has to flip their strategy upside down.  All of a sudden, hitting a backhand approach has to be hit to the opposite side.  And as for the spin, tennis players rarely hit perfect 6-o'clock-to-12-o'clock spin on the ball.  Often times that spin has a little or a lot of sidespin mixed in as well - think 5-o'clock-to-11-o'clock for a right-handed forehand.  This spin completely changes how the ball flies through the air, how the ball bounces, and potentially, how a player has to redirect the ball to counter the spin.

This only scratches the surface of the advantages and disadvantages of handedness in tennis, but if you were unfamiliar with the nuances of the sport, it provides you with enough information to see the legitimacy in the question.

For the remainder of this post, I'll be describing my methods and my results, as well as including and discussing various segments of my R code.  I'll be discussing some smaller topics in each section, such as if lefties serve more aces or win a higher percentage of service games.  Towards the end of this post, I'll perform some more in-depth statistical analysis (i.e. a Two Sample Proportion z-Test) and I'll summarize my results.

So, do lefties really have an advantage?

The answer: No.  Not a bit.  If anything, they lose more matches than they should.  Which is curious.  

In the rest of this post you'll find my rationale and supporting arguments.

I should pause right here and make one very important point.  My analysis shows that lefties, during the 10-year span from 2006 to 2015 did not have an advantage over right handed players (in part because they lost more often to righties than won over them).  This analysis, and the resulting conclusion only hold true for ATP World Tour players (i.e. the top 250 or so players in the world), and cannot really be extrapolated beyond these elite players.

In particular, I would absolutely be willing to extend my conclusion out some years and bet that lefties still do not have an advantage in today's game.  But this analysis cannot be used to draw any conclusions about lower skilled players.  Among lower level players, such as those on the Challenger or Future circuits, or even college players in the US, lefties almost universally have an advantage (although some future analyses would be needed to really show this).  And of course, at even lower levels, we would imagine the advantage would increase.  However, my analysis is only concerned with ATP World Tour players between 2006 and 2015, and the results of my analyses cannot properly be extrapolated to lower level players.  See the conclusion section of this post for more details.

---

## The Analysis  

To begin this analysis, I'll first look at specific match statistics to see if, for example, left-handed players serve better or if they win more break points.  After that, I'll turn my attention towards match-ups of left-handed players versus right-handed players.  And finally, I'll then look at the overall proportions of matches won by left-handed players versus right-handed players to see if there is any statistically significant difference.

Unfortunately, the playing hand for 114 out of the 832 unique players in my data set is unknown.  These players are mostly players that only played in a couple of smaller tournaments and were not very successful at this level of the game.  The mean and median world ranking for these players is 314 and 275, respectfully.  The mean and median total number of matches played for these players was 2.47 and 1, confirming their lack of playing time.  Regardless, since their playing hand is unknown, they have to be removed from my data set for the purposes of this analysis.

Note:  For the majority of this analysis, I'll be referencing the `atp_stats_overall_by_player` data frame constructed in my second post in this series.  See that post for more details on how it was constructed.

```r
# Fitlering out where player's hand is unknown
atp_stats_overall_by_player_left_right_known <- atp_stats_overall_by_player %>% filter(hand != "Unknown")
```

Furthermore, it's worth checking a couple of conditions before diving into the bulk of my analysis.  The first condition worth checking is to ensure that there is a relatively even distribution of left-handed players and right-handed players in the data set.  If for instance, lefties really did have an enormous advantage, and there were a disproportionate amount of them among the very top players, that could throw off some of my later analyses.  

```r
# Creates boxplot - making sure lefties are uniformly dispersed across players
atp_stats_overall_by_player_left_right_known %>% ggplot(aes(x = hand, y = avg_rank, color = hand)) + 
  geom_boxplot() +
  labs(title = "Average Player World Ranking by Hand",
       y = "Average Player Ranking",
       x = "Hand") +
  coord_flip() + 
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14),
        plot.title = element_text(size = 16, hjust = 0.5)) 
  ```
  
![alt text](/assets/img/tennis-left-right-distribution.jpeg "Tennis-left-right-distribution")
  
We can see in the above boxplots that the distribution of left-handed players and right-handed players seems to be pretty even across the rankings.  Of course, since there are more righties, we would expect their overall spread to be larger, and it is.  To quantify this a little more, the median world ranking is 147 and 153 for all left-handed and right-handed players, respectfully.  The mean world ranking for each is 187 and 201.
  
Looking at world rankings alone, it appears that lefties do tend to be ranked higher, but there is more to the story.

The other condition worth checking is the percentage of lefties in the data set.  According to a quick Google search, somewhere between 10% and 13% of the world's population is left-handed.  In my data set of 718 unique players, 13.93% are left-handed.  This is a bit higher than we'd expect, assuming that left-handedness would be equally common among ATP Tennis Players as the rest of the world.  Although it seems to be a bit higher than the world average, it's not all that far off.

### Specific Match Statistics

In the above, I've shown that left-handedness isn't any more rare or more common in ATP Tennis Players than in the general population, and that left-handed players are pretty well distributed among all the players, regardless of rank.

In this portion of the post, I'll be comparing overall match statistics for left-handed players versus right-handed players.  

To begin, I'll be looking at whether or not lefties **serve more aces**.  To determine this, I calculated the average number of aces served per service point for both left-handed and right-handed players.  

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_ace_per_service_point_by_hand = mean(pct_ace_per_service_point, 
                                                     na.rm = TRUE))                                                     
```
Per service point, lefties on average serve 6.29% aces.  For righties, that number increases slightly to 6.38%.  This is a fairly small increase, and as I'll show later not statistically significant.

To continue with the offense side of things, next I'll look at whether lefties or righties win a higher percentage of **points off the first serve**.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_points_won_off_first_serve_by_hand = mean(pct_points_won_off_first_serve, 
                                                              na.rm = TRUE))
```

There are similar results here.  Left-handed players win 66.8% of their points when they get their first service in, while right-handed players win 67.6%.  Once again, although the righties are just a nudge higher, the differences are quiet small.

Below I'll repeat the same procedure, but this time to determine which type of player wins a higher percentage of **points off the second serve**.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_points_won_off_second_serve_by_hand = mean(pct_points_won_off_second_serve, 
                                                               na.rm = TRUE))
```

On the average, left-handed players win 46.9% of points after missing their first serve and getting their second serve in.  For right-handed players, that percentage increases slightly once again to 47.3%.  

On a side note here,  it's interesting that both left-handed and right-handed players win less than 50% of service points off their second serve.  This would be an interesting place for further exploration.  Perhaps on the whole, players would be better off increasing their second serve speed or placing their serves closer to the lines (i.e. taking more risk) to get their percentage of points won off the second serve above 50%.

To finish looking at the offensive side, I compared whether left-handed or right-handed players win a higher **percentage of service games**.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_service_games_won_by_hand = mean(pct_service_games_won, 
                                                     na.rm = TRUE))
```
On the average, left-handed players win 69.6% of their service games.  Once again, right-handed players win a slightly higher percentage of their service games at 70.4%.

Moving to the defensive side of the ball, I looked at whether lefties or righties win a higher percentage of the break points they force, as well as which handed players win a higher percent of return games.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_break_points_converted_on_defense_by_hand = 
              mean(pct_break_points_converted_on_defense, na.rm = TRUE))
```

As for the **average percentage of break points converted** on defense, lefties convert 36.4% and righties convert 37.3%.

The last defense statistic I looked at was the **percentage of return games won**.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_return_games_won_on_defense = 
              mean(pct_return_games_won_on_defense, na.rm = TRUE))
```

On the average, lefties win 16.1% of their return games, while righties win 16.8%.

And finally, the last overall statistic I looked at is on the average, which type of player wins a higher **percentage of their matches**.

```r
atp_stats_overall_by_player_left_right_known %>% 
  group_by(hand) %>% 
  summarize(avg_pct_matches_won_by_hand = mean(pct_matches_won, 
                                               na.rm = TRUE))
```

Across the board, left-handed players win an average of 25.7% of their matches, while right-handed players win an average of 27.6%.

Below is a summary table for the above information.  Note: "Avg Pct" stands for "Average Percent"

Statistic | Left-Handed Players | Right-Handed Players | Type of Player with Higher Stat | Significant at \\( \alpha = 0.05 \\) Level?
--------- | ------------------- | -------------------- | ------------------------------- | -------------------------------------------
Avg Pct Ace Per Service Point | 6.29% | 6.38% | Right | No
Avg Pct Points Won Off 1st Serve | 66.8% | 67.6% | Right | **Yes**
Avg Pct Points Won Off 2nd Serve | 46.9% | 47.3% | Right | No
Avg Pct Service Games Won | 69.6% | 70.4% | Right | No
Avg Pct of Break Points Converted |36.4% | 37.3% | Right | No
Avg Pct Return Games Won | 16.1% | 16.8 | Right | No
Avg Pct Matches Won |25.7% | 27.6% | Right | No

I also performed a Two-Sample t-Test on each of the above statistics to see if the differences in any were significant at the \\( \alpha = 0.05 \\) significance level.  The only statistic that was significant was the average percentage of points won off the first serve, with a p-value of 0.02948.  This p-value, although below the common threshold of 0.05, isn't terribly low, so I wouldn't feel comfortable stating that right-handed players win significantly more points off their first serve than left-handed players.

For completeness, and for anyone interested in the syntax, I've provided my R code for the significant result below.  To perform a t-Test on a different variable, just change out the appropriate portion of code.

```r
t.test(atp_stats_overall_by_player_left_right_known$pct_first_serves_in ~ 
         atp_stats_overall_by_player_left_right_known$hand)
```

Although there was only one statistically significant mean difference for all seven stats above, right-handed players were, on average, higher across the board.  This provides evidence to support my argument that left-handed players do not have an advantage amongst the highest level of professional male tennis players.

However, just slightly higher percentages across seven stats isn't exactly clear evidence for any verdict.  In the rest of this post I'll be comparing head-to-head matchups between left-handed and right-handed players.  I'll also be examining the overall proportion of matches won and lost by left-handed and right-handed players to see if there is any discernible difference.

### Head-to-head Matchups

In this portion, I'll be looking at head-to-head matchups between left-handed players and right-handed players.  The objective here is to see if, on the average, lefties or righties win more in matches between each other.

If left-handed players have an advantage, we would expect them to win more matches against right-handed players.  That is, we would expect them to win more than 50% of these matches, due to this supposed advantage.

In the below chunk of code I created the data frame `matches_right_vs_left` which contains the percentage of these matches won by left-handed players, as well as the percentage won by right-handed players.  These values are of course complements to each other.

```r
number_matches_right_vs_left_won_by_right <- atp %>% 
  filter((winner_hand == "Right" & loser_hand == "Left")) %>% 
  summarize(number_right_vs_left_won_by_right = n())

number_matches_right_vs_left_won_by_left <- atp %>% 
  filter((winner_hand == "Left" & loser_hand == "Right")) %>% 
  summarize(number_right_vs_left_won_by_left = n())

matches_right_vs_left <- number_matches_right_vs_left_won_by_right %>% 
  bind_cols(number_matches_right_vs_left_won_by_left) %>% 
  mutate(total_matches_right_vs_left = number_matches_right_vs_left_won_by_right + 
           number_matches_right_vs_left_won_by_left,
         pct_matches_right_vs_left_won_by_right = number_matches_right_vs_left_won_by_right/
           total_matches_right_vs_left,
         pct_matches_right_vs_left_won_by_left = number_matches_right_vs_left_won_by_left/
           total_matches_right_vs_left)
```

From the above data frame, we can see that 48.1% of head-to-head matchups are won by the left-handed player, while 51.9% are won by the right-handed player.

So across 10 years of modern man's tennis, right-handed players have actually won a higher percentage of these match ups than left-handed players.  

### Proportion of Match Wins and Loses

In the last portion of my analysis below, I explored the proportion of all matches won and lost by left-handed and right-handed players between 2006 and 2015.  Using a Two-Sample proportion test, I then show that right-handed players win a statistically significant higher proportion of their matches.

To perform the significance test, I first need to organize my data in a more useful manner.  In particular, I need my data such that each row contains information on a single match for a single player.  I also need to create two new variables, `result` and `hand`, that state whether a player won the match or lost the match, and which hand that player plays with.

The begin to organize my data, I first subsetted the `atp` data frame to get the relevant columns of interest.  I assigned this new subsetted data frame to `atp_hand_analysis`.

```r
atp_hand_analysis <- atp[, c("tourney_id", "tourney_date", "tourney_name", "surface", 
                         "winner_name", "loser_name", "winner_hand", "loser_hand", 
                         "winner_rank", "loser_rank")]
```                         
                         
Next I need to create two new variables, `result` and `hand`, which I'll later use to sum up the total number of wins and loses per each type of player.  To create these two new variables, I used the `gather` function from the `tidyr` package. 

`gather` is a function commonly used to gather a data frame over two columns that should really be one.  That is, in an instance where one variable is spread out over two columns, gather can be used to restructure the data such that these two columns are fully represented in one variable.  This often times makes the data easier to manipulate.

In the context of this situation, I am using `gather` to reorganize the `winner_hand` and `loser_hand` columns into one column: `hand`. 
Before using this function, I renamed the `winner_hand` and `loser_hand` columns to `Won` and `Lost`.  I then gathered the data over those two columns.  As you can see, I set the `key` argument equal to `result`, and the `value` argument equal to `hand`.  `gather` then restructures the data by putting the column names `Won` and `Lost` in the new `result` column, and puts the information from these columns in the `hand` column.  Since these columns contain information on the match winner and match loser playing hand, this makes sense.

Gather also necessary doubles the length of the data frame, since a row is created for each match winner and match loser, unlike in the original data frame where each row contained information on an entire match.

```r
# Renaming columns to more relevant names, and using gather to organize data
atp_hand_analysis <- atp_hand_analysis %>% 
  rename(Won = winner_hand, Lost = loser_hand ) %>%      
  gather(key = result, value = hand, Won, Lost) 
```

Now that I've used `gather` to better organize my data, I can sum how many matches were won and lost for left-handed players and right-handed players across all years of the original data set.

Before doing this, I need to filter out all the rows where a player's playing hand is not known.

```
# Filtering out players with unknown hand
atp_hand_analysis <- atp_hand_analysis %>% filter(hand != "Unknown")
```

I also defined the levels of the `result` variable so that `Won` comes before `Lost`.  This is not necessary, but when performing the proportion test, this allows me to get the proportion of matches won instead of the proportion of matches lost, which suits my needs better.

```r
atp_hand_analysis$result <- factor(atp_hand_analysis$result, levels = c("Won", "Lost"))
```

Finally, to count how many matches were won and lost for each type of player, I used the convenient `table` function provided in base R. 

```
table_of_right_left_won_lost <- table(atp_hand_analysis$hand, 
                                      atp_hand_analysis$result)
```
The resulting table is below.
 
  []() | Won   | Lost  
 ----- | ----- | ----
 **Left**  | 3148  | 3329  
 **Right** | 22503 | 22143 

Now with the above table of counts, we can perform a significance test to see if the difference in the proportion of matches left-handed players won is significantly different from the proportion of matches right-handed players won.  To perform this test, I used the `prop.test` function.

```r
# Two Proportion z-Test
prop.test(table_of_right_left_won_lost)
```

I've included the R printout of the results of this test in full below.

```r
  2-sample test for equality of proportions with continuity correction

data:  table_of_right_left_won_lost
X-squared = 7.2624, df = 1, p-value = 0.007041
alternative hypothesis: two.sided
95 percent confidence interval:
 -0.031118241 -0.004890228
sample estimates:
   prop 1    prop 2 
0.4860275 0.5040317 
```

In the above R printout, `prop 1` is the proportion of matches left-handed players won, and `prop 2` is the proportion of matches right-handed players won.  So, during the 10-year span from 2006 to 2015, left-handed players won 48.6% of their matches, while right-handed players won 50.4% of their matches.

The p-value of this test was 0.007041, which is much lower than the common significance level of \\( \alpha = 0.05 \\), or even \\( \alpha = 0.01 \\).  This test provides statistically significant evidence that right-handed players actually win a higher proportion of their matches than left-handed players.

I should mention here that the independence clause of the proportion test might be a bit shaky.  If we assume that all of the matches in the data set are independent of each other, then the results of the test hold.  However, this assumption may or may not be completely true, and is certainly up for debate.  There are various ways the matches may or may not be independent.  If right-handed players, for example, have some slight advantage, then as they advance through tournaments over left-handed players we might expect them to continue advancing.  Or we could pick out the 31 matches in which the right-handed Roger Federer played the left-handed Rafael Nadal across these 10 years.  Nadal won 67.7% of these matches, so clearly the leftie here won a significantly higher proportion of matches.

However, I do think the independence assumption here is appropriate, especially with my immensely large sample size.

Out of curiosity, I took a second look at matches between players ranked in the top 100, to see if the results were still significant.  I've provided the supporting R code as well as the `prop.test` output below.

```r
atp_hand_analysis_top_100_players <- atp_hand_analysis %>% 
  filter(winner_rank <= 100 & loser_rank <= 100)

table_of_right_left_won_lost_top_100 <- table(atp_hand_analysis_top_100_players$hand, 
                                              atp_hand_analysis_top_100_players$result)

prop.test(table_of_right_left_won_lost_top_100)

  2-sample test for equality of proportions with continuity correction

data:  table_of_right_left_won_lost_top_100
X-squared = 3.7478, df = 1, p-value = 0.05288
alternative hypothesis: two.sided
95 percent confidence interval:
 -0.0332560735  0.0001973874
sample estimates:
   prop 1    prop 2 
0.4854908 0.5020201 
```

For matches only between the top 100 ranked players in the world at any given time between 2006 and 2015, left-handed players won 48.5% of their matches while right-handed players won 50.2%.  This time, the p-value is still low at 0.05288, but it doesn't quite surpass the \\( \alpha = 0.05 \\) significance threshold.  So if we want to be stringent, the difference in the proportions of wins for left-handed players and right-handed players is not statistically significant if we only look at matches between the top 100 players.  However, it is just barely over the threshold, so I feel comfortable saying there is still supporting evidence to state that right-handed players win more matches than left-handed players across all players.

---

## Conclusion

To close out this post, I'll be summarizing my supporting arguments to show that left-handed players, at the ATP World Tour Level, do not have an advantage.  And then briefly after that, I'll discuss a completely speculative hypothesis for why I believe this may be the case.

### Summary

In this post, I showed significant evidence against the claim that left-handed players have an advantage.  This argument, of course, only hold weight at the very top tier of professional men's tennis, and should not extrapolated to any other tier of either the men's or women's game.

In looking at just averaged statistics, I showed that right-handed players outperform left-handed players in every category.  The statistics I looked at were:

* average percentage of ace per service point
* average percentage of points won off the first serve
* average percentage of points won off the second serve
* average percentage of service games won
* average percentage of break points converted
* average percentage of return games won
* average percentage of matches won

In each of these statistics, right-handed players were slightly above left-handed players.  Only one of these statistics, the average percentage of points won off the first serve, was found to be statistically significant.

In looking at matches played between left-handed and right-handed players, I showed that right-handed players win 51.9% of these matches.

Finally, I examined the overall proportion of matches won for both left-handed and right-handed players.  Across all matches in my data set from 2006 to 2015, left-handed players won 48.6% of their matches, while right-handed players won 50.4% of their matches.  A proportion test to see if there was a difference in the proportion of matches won by left-handed and right-handed players had a statistically significant result, with a p-value of 0.007041.  That is, we would expect the difference in proportions to be this extreme, in either direction, less than 1 out of 100 times.

I also reexamined the proportion of matches won for the top 100 players in the world.  For just this subset of data, left-handed players won 48.5% of their matches, while right-handed players won 50.2% of their matches.  The results of this proportion test were just above the statistically significant threshold, with a p-value of 0.05288.

To summarize, my analysis has show that left-handed players absolutely do not have an advantage at the ATP World Tour Level of men's professional tennis.  They systematically have lower match statistics than right-handed players, they lose over 50% of the time to right-handed players, and they also win a significantly lower proportion of their overall matches than right-handed players.

### Speculation

Finally, I'd like to include a few last comments in this post.  In this section, I'll be providing a completely speculative hypothesis for why left-handed players do not have an advantage at the highest level of men's professional tennis.

Just about any athlete will tell you that left-handed players have an advantage in any appropriate sports, and tennis is no different.  As a tennis player myself, there is no refuting that left-handed players absolutely have an advantage at some level of the game.  In lower levels of the game, such as juniors or college, left-handed players are rarer and certainly have some advantage over right-handed players, simply due to this.  

My hypothesis is this:  That at the higher tiers of the game (such as Futures and Challenger levels), left-handed players win matches over right-handed players in part due to their leftie advantage, and so they earn ranking points and their world ranking increases.  However, as they continue to advance, their skill level begins to become slightly lower than similarly ranked right-handed players.  So at the highest levels of the game, the lefties were able to get there by mostly skill, but also a little bit of left-handed advantage.  On the contrary, the right-handed players had to get to that point entirely on their skills.  This culminates in the top 500 or so players in the world, where the righties have the skill to back up their rankings, and the lefties commonly have slightly less skill, but have advanced that far in small part to their natural advantage.  So the righties are able to win a higher proportion of their matches overall, and also beat the lefties more often than not, because they did not have any advantage.  They are entirely the best players in the world.  
