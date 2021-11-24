import requests


class InstaUserInfo:
    
    def __init__(self, user):
        self.user = user
        self.url = f'https://www.instagram.com/{self.user}/?__a=1'
        self.result = requests.get(self.url).json()
    
    def FullName(self):
        fullname = self.result['graphql']['user']['full_name']
        return fullname
    
    def ID(self):
        id = self.result['graphql']['user']['id']
        return id
    
    def Bio(self):
        bio = self.result['graphql']['user']['biography']
        return bio
    
    def Followers(self):
        followers = self.result['graphql']['user']['edge_followed_by']['count']
        return followers
    
    def Following(self):
        following = self.result['graphql']['user']['edge_follow']['count']
        return following
    
    def isPrivate(self):
        is_private = self.result['graphql']['user']['is_private']
        return is_private
    
    def isVerified(self):
        is_verified = self.result['graphql']['user']['is_verified']
        return is_verified
    
    def CategoryName(self):
        category_name = self.result['graphql']['user']['category_name']
        return category_name
    
    def isBusinessAccount(self):
        is_business_account = self.result['graphql']['user']['is_business_account']
        return is_business_account
    
    def isProfessionalAccount(self):
        is_professional_account = self.result['graphql']['user']['is_professional_account']
        return is_professional_account