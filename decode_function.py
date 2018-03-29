def decode_function(encode, max, min, Bit):
    decode = []

    for i in encode:
        tmp = []
        for j in i:
            s = 0
            L = len(j)-1
            for k in j:
                s = s + k*(2**L)
                L = L-1
            tmp.append(s)
        for j in range(len(tmp)):
            tmp[j] = tmp[j]*(max[j]-min[j])/(2**(Bit[j])-1)+min[j]
        decode.append(tmp)
    return decode