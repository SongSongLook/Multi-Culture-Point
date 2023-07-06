def get_model_identifier(model):
    model = model.lower()
    models = {
        "iphone 5s": "iPhone6,1 or iPhone6,2",
        "iphone se": "iPhone8,4",
        "iphone 6": "iPhone7,2",
        "iphone 6 plus": "iPhone7,1",
        "iphone 6s": "iPhone8,1",
        "iphone 6s plus": "iPhone8,2",
        "iphone 7": "iPhone9,1 or iPhone9,3",
        "iphone 7 plus": "iPhone9,2 or iPhone9,4",
        "iphone 8": "iPhone10,1 or iPhone10,4",
        "iphone 8 plus": "iPhone10,2 or iPhone10,5",
        "iphone x": "iPhone10,3 or iPhone10,6",
        "iphone xr": "iPhone11,8",
        "iphone xs": "iPhone11,2",
        "iphone xs max": "iPhone11,4 or iPhone11,6",
        "iphone 11": "iPhone12,1",
        "iphone 11 pro": "iPhone12,3",
        "iphone 11 pro max": "iPhone12,5",
        "iphone se (2nd generation)": "iPhone12,8",
        "iphone 12": "iPhone13,2",
        "iphone 12 mini": "iPhone13,1",
        "iphone 12 pro": "iPhone13,3",
        "iphone 12 pro max": "iPhone13,4",
        "iphone 13": "iPhone14,4",
        "iphone 13 mini": "iPhone14,5",
        "iphone 13 pro": "iPhone14,2",
        "iphone 13 pro max": "iPhone14,3"
    }

    if model in models:
        return models[model]
    else:
        return "Model identifier not found."
    
iphone_model = input("Enter the iPhone model: ")
model_identifier = get_model_identifier(iphone_model)
print(f"Model Identifier: {model_identifier}")
