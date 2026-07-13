import random

class TeamCultureProfile:
    """
    Represents the 'culture' an AI agent has learned or been configured with.
    This includes communication style, core values, and team-specific quirks.
    """
    def __init__(self, name, tone, values, common_phrases, humor_level="low"):
        self.name = name
        self.tone = tone  # e.g., "informal", "formal", "encouraging"
        self.values = values  # e.g., ["collaboration", "innovation", "customer_first"]
        self.common_phrases = common_phrases # e.g., {"greeting": "Hey team!", "closing": "Cheers!"}
        self.humor_level = humor_level # "low", "medium", "high"

class AIAgent:
    """
    A simple AI agent that adapts its responses based on a given TeamCultureProfile.
    """
    def __init__(self, name, culture_profile):
        self.name = name
        self.culture = culture_profile

    def _get_greeting(self):
        """Retrieves a culturally appropriate greeting based on the team's common phrases."""
        return self.culture.common_phrases.get("greeting", "Hello!")

    def _get_closing(self):
        """Retrieves a culturally appropriate closing based on the team's common phrases."""
        return self.culture.common_phrases.get("closing", "Regards.")

    def _add_cultural_flair(self, response_text, query_lower):
        """
        Injects cultural elements like tone, values, and humor into the response.
        This simulates the AI applying its 'learned' team culture.
        """
        flair_elements = []

        # Adapt tone based on culture profile
        if self.culture.tone == "encouraging":
            flair_elements.append("Keep up the great work!")
        elif self.culture.tone == "informal":
            flair_elements.append("Just saying!")

        # Inject team values if relevant to the query
        if "collaboration" in self.culture.values and ("team" in query_lower or "collaborate" in query_lower):
            flair_elements.append("Remember, teamwork makes the dream work!")
        elif "innovation" in self.culture.values and ("idea" in query_lower or "new" in query_lower):
            flair_elements.append("Let's innovate and push boundaries!")
        elif "customer_first" in self.culture.values and ("client" in query_lower or "customer" in query_lower):
            flair_elements.append("Always put the customer first!")
        # Randomly inject a value if no specific trigger, for broader demonstration
        elif random.random() < 0.2 and self.culture.values:
            flair_elements.append(f"Embracing our value of {random.choice(self.culture.values).replace('_', ' ')}!")

        # Add humor based on humor_level
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised."
        ]
        if self.culture.humor_level == "high":
            flair_elements.append(random.choice(jokes))
        elif self.culture.humor_level == "medium" and random.random() < 0.3:
            flair_elements.append(random.choice(jokes))

        if flair_elements:
            return response_text + " " + " ".join(flair_elements)
        return response_text

    def respond(self, query):
        """
        Generates a response to a query, integrating the agent's team culture profile.
        """
        query_lower = query.lower()
        response_core = ""

        # Basic query processing (simplified for demonstration)
        if "project status" in query_lower:
            response_core = "The project is progressing well, on track for the next milestone."
        elif "feedback" in query_lower:
            response_core = "Please share your thoughts in the #feedback channel. Your input is crucial!"
        elif "new idea" in query_lower or "brainstorm" in query_lower:
            response_core = "That's an exciting idea! Let's schedule a quick sync to discuss it further."
        elif "help" in query_lower:
            response_core = "I'm here to help! What specifically do you need assistance with?"
        else:
            response_core = "I'm not sure how to respond to that, but I'm always learning!"

        # Apply cultural elements: greeting, core response, cultural flair, closing
        final_response = f"{self._get_greeting()} {response_core}"
        final_response = self._add_cultural_flair(final_response, query_lower) # Inject cultural flair
        final_response += f" {self._get_closing()}"

        return final_response

# --- Main execution --- 
if __name__ == "__main__":
    # Define different team culture profiles.
    # These profiles represent the "culture" an AI agent has been taught or configured with.

    # Team Alpha: Informal, collaborative, innovative, with high humor.
    team_alpha_culture = TeamCultureProfile(
        name="Team Alpha",
        tone="informal",
        values=["collaboration", "innovation"],
        common_phrases={"greeting": "Hey team!", "closing": "Cheers!"},
        humor_level="high" # High humor level
    )

    # Team Beta: Formal, customer-focused, efficient, no humor.
    team_beta_culture = TeamCultureProfile(
        name="Team Beta",
        tone="formal",
        values=["customer_first", "efficiency"],
        common_phrases={"greeting": "Good morning/afternoon,", "closing": "Best regards,"},
        humor_level="low" # Low humor level
    )

    # Create AI agents, each assigned a specific culture profile.
    alpha_assistant = AIAgent(name="AlphaBot", culture_profile=team_alpha_culture)
    beta_assistant = AIAgent(name="BetaBot", culture_profile=team_beta_culture)

    print(f"--- {alpha_assistant.name} (Culture: {team_alpha_culture.name}) ---")
    # AlphaBot responds informally, might inject collaboration/innovation values, and humor.
    print(f"Query: What's the project status?")
    print(f"Response: {alpha_assistant.respond('What\'s the project status?')}\n")

    print(f"Query: I have a new idea for the feature.")
    print(f"Response: {alpha_assistant.respond('I have a new idea for the feature.')}\n") # Triggers 'innovation' value

    print(f"Query: How can we improve our collaboration?")
    print(f"Response: {alpha_assistant.respond('How can we improve our collaboration?')}\n") # Triggers 'collaboration' value

    print(f"--- {beta_assistant.name} (Culture: {team_beta_culture.name}) ---")
    # BetaBot responds formally, might inject customer_first/efficiency values, no humor.
    print(f"Query: What's the project status?")
    print(f"Response: {beta_assistant.respond('What\'s the project status?')}\n")

    print(f"Query: I have a new idea for the feature.")
    print(f"Response: {beta_assistant.respond('I have a new idea for the feature.')}\n")

    print(f"Query: We need to address a client issue.")
    print(f"Response: {beta_assistant.respond('We need to address a client issue.')}\n") # Triggers 'customer_first' value

    print(f"Query: Can you help me with a task?")
    print(f"Response: {beta_assistant.respond('Can you help me with a task?')}\n")