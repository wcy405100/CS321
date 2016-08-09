# CS321 Extra Homework
# Name: Chenyu Wang

import fileinput # for input outside file

#remove whitespace in list
def removews(a):
    f = ''
    for e in a:
       if e != ' ':
            f += e
    return f
# this function will help find the key of input value if match
# for ambiguous language we can return all keys in dictionary
def find_key(input_dict, value):
    c = []
    for a in input_dict.items():
        for b in a[1]:
            if value != b:
                continue
            else:
                c.append(a[0])
    return c
# using DP in CKY algorithm
# Return true or false and all parse tree
def cky_alg(input_dict,string, rstring, output):
    DP_m = []   #store the string list
    tree = []   #store the parse tree
    count = 0   #count for parse tree occurance
    disp = []
    for subs_len in range(1,len(string)+1):
        DP_m.append([]) # the first dimension is according to  substring length
        tree.append([])
        for s_index in range(len(string)-subs_len+1):
            DP_m[subs_len-1].append([]) # the second dimension is according to starting index inside the whole string
            tree[subs_len-1].append([])
            subs = string[s_index:(s_index+subs_len)]
            if subs_len == 1:           # this is storing the base case of DP into DP_m[0][starting index], such as A -> a
                output = find_key(input_dict,subs)
                DP_m[subs_len-1][s_index].append(output)
                tree[subs_len-1][s_index].append([])
                for str0 in output:
                    temp = ' (' + str0 + ' ' + subs + ')'
                    tree[subs_len-1][s_index][0].append(temp)
                continue
            for split_p in range(len(subs)):
                DP_m[subs_len-1][s_index].append([])
                tree[subs_len-1][s_index].append([])
                subs_a = subs[:split_p] # left substring
                subs_b = subs[split_p:] # right substring
                if subs_a: # we don't account subs_a == 0 because
                   for ind_c, ke1 in enumerate(DP_m[len(subs_a)-1][s_index]): # searching all the possible cut of k on substring a
                        for ind_d,ke2 in enumerate(DP_m[len(subs_b)-1][split_p+s_index]): # searching all the possible cut of k on substring b
                            if ke1 and ke2:
                                for ind_e,m in enumerate(ke1):
                                    for ind_f,n in enumerate(ke2):
                                        for ele in find_key(input_dict,m+n): # this is only one possible result for a certain split_p
                                            if ele:
                                                for unit in ele:
                                                    DP_m[subs_len-1][s_index][split_p].append(unit)
                                                    str1 = ' (' + unit+tree[len(subs_a)-1][s_index][ind_c][ind_e]+tree[len(subs_b)-1][split_p+s_index][ind_d][ind_f]+')'
                                                    tree[subs_len-1][s_index][split_p].append(str1)
    for resu in tree[len(string)-1][0]:
        for resul in resu:
            if resul:
                count += 1
                if count < 3:
                   disp.append(resul)
    result = rstring +' : '+ str(count) +' parse trees.'
    print result
    f.write(result+'\n')
    if count !=0:
        print disp[0]
        f.write(disp[0]+'\n')
    if count > 1 :
        print disp[1]
        f.write(disp[1]+'\n')

k = [] ; b =[] ; string = [] ; rstring =[]
test = fileinput.input()
#read files from input files
for ind, line in enumerate(test):
    temp = []
    line = line.rstrip()
    if line:
        list1 = line.split('->')
        k.append(removews(list1[0]))    # Make Key value list
        tmp = list1[1].split('|')
        for i in tmp:
            f = removews(i)
            temp += [f]
        b.append(temp)
    else:
        boundary = ind      # find the blank line index
        break
# Build dictionary for regular expression rules
dic = dict((k[j],b[j]) for j in range(len(k))) # combine keys and bodies into dictionary
for stri in test:
    stri = stri.rstrip()
    test = removews(stri)
    rstring.append(stri)
    string.append(test)
f = open("Chenyu_wang_cfg.out","w")
f.write('================================\n')
print '================================'
for n,inputs in enumerate(string):
    cky_alg(dic, inputs , rstring[n],f)
    f.write('\n')
    print ''
print '================================'
f.write('================================')
f.close()




