# coding=utf-8
"""
VARIABLE DESCRIPTIONS:
survival        Survival
                (0 = No; 1 = Yes)
pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)

SPECIAL NOTES:
Pclass is a proxy for socio-economic status (SES)
                (1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower)

Age is in Years; Fractional if Age less than One (1)
                If the Age is Estimated, it is in the form xx.5

With respect to the family relation variables (i.e. sibsp and parch)
some relations were ignored.  The following are the definitions used
for sibsp and parch.

Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
Parent:   Mother or Father of Passenger Aboard Titanic
Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic

Other family relatives excluded from this study include cousins,
nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
only with a nanny, therefore parch=0 for them.  As well, some
travelled with very close friends or neighbors in a village, however,
the definitions do not support such relations.

(https://www.kaggle.com/c/titanic/data)
"""



"""
Describe the data.
> How big?
> What are the columns and what do they mean?
"""



"""
What’s the average age of...
> any Titanic passenger
> a survivor
> a non-surviving first-class passenger
> Male survivors older than 30 from anywhere but Queenstown
> For the groups you chose, how far (in years) are the average ages from the median ages?
"""

"""
What’s the most common...
> passenger class
> port of Embarkation
> number of siblings or spouses aboard for survivors
"""


"""
Within what range of standard deviations from the mean (0-1, 1-2, 2-3) is the median ticket price?
Is it above or below the mean?
"""



"""
How much more expensive was the 90th percentile ticket than the 5th percentile ticket? Are they the same class?
> The highest average ticket price was paid by passengers from which port? Null ports don’t count
"""



"""
Which port has passengers from the most similar passenger class?
What fraction of surviving 1st-class males paid lower than the overall median ticket price?
How much older/younger was the average surviving passenger with family members than the average non-surviving passenger without them?
Display the relationship (i.e. make a plot) between survival rate and the quantile of the ticket price for 20 integer quantiles. Make sure you label your axes.
"""


"""
*STRETCH GOAL* For each of the following characteristics, find the median in the data.
age
ticket price
# siblings/spouses
# parents/children
If you were to use these medians to draw numerical boundaries separating survivors from non-survivors, which of these characteristics would be the best choice and why?
"""