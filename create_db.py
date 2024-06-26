#Create mongita database with article information
import json
from mongita import MongitaClientDisk

#This one is for dates
from datetime import datetime
# Function to convert date string to datetime object
def convert_date(date_str):
    # Assuming the date format is 'month/day/year'
    month, day, year = map(int, date_str.split('/'))
    return datetime(year, month, day)


#Put future articles in this array then just index it in the actual db so it doesn't clutter it up
article = ["""
School of Fashion students are collaborating with fitness guru Jaime Brenkus to compete for their t-shirt design to be featured on his show.

Brenkus rose to popularity in the 1990s after he created the program “8-Minute Abs.” Since then, Brenkus has helped millions of people meet their fitness goals.

Over the last two years, Brenkus and associate fashion professor Vince Quevedo have created a program that will help prepare students for the real world.

“I think the biggest thing is knowing that basically putting the students in an arrangement gives them a platform for the students to achieve,” Brenkus said. “We call it a real life experience with a national brand.”

Quevedo’s students each make a t-shirt design suited to Brenkus. Once the competition is over, Brenkus chooses a design to wear on his PBS program. Not only does this allow students a chance to design their own piece of fitness apparel, but also the chance to be featured on a major platform.

With nearly 1,500 students in fashion design and fashion merchandising, the collaboration has many benefits. For fashion students, this opportunity is preparing them for their future even while they are still in school.

With fitness at the forefront of the assignment, Brenkus explained his steps to start a fitness journey.

“I think you have to look at and see what your goals and objectives are, whether it’s to basically lose weight or whether it’s to shape your life. You have to go back to tried and true strategies,” he said.

The collaboration between Kent State students and Brenkus has offered a good experience for both parties.

“Students themselves exemplified the type of curriculum that Kent State has, because they’re very bright and talented,” Brenkus said. “When everybody created shirts for us, I gotta tell you, I could have probably used every single one of them.”
""",
"""
On the night of a formal dance at their high school, Aiden Zapisek, who identifies as non-binary and gay, entered a stall in the men’s bathroom. Soon after, a group of boys walked in and surrounded the stall door.

With their heart pounding, Zapisek froze as the boys banged on the door while yelling, moaning and throwing things into the stall.

“It was definitely hard to come around after that happened,” Zapisek said. “I’m okay with it now. It sucks that it happened, but screw them.”

Now a freshman digital media production major, Zapisek said they hope to be a voice for non-binary, trans and gender-nonconforming people who don’t feel safe using public restrooms.

When they first heard about House Bill 183, Ohio’s latest bill that would require K-12 and college students to use bathrooms and locker rooms that align with their sex assigned at birth, all they could think about were students who have had similar experiences while trying to use the bathroom.

“As somebody who is non-binary and does use a male restroom, I’m not extremely comfortable with it,” Zapisek said. “I’ve had men bang on doors and be like, ‘Hey, what are you doing in there?’ and just yell and be loud, and it’s very uncomfortable. So, I understand if somebody feels comfortable in one bathroom over the other, or if they identify as female and want to go in a female bathroom, they should be able to do that and vice versa.”

The House Higher Education Committee approved the bill, which would also ban schools from letting students share overnight accommodations with the opposite biological sex, on April 10.

Ohio House Reps. Beth Lear and Adam Bird, who introduced H.B. 183 last May, did not respond to KentWired’s request for comment.

The bill comes amid a nationwide push to restrict transgender people’s access to public restrooms, locker rooms and other facilities. Similar bills have passed in states such as Utah and have been introduced in Idaho, Georgia, Arizona, New Mexico, Iowa and West Virginia.

Zapisek said one of their trans friends, who lives on campus, said there was a debate over whether they were allowed to use the bathroom on their “female-only” floor because they identify as a trans man.

“They ended up being able to use the bathroom, but it was a serious dilemma and situation,” Zapisek said.

For Lauren Vachon, an assistant professor and coordinator of the LGBTQ Studies program, the bathroom debate hits close to home.

Vachon’s trans son, Jeremy, came out in high school and wanted to feel comfortable using the school bathrooms. When Vachon and their son walked into a meeting with the school district to discuss accommodations, they were surprised by the school’s willingness to accommodate.

The school offered him to use a separate restroom, which made him the most comfortable. While Vachon believed it was a better option, they didn’t feel it was truly equal.

“I felt that ‘use this special bathroom’ was not true, equal access, right?” Vachon said. “I agreed that it was probably best for Jeremy, and he also agreed, but my feelings about it were complicated. Really, I had gone into that meeting with school administrators ready to do battle — but I didn’t have to.”

Vachon has been a professor at Kent State since 2016, and they said they’ve heard from many queer and trans students who are concerned for their safety as H.B. 183 advances.

“The kind of policing of bathrooms that this bill will engender will make it dangerous for these students to use public restrooms on campus,” Vachon said.

However, Bird told the Ohio Capital Journal that H.B. 183 will give Ohioans protections in restrooms.

“Me and my Republican colleagues have heard from constituents all across the state,” Bird said. “They may not have been loud. They may not have been vocal. They may not have come with a sign to the Statehouse, but we are here representing the vast majority of Ohioans who want protections.”

Vachon said they don’t believe the bill will solve Ohioans’ problems, and they said Republican members of the Statehouse are engaging in “performative politics.” They said members are catering to conservative organizations, such as the Alliance Defending Freedom and the Heritage Foundation, which they said are the machines behind this type of legislation.

“That produces this alignment where all the Republicans in state houses in Ohio and other states feel compelled to introduce these bills that are sometimes almost identical in their wording because they’ve been written by these national groups,” Vachon said.

One aspect of the bill that Vachon is especially concerned about is its vague enforcement mechanism, which heavily relies on an individual’s biological sex listed on their birth certificate. The bill defines biological sex as “the biological indication of male and female, including sex chromosomes, naturally occurring sex hormones, gonads and nonambiguous internal and external genitalia present at birth, without regard to an individual’s psychological, chosen or subjective experience of gender.”

Vachon said that even if queer and transgender students have had their gender markers on their birth certificate changed, it won’t be enough.

“What’s going to happen to a trans man who has a full beard who’s [going to] have to use the women’s room?” Vachon said. “There’s the other scenario of trans women having to use the men’s room, and that is incredibly unsafe for trans women.”

Research has found that transgender women experience assault about four times higher than cisgender women. The human rights organization GLSEN found in a 2021 Ohio report on the experiences of LGBTQ+ middle and high school students that 42% of trans and non-binary students were stopped from using the bathroom that aligned with their gender, and 36% couldn’t use the locker room aligning with their gender.

If H.B. 183 passes, Vachon said non-binary and trans students should seek out safe bathrooms for themselves, and they said the LGBTQ+ Center maintains a list of where all the universal restrooms are located on campus.

“My advice is for people to seek out safe bathrooms for themselves,” Vachon said. “Kent State is installing quite a few restrooms that will be key if this bill were to become law — the ones that have a single toilet and a sink behind a locked door. Under this bill, those would still be allowed to be considered universal restrooms if they’re like that style.”

Erica Pelz, a faculty member and sophomore sociology student, said the bill is a direct attack on all women. Pelz spoke outside of their role with the university.

“I’m very worried about both trans students and cisgender students who are going to be challenged by people with nefarious intentions who are just trying to go pee,” Pelz said. “‘Prove to me that you should be in the women’s restroom. Prove that you’re really a woman,’ you know?”

As a trans woman, Pelz said LGBTQ+ people and allies should assess their risk before speaking out against H.B. 183 and similar bills.

“If you can tolerate that risk, start calling representatives, start writing letters and be heard,” Pelz said. “When you hear somebody say something that is blatantly untrue about trans folks and bathrooms, correct them and explain why it matters.”
""",
"""
The Kent State of Well-Being encouraged students to take steps toward positive environmental impacts during its meeting Wednesday.

The event involved students making their own eco-friendly reusable bags and learning about sustainable ways to dispose of plastic wrappers via ecobricks.

Ecobricks are simple ways to limit the greenhouse gasses that get sent into the atmosphere after plastic sits in the sun. All you need is a dry plastic bottle, dry plastic and a stick for packing to begin creating your own.

Using old recreation center T-shirts, participants were able to tie knots to create a sustainable bag that can be used for class, markets or grocery shopping.

Evan Coates, a junior public health major, said he wanted this event to not only be informative, but also be interactive. He used the ecobrick as an educational factor and the bags as an eye-catcher.

“We had leftover shirts that we were gonna get rid of so I just thought, well, let’s show students what they can turn these into,” Coates said.

Plastic pollution is becoming more of an issue as time goes on. Reusable bags are one of many ways people can limit waste and reduce their footprint.

In addition to plastic waste, reusable bags hold more items than the average grocery store bag. Therefore, the trips you take and the waste you create are all minimized.

Reusable bags in general can be stronger and more durable. Heavy items while grocery shopping, such as milk or soda, typically need to be outside of the plastic bag due to fear of breakage. Reusable bags made of thick and layered material leave you stress-free while carrying in your groceries.

While ecobricks weren’t actively being made at the event, Coates was there to explain more about how to create one, how it’s beneficial, and the impact it could make if everyone takes part in it.

“We wanted to get involved with the community, and I felt like this would spread education about environmental topics,” he said.

The Kent State of Well-Being is located to the right of the campus recreation center entrance. Employees here are referred to as “peer educators,” and work to encourage balance in students’ lives.

Brynn Kler, a sophomore exercise science major and employee for the Kent State of Well-Being, said that wellness is all-encompassing and they try to educate students about that.

The center uses the eight dimensions of wellness when planning events and resources. The eight dimensions are the following: social, emotional, spiritual, intellectual, physical, environmental, financial and occupational.

“We preach a lot about how our wellness is all individual,” Kler said. “You know, my wellness may not look the same as yours, and that is completely normal.”

With wellness and sustainability tied together at this event, students got an educational and hands-on event promoting environmental well-being.

For connection to more resources, visit the Kent State of Well-Being center.
""",
"""
Researchers from the university teamed up with other universities to form the Ohio/Pennsylvania University Research Consortium, which works to summarize the effects of the East Palestine train derailment.

Beyond Kent State, the consortium is made up of around two dozen researchers from seven universities and was organized by researchers from Case Western Reserve University, The Ohio State University and University of Pittsburgh.

Jeffrey Hallam, a university professor in the College of Public Health and director of the Healthy Communities Research Institute, is the liaison between Kent State and the Research Consortium.

Hallam said the universities wished to participate in this research opportunity because of the proximity of the derailment, but researchers further away were also interested in exploring the data.

“The Research Consortium was put together primarily because this happened right there in East Palestine, and there was a flood of people from Ohio and Pennsylvania that wanted to go in there and do research,” Hallam said. “The folks that live there were inundated with people and researchers, lots of people running around while they’re still trying to deal with the cleanup and everything else.”

Hallam said the consortium came together to provide an independent voice of the data that was already being collected and present it to the public.

Members of the consortium have a variety of academic backgrounds and research experience and use pre-obtained data from various sources, such as other researchers and response agencies.

The goal of the consortium is to present the findings in a manner that is more understandable for those affected and to make recommendations for community members, Hallam said.

The data presented by members of the Research Consortium is publicly available, but the university has its own researchers who are currently collecting data separately from the consortium.

“It was all publicly available data that was then presented back to the public, but we do have Kent State researchers that are collecting data and have been since the derailment,” Hallam said.

The Kent State researchers collecting their own data have not yet presented their findings, as the research is ongoing.

Sandra Morgan, strategic partnership and outreach director for the College of Arts and Sciences, looks for opportunities on behalf of the college, which prompted her to look for research for the derailment.

“Out of this tragedy at East Palestine, I saw an opportunity for our faculty members to participate, do some research and get in the mix,” Morgan said.

Other universities were attempting to initially help with conducting research in the city, but Morgan said they were not necessarily helping for the right reasons, and this caused Kent State researchers to take a while building trust and becoming part of the consortium.

Morgan said the research opportunities presented were great, but what inspired her and other members of the university to partake in it was the closeness with which the derailment happened.

“We wanted to know what was happening, certainly, in the area, and especially since we have a couple of campuses that are right in the area, Salem and East Liverpool, we wanted to be a part of the solution,” Morgan said.

Morgan said the researchers are working through all of the data presented to them, including samples from soil, water, air and plant life.

The consortium held a state of the science update in East Palestine on April 10, which focused mainly on the data surrounding air. The next update, which will occur at an undecided future date, will focus on soil and water data.

The state of the science update was open to the public, and residents or anyone else interested in the effects was encouraged to attend.

“To be able to interpret the information in a way that people understood, and for them to be able to ask questions to people who are experts in their respective fields, was also very helpful,” Morgan said. “To not just have the government answer to everything, but to have people for whom this is their life’s work be able to answer.”
""",
"""
So, it’s the end of the second semester. At least, it is by the time this is released. As I write this, it’s late at night after putting it off all week. This has been the same situation with all of my assignments for at least the last month. This can be narrowed down to a simple term known as burnout.

I’m sure that if you clicked on this article, you’re probably in the late stages of academic burnout, too. Trust me, you’re not alone. It’s an epidemic that plagues college students everywhere at least once a year. 

The official dictionary definition of burnout is: “feeling empty and mentally exhausted, devoid of motivation and beyond caring.” I personally concur with this. I’m at the stage of the semester where I kind of just don’t care. I’m tired all the time and have no motivation to do anything, but I still manage to barely pick myself up and get done what I have to so I don’t flunk out a class, or a few for that matter. 

It’s the same process every time. I get a new assignment, I leave class, I take a nap, I avoid doing said assignment until the last minute, I go to bed, repeat. The same damn process over and over and over. It’s even worse when you’re a diagnosed depression and anxiety-ridden freshman like me. 

One minute you can range from feeling motivated to do an assignment, but wait too long and you’ll want to stay as far away from it as possible. At the end of the week, though, you somehow make it. You somehow manage to do what your head is telling you is impossible.

You live to see another day. 

Well, I’m here to tell you that you can do it! Hell, I mean I’m here writing this after barely surviving through another week, yet, I persevered. The next time that the burnout is just too real, don’t force yourself to do it, because I have some advice for you! 

Based on my observations of an article from choosingtherapy.com, I found a few therapist-recommended tips to help you through this burnout. 

    Just breathe. Deep breaths tell your brain to relax when stressed. Your mind may still be racing, but at least your body understands you are not in immediate danger. Try counting your inhales and exhales or putting your hand on your stomach to notice the rise and fall as you breathe. 
    Use daily relaxation reminders. Establishing relaxation reminders throughout your day is a great way to stay consistent with managing your stress proactively. Set a reminder on your phone or work calendar to step away for a rest break. Take a deep breath, roll your shoulders and tell yourself, “I am calm.” With regular practice, your body becomes more and more efficient at returning to a state of balance.  
    Get realistic with time management. While preventing burnout may not always be possible, improving your time management can help you feel less overwhelmed. Start by establishing your priorities each day. You can then create a schedule and break large tasks into more manageable steps.
    Focus on what you can control. Feeling bogged down by the things you can’t change is easy. However, you may feel more empowered when focused on what you can change (your reactions, mindset and behaviors). This step can promote a sense of confidence and offset or reduce the effect of burnout.   
    Get enough sleep. Consider how much energy you actually have each day when determining how to overcome burnout. Sleep hygiene is especially critical. Ensure you get plenty of sleep (adults typically need seven to nine hours) in a dark, cool and comfortable environment. 
    Prioritize self care. Self-care can help you manage burnout by strengthening your physical and emotional well-being. Self-care comes in many forms, but the overarching goal is to meet your needs kindly and compassionately. Schedule regular, daily self-care. Just a few minutes can make a significant difference.
    Take frequent breaks throughout the day. Even small breaks can help you restore your energy levels each day. Plan times to eat meals, drink coffee or even socialize with colleagues during work. Try a time management method where you work for a designated chunk before taking a planned break. In addition to helping you feel better emotionally, doing so can boost productivity.
    Ask for help. Sometimes, reducing burnout comes down to knowing how and when to ask for help. Independence has virtues, but reminding yourself that everyone needs support at some point is crucial. Furthermore, many people want to help, so consider requesting assistance with specific tasks or projects from trusted loved ones.

I hope you take this advice into consideration. I really just hope you take care of yourself in general. The year is almost over and then it’s summertime.

Let’s handle this as a team and make our homework cry in desperation instead of us. You can do this! This is just a short time in your life. It will get better. So, go out there and kick some butt. 
"""
]
#Put future articles in here the way it is formatted
print(article)
publish_data = [
    {"pop":"1","author":"Lauren Vaughn", "title":"School of Fashion collaborates with ’90s fitness guru for t-shirt design contest", "text":article[0], "date_created":convert_date("4/28/24"), "date_string":"4/28/24"},
    {"pop":"2","author":"Aden Graves", "title":"Inside House Bill 183: Ohio’s latest bathroom bill", "text":article[1], "date_created":convert_date("4/28/24"), "date_string":"4/28/24"},
    {"pop":"5","author":"Morgan Hoover", "title":"Kent State of Well-Being supports Earth Month with Wednesday event", "text":article[2], "date_created":convert_date("4/25/24"), "date_string":"4/25/24"},
    {"pop":"3","author":"Kayla Gleason", "title":"University researchers analyze, present effects of East Palestine train derailment", "text":article[3], "date_created":convert_date("4/25/24"), "date_string":"4/25/24"},
    {"pop":"1","author":"Nick Keller", "title":"OPINION: The burnout is real", "text":article[4], "date_created":convert_date("4/23/24"), "date_string":"4/23/24"},
]

#Create a mongita client connection
client = MongitaClientDisk()

#Create article database
articles_db = client.articles_db

#Create articles collections
article_collection = articles_db.article_collection

#empty the collection
article_collection.delete_many({})

#Put the quotes in the database
article_collection.insert_many(publish_data)

#Check if articles are there
print(article_collection.count_documents({}))
