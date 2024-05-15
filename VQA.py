import SparkApi

# 以下密钥信息从控制台获取
appid = "5f39ccd8"  # 填写控制台中获取的 APPID 信息
api_secret = "ZWUxMjhhM2VkNzk1MzI5N2FhYzliODZk"  # 填写控制台中获取的 APISecret 信息
api_key = "f6d0d54675341a4dc0404aa640afc3e7"  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
domain = "general"  # v1.5版本
# domain = "generalv2"    # v2.0版本
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址


text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    print("Text:", text)  # 添加这一行以查看传入的文本
    if text is None:
        print("Text is None")  # 如果文本是None，打印一条消息
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text




# if __name__ == '__main__':
#     # text.clear
#     while (1):
#         Input = input("\n" + "聪明且帅气的我:")  # 输入问题
#         question = checklen(getText("user", Input))
#         SparkApi.answer = ""
#         print("安中问答:", end="")
#         SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
#         getText("assistant", SparkApi.answer)
#         print(SparkApi.get_ans(), end='')