import json
def show(self):
        body = self.request.body.decode('utf-8')  
        print(body)  
        # body = json.loads(body)
        # print(body)
        # print('-'*50)
        # print(body['responseId'])#1        
        # print('-'*50)
        # print(body['queryResult'])#2
        # print(body['queryResult']['action'])        
        # print(body['queryResult']['queryText'])
        # print('-'*50) 
        # print(body['originalDetectIntentRequest'])#3
        # print(body['originalDetectIntentRequest']['payload'])       
        # print(body['originalDetectIntentRequest']['payload']['data'])
        # print(body['originalDetectIntentRequest']['payload']['data']['replyToken'])
        # print(body['originalDetectIntentRequest']['payload']['data']['source']['userId'])  
        # print('-'*50)
        # print(body['session'])#4     
        # print('-'*50)    
