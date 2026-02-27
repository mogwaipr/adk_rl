import vertexai
from vertexai.generative_models import GenerativeModel

# 2. Try the 2026 stable versions
# Note: 'gemini-1.5-flash-001' is older. Try the stable 'gemini-1.5-flash' 
# or the newer 'gemini-2.0-flash-001' which we saw in your garden list.
test_models = ["gemini-1.5-flash", "gemini-2.0-flash-001"]

for model_name in test_models:
    try:
        print(f"Attempting {model_name}...")
        model = GenerativeModel(model_name)
        response = model.generate_content("Hello! Are you active?")
        print(f"✅ Success with {model_name}: {response.text}")
        break 
    except Exception as e:
        print(f"❌ Failed with {model_name}: {e}")