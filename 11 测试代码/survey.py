class AnonymousSurvey:
    """收集问卷答案"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份答案"""
        self.responses.append(new_response)

    def show_result(self):
        """显示所有答案"""
        print("Result:")
        for response in self.responses:
            print(f"- {response}")


# # 定义问题并创建对象
# question = "your first language"
# language_survey = AnonymousSurvey(question)
#
# # 显示问题并存储答案
# language_survey.show_question()
# print("'q' to quit")
# while True:
#     response = input("language: ")
#     if response == 'q':
#         break
#     language_survey.store_response(response)
#
# # 显示问卷结果
# print("\nthank you write survey")
# language_survey.show_result()