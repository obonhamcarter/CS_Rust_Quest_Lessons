# College Fair Demo Track

This directory contains the **College Fair Demo Track** - 5 introductory quests designed to introduce prospective students to Computer Science before they dive into coding.

## Overview

The Demo Track addresses a critical gap: students need to understand **what Computer Science is** and **why they should study it** before jumping into Rust syntax.

## Quest Structure

### Quest 0: Welcome to CS (00-welcome-to-cs.qmd)
**Time:** 3 minutes  
**Purpose:** Explain what Computer Science actually is beyond just coding

**Content:**
- CS as problem solving, creativity, and innovation
- Real-world examples (Spotify algorithms, Google Maps, medical imaging)
- CS mindset and ways of thinking
- How CS combines with other fields

### Quest 1: CS in Daily Life (00-cs-daily-life.qmd)
**Time:** 2 minutes  
**Purpose:** Help students see Computer Science hidden in their everyday activities

**Content:**
- Hour-by-hour breakdown of a typical day
- CS behind smartphones, social media, streaming, navigation
- Invisible infrastructure (networks, databases, cloud)
- Recognition that CS is everywhere

### Quest 2: Why Study CS? (00-why-study-cs.qmd)
**Time:** 3 minutes  
**Purpose:** Present career opportunities and reasons to choose Allegheny

**Content:**
- Career statistics (median salary $100K+, 15% growth)
- Major vs Minor vs "just try a course" options
- How CS pairs with any other field (biology, art, business, etc.)
- Allegheny-specific advantages (small classes, hands-on, liberal arts)
- Real student pathways

### Quest 3: Try It Yourself (00-try-it-yourself.qmd)
**Time:** 5 minutes  
**Purpose:** Give students their first coding experience with instant success

**Content:**
- Simple "Hello World" program
- Personalize it with their name
- Do basic math (calculate graduation age)
- Make decisions with if/else
- Bonus creative challenges
- Uses Rust Playground (no installation needed)

### Quest 4: What's Next? (00-whats-next.qmd)
**Time:** 2 minutes  
**Purpose:** Provide clear action steps and maintain momentum

**Content:**
- Celebration of completing demo track
- Multiple pathways forward (continue quests, visit campus, talk to faculty)
- Action checklists (Today, This Week, This Month)
- Contact information and resources
- Frequently asked questions

## Total Time

**15-20 minutes** for complete demo track - perfect for college fair engagement!

## Design Principles

1. **Quest Theme Maintained:** All slides use the same role-playing game metaphor as the coding quests
2. **Visual and Engaging:** Heavy use of emojis, cards, highlight boxes
3. **No Prerequisites:** Zero CS or programming knowledge assumed
4. **Action-Oriented:** Every quest has clear takeaways and next steps
5. **Mobile-Friendly:** Designed to work on phones at the fair
6. **Progressive Disclosure:** Start broad (what is CS) → narrow (try coding) → actionable (next steps)

## Integration with Existing Site

The Demo Track is prominently featured:
- Listed first on the home page
- Separate section in navigation sidebar
- Own landing page (college-fair.qmd) optimized for QR codes
- Clear differentiation from the 19 coding quests

## Usage at College Fair

**Recommended Approaches:**

1. **QR Code Method:** Display QR code pointing to `college-fair.qmd` at booth
2. **Guided Demo:** Professor/student walks prospects through Quest 3 (Try It Yourself)
3. **Self-Guided:** Students complete all 5 quests on their own devices (15 min)
4. **Teaser:** Show Quest 0 on a large screen to attract attention

**Success Metrics:**
- Student completes all 5 demo quests
- Student bookmarks the site
- Student schedules a campus visit
- Student emails CS department with questions
- Student attempts coding Quests 1-5 after the fair

## Technical Notes

All quest files are:
- Written in Quarto QMD format
- Use `live-html` format for interactivity
- Include quest badges, cards, and consistent styling
- Link to Rust Playground for coding exercises (no local setup required)
- Optimized for both desktop and mobile viewing

## Maintenance

When updating demo quests:
1. Maintain consistent quest theme and styling
2. Keep time estimates realistic (under 5 min per quest)
3. Update career statistics annually (salary data, job growth)
4. Refresh real-world examples to stay current
5. Update Allegheny-specific content (programs, events, contact info)

## Future Enhancements

Potential additions:
- Video testimonials from current students
- Interactive CS concept demos (sorting visualization, pathfinding)
- Virtual lab tour
- Live Q&A scheduling
- Gamification (badges for completing all quests)
- Analytics to track which quests are most engaging
