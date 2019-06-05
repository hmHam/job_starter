def disp_model_data(data):
    return {field.name: getattr(data, field.name) for field in data._meta.fields}