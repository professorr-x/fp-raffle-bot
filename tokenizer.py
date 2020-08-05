from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import json


class CaptchaToken:

    with open('settings/config.json') as f:
        settings = json.load(f)

    api_key = settings['anticaptcha']['api_key']
    site_key = '6LfIUL8UAAAAAMvYieKAMgh4e9qQFpLiLdqLLJG4'  # grab from site
    url = 'https://raffles.footpatrol.com/off-white-x-nike-air-jordan-4-u5wtuddl-428'
    
    def getToken(self):
        client = AnticaptchaClient(self.api_key)
        task = NoCaptchaTaskProxylessTask(self.url, self.site_key)
        job = client.createTask(task)
        job.join()
        return job.get_solution_response()
