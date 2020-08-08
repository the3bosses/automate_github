from github import Github
from githubtools import *



access_token = ''

login = Github(access_token)

repos = login.search_repositories(query="language:python")

user = login.get_user()

# test = user.create_repo(name='git_test_auto_three')

# test.create_file("/Readme")

# repo_name = user.login + "-"

user.get_repo(name='git_test_auto_testing').delete()
user.get_repo(name='git_test_auto_three').delete()
user.get_repo(name='git_test_auto_two').delete()
user.get_repo(name='new_repo_name').delete()
user.get_repo(name='new_repo_test_four').delete()
user.get_repo(name='new_test_created').delete()
user.get_repo(name='real_test').delete()

# rep.delete

# org = login.get_organization('the3bosses')
# for o in org:
#   print(o)

# org.create_repo('test_repo')

for repo in login.get_user().get_repos():
  print(repo.name)

