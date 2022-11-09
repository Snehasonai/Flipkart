Feature: order details flipkart
    Scenario Outline: order details
      Given we navigate to flipkart
      Then close the popup
      When click login
      Then we type "<username1>" field
      And we type in "<password1>" the field
      Then we click on the sign in button
      Then we over on profile
      And click on Orders
      Then click on On the way
      Then click on Delivered
      Then click on cancelled
      Then click on Returned
      Then click on Last 30 days
      Then click on 2022
      Then click on 2021
      Then click on 2020
      Then click on 2019
      Then click on older

      Examples:
        | username1 | password1 |
      | chiranjitc19@gmail.com | chiranjit123 |

