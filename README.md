# WWC_Hackathon
Women Who code hackathon project for Social Good

Problem Statement:
There’s a societal issue regarding a lack of empathy and regard for women coming out of prison. As a result, these women are under-served, and suffer from a lack of resources, furthering the challenge to get their lives back on track.  Women who are released from prison in Ontario, Canada often have no belongings upon their release. Their number one priorities are food, shelter, and reconnection with family.  Once these needs are resolved their secondary needs are supplies: furniture, household items, clothes, etc..  This supply issue can be addressed by technology.

Solution:
The goal: 
Address the supply issue by increasing the number of physical donations provided to the non-profit, The Second Chance Foundation, in Scarborough, Ontario, Canada.  The foundation helps to provide necessities to women recently released from prison.  This goal will be met by web scraping platforms where people living in or near Scarborough are offering needed goods for free or at a low price (e.g., Kijiji, Facebook Marketplace).  The user will be emailed to ask them to consider donating their offered goods to The Second Chance Foundation instead. 

Kojojo Donations is a static website that mimics kijiji.com. We created a web scraper that searches posted items that are needed by The Second Chance Foundation. Our localhost website is web scraped (instead of kijiji).
The code is set up to email the person who posted and they are asked to consider donating the item to The Second Chance.

We focus on contacting people that meet the following criteria:
They live within specific postal codes (i.e., local to The Second Chance)
They advertised their item for below $50 
The item is needed by The Second Chance

We used Django framework to create our localhost website (Kojojo Donations) and created a postgres database on AWS Lightsail loaded with kijiji data that was downloaded from ParseHub.com. 

Notes:
The team wanted to focus on helping underprivileged women as our social good. We interviewed Beverly Dwyer, founder of The Second Chance Foundation, to understand the organization’s needs and to determine which needs can be addressed with technology.

The team discussed a few platforms to search for items (Kijiji, Craigslist, and Facebook Marketplace) but decided that we needed more time to research the legalities
and to review the terms and conditions for each platform.  As a workaround we created a localhost website that has real data from kijiji (that was download from ParseHub.com) 

We created a localhost website to web scrape because we weren’t sure which platform would be the best for the actual solution. 
As a proof of concept, we focused on posts that were within 10 km of The Second Chance Foundation, and searched for furniture items. ParseHub's Kijiji DataScrape
