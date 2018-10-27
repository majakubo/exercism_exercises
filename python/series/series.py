def slices(series, length):
    if length > len(series):
        raise ValueError("length too large")
    if length <= 0:
        raise ValueError("length too small")

    return [series[i:i+length] for i in range(0, len(series) - length + 1)]

