TEST_CASES_PROMPT = '''
You will be given an image containing User Interface for a mobile app. 
The things that you need to consider in the image is given by using triple backticks as the delimiter and the information is presented in markdown format.
Perform the following tasks:
1. Figure out the requirements of the project
2. List out the requirements of the project but do not produce and output
3. For each requirement produce a verbose list of usecases but do not output anything
4. For each usecase design a test case using go language.
5. Produce the list of requirements represented by the project and output in markdown format.
6. Present all the list cases with each test case in it's own code block

```
1. **Layout and Structure:**
   - Overall arrangement of elements like navigation bars, sidebars, and content sections.
   
2. **Navigation:**
   - Types of navigation used (e.g., menus, tabs, breadcrumbs) and their hierarchy.
   
3. **Typography:**
   - Font styles, sizes, and hierarchy used for headings, paragraphs, and buttons.
   
4. **Color Scheme:**
   - Primary and accent colors used across the interface, including backgrounds and text colors.
   
5. **Interactive Elements:**
   - Types of interactive elements (e.g., buttons, links, forms) and their behaviors.
   
6. **Images and Icons:**
   - Usage of images, icons, or illustrations to support content or indicate actions.
   
7. **Responsive Design:**
   - How the UI adapts to different screen sizes (e.g., desktop, tablet, mobile).
   
8. **Forms and Input Fields:**
   - Types of input fields used (e.g., text fields, dropdowns, checkboxes) and their validations.
   
9. **Error Handling:**
   - How errors or validation messages are displayed and handled within the UI.
   
10. **Accessibility Features:**
    - Considerations for accessibility such as alt text for images and keyboard navigation.
    
11. **Loading Indicators:**
    - How the UI communicates loading states or delays to the user.
    
12. **Animations and Transitions:**
    - Use of animations or transitions for visual feedback and interaction.
    
13. **Modal Windows or Pop-ups:**
    - Usage of modal windows or pop-ups for additional information or actions.
    
14. **Social Media Integration:**
    - Integration of social media buttons or feeds within the UI.
    
15. **Media Players or Embeds:**
    - Usage of media players (e.g., video, audio) or embeds like maps or calendars.
    
16. **Localization Features:**
    - Considerations for supporting multiple languages or regions.
    
17. **Feedback Mechanisms:**
    - Methods for users to provide feedback or contact support.
    
18. **User Preferences:**
    - Options for users to customize settings or preferences within the UI.
    
19. **Security Features:**
    - Indicators of secure connections (e.g., HTTPS) and authentication methods.
    
20. **Analytics and Tracking:**
    - Integration of analytics tools to track user interactions and behaviors.

```
'''