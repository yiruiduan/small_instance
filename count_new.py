#Author:yiruidaun
#简单计算机，可以根据输入的简单算式进行计算并求出结果
import re
def count_zhengshu(instance):
    '''传入公式的第一个数字输正数的进行运算'''
    if re.search("\*", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) * float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\/", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) / float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\+", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) + float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\-", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) - float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    else:
        print("输入有误！！！！！")

def count_fushu(instance):
    """传入的公式第一位数字是负数进行运算"""
    if re.search("\*", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) * float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\/", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) / float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\+", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) - float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    elif re.search("\-", instance):
        number = float(re.split("[\*|\-|\+|\/]", instance)[0]) + float(re.split("[\*|\-|\+|\/]", instance)[1])
        return number
    else:
        print("输入有误！！！！！")

def get_formula2(bracket):
    """复合运算有加减有乘除"""
    while True:
        if re.search("[0-9]+\.?[0-9]*[\+|\-|\*|\/][0-9]+\.?[0-9]*",bracket):
            if re.search("[0-9]+\.?[0-9]*[\+|\-][0-9]+\.?[0-9]*[\*|\/][0-9]+\.?[0-9]*", bracket):
                formula_list = re.split("[\+|\-|\(|\)]", bracket)
                print(formula_list)
                for formula_mul in formula_list:
                    if re.search("[\*|\/]", formula_mul):
                        result = get_formula1(formula_mul)
                        formula_mul = re.sub("\*", "\*", formula_mul)
                        formula_mul = re.sub("\/", "\/", formula_mul)
                        formula_mul = re.sub("\+", "\+", formula_mul)
                        formula_mul = re.sub("\-", "\-", formula_mul)
                        print(formula_mul)
                        bracket=re.sub(formula_mul,result,bracket)
            else:
                bracket=get_formula1(bracket)
        else:
            return bracket

def get_formula1(bracket):
    """一级运算，公式到最简形式只包含加减"""
    print("\033[31;1m%s\033[0m"%bracket)
    while True:
        if re.search("[0-9]+\.?[0-9]*[\*|\/|\+|\-][0-9]+\.?[0-9]*", bracket):
            formula = re.search("[0-9]+\.?[0-9]*[\*|\/|\+|\-][0-9]+\.?[0-9]*", bracket).group()
            if re.search("^[\(]?[\-][0-9]+\.?[0-9]*[\+|\-][0-9]+\.?[0-9]*", bracket):
                sum=count_fushu(formula)
            else:
                sum=count_zhengshu(formula)
            formula=re.sub("\*","\*",formula)
            formula=re.sub("\/","\/",formula)
            formula=re.sub("\+","\+",formula)
            formula=re.sub("\-","\-",formula)
            bracket=re.sub(formula,str(sum),bracket)
        else:
            return bracket

def brackets(a):
    """公式中的括号进行分级处理，从最里面进行向外处理"""
    while True:
        try:
            bracket=re.search("\([\d|\.|\-|\+|\*|\/]+\)",a).group()
            try:
                new_result=re.search("\(([\-|\+]?.+)\)",str(get_formula2(bracket))).group(1)
            except AttributeError as e:
                new_result=str(get_formula1(bracket))

            bracket=re.sub("\(","\(",bracket)
            bracket=re.sub("\)","\)",bracket)
            bracket=re.sub("\+","\+",bracket)
            bracket=re.sub("\-","\-",bracket)
            bracket=re.sub("\*","\*",bracket)
            bracket=re.sub("\/","\/",bracket)
            a=re.sub(bracket,new_result,a)
            a=re.sub("\ ",'',a)
            while True:
                if re.search("([0-9]+\.?[0-9]*)([\*|\/])\-([0-9]+\.?[0-9]*)",a):
                    strings=re.search("([0-9]+\.?[0-9]*)(\*)\-([0-9]+\.?[0-9]*)",a)
                    string=strings.group()
                    string = re.sub("\+", "\+", string)
                    string = re.sub("\-", "\-", string)
                    string = re.sub("\*", "\*", string)
                    string = re.sub("\/", "\/", string)
                    new_string = "-" + strings.group(1) + strings.group(2) + strings.group(3)
                    a=re.sub(string,new_string,a)
                else:
                    break

            print(a)
            a=re.sub("\-{2}","+",a)
            a=re.sub("\+{2}","+",a)
            a=re.sub("\+\-","-",a)
            a=re.sub("\-\+","-",a)


        except AttributeError as e:
            total=get_formula2(a)
            return total



# a="  2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3/10)/ (16-3*2/5) ) "
a="100 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))*10 - (-4*3/10)/ (16-3*2/5) )-5/10*2"
# a="(-100+2*50-99-1)"
print("\033[32;1m%s\033[0m"%brackets(a))
