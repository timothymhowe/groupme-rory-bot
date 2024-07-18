from random import randint
from datetime import datetime


def get_random_rory_fact_payload(GROUPME_BOT_ID):
    
    rory_fact = get_random_rory_fact()
    
    payload={
        "bot_id"  : GROUPME_BOT_ID,
        "text": rory_fact
            } 
    
    return payload

# rory fact case switch.  this is hardcoded, less than ideal, but workable I suppose
def get_random_rory_fact():
    
    # Define the target date
    last_missed_3_footer_date = datetime(2024, 6, 16)
    last_major_date = datetime(2014, 8, 10)
    current_date = datetime.now()

    # Calculate the difference in days
    days_since_missed_putt = (current_date - last_missed_3_footer_date).days
    days_since_last_major = (current_date - last_major_date)
    facts = [
        "Rory McIlroy famously blew a four-shot lead during the final round of the 2011 Masters, finishing tied for 15th.",
        f"It has been {days_since_last_major} day(s) since Rory McIlroy has won a major.",
        f"It has been {days_since_missed_putt} day(s) since Rory McIlroy missed a 3 foot putt in a major.",
        "Rory has missed 2 cuts at The Masters in the last 4 years.",
        "Rory McIlroy withdrew from the 2013 Honda Classic mid-round citing severe tooth pain, an excuse media and fans alike knew was bullshit.",
        "In 2015, McIlroy suffered an ankle injury while playing soccer, causing him to miss the Open Championship.",
        "His 2016 season was affected by a rib injury that hampered his performance and led to several missed tournaments.",
        "McIlroy faced criticism for his decision to skip the 2016 Olympics in Rio de Janeiro, citing concerns over the Zika virus.",
        "Rory McIlroy famously missed the cut at the 2019 Open Championship at Royal Portrush, less than an hour from his childhood home.",
        "McIlroy failed to win any tournaments in 2020, breaking a streak of winning at least one event per year for over a decade.",
        "Despite his talent, McIlroy has struggled with consistency in putting, which has been a recurring weakness in his game.",
        "In 2012, McIlroy was penalized for slow play during the European Tour's Abu Dhabi HSBC Golf Championship.",
        "McIlroy's ex-fiancee and former World No. 1 in Tennis, Caroline Wozniacki, won a Grand Slam as recently as 2018",
      
        'In the 125th Open Championship, Rory McIlroy failed to hole a putt longer 4\'9" in the final round.  In the final round of the 2024 US Open, he failed twice to make putts shorter than 4". Brutal.',
        "McIlroy fired the caddy he won 4 majors with because he had the audacity to question Rory's lack of focus and preparation after bogeying 5 of the first 6 holes in the first round of the 2017 Open Championship at Birkdale.",
        'Rory McIlroy is one of the Tour\'s longest drivers, despite standing at just 5\'4" tall.'
    ]

    return facts[randint(0,len(facts)-1)]


