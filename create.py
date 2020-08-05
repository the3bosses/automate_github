#!/Users/constant.vdw/.pyenv/shims/python
import os
import errno
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
assert opts.headless


driver = webdriver.Firefox(options=opts, executable_path='/Users/constant.vdw/Documents/geckodriver')

# Creating a folder to use for git repo
def create_folder():
  # Asking for the folder name to create 
  folder_name = str(sys.argv[1])
  if os.path.exists('/Users/constant.vdw/Documents/Projects'):
    os.chdir('/Users/constant.vdw/Documents/Projects')
    os.path.exists(f'/Users/constant.vdw/Documents/Projects/{folder_name}')
    try:
        os.makedirs(folder_name)
        os.chdir(f'/Users/constant.vdw/Documents/Projects/{folder_name}')
        os.system('ls -la')
    except OSError as e:
      if e.errno == errno.EEXIST:
        print(e)
        print('Cannot change to the Current Working Directory')
        print('Current Working Directory ', os.getcwd())
        sys.exit(-1)

# Create git repo
def create_git_repo():
  # Enter the name for the git repo
  repo_name = str(sys.argv[2])

  # Creating Git Repo
  driver.get('https://github.com/login')
  driver.maximize_window()
  driver.find_element_by_id('login_field')\
    .click()
  driver.find_element_by_id('login_field')\
    .send_keys('the3bosses@gmail.com')
  driver.find_element_by_id('password').click()
  driver.find_element_by_id('password').send_keys('Danica@2022')
  driver.find_element_by_class_name('btn-primary').click()
  sleep(3)
  driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
  driver.find_element_by_id('repository_name').send_keys(repo_name)
  sleep(5)
  driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').click()
  git_uri = driver.find_element_by_id('empty-setup-clone-url').get_attribute('value')
  print(git_uri)
  os.system(f'git clone {git_uri}')
  driver.quit()

# Git Commands
  os.system(f'git clone {git_uri}')
  os.chdir(f'{repo_name}')
  os.system('echo "# repo_created" >> README.md')
  os.system('git init')
  os.system(f'git add README.md')
  os.system("git commit -m 'initial commit'")
  os.system('git push -u origin master')
  os.system('code .')

if __name__ == '__main__':
  create_folder()
  create_git_repo()
  



