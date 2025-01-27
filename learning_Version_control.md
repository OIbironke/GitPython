# GIT fundamentals <br> 
## Objectives
- Learn what Version Control is
- Learn what Git is
  - Install Git
  - Create a repository
  - Stage and commit files in Git
- Create a GitHub account
  - Copy a local repo to GitHub
  - Copy a GitHub repo locally
- sync local and remote repo copies
---
## What is version control?
A track record of every version of any content version update. It is common to undo changes in any level of content e.g.
MS Word document. The version can provide an off site copy of the data should a need to restore due to loss, 
and supports/manages collaboration. In the case of overlapping, merging and conflicts can be identified and resolved.
This is valuable not just to developers and data scientists but to anyone who works with data.
---
## What is Git?
It is a Version Control System (VCS).
Primary benefits of Git include: <br>
- Speed
- Modern
- Fully featured
- Open Source (free)
- Most popular VCS

Git comes with a command-line interface called Git bash which all commands can be run through.
Git server which is included with Git can be used to copy data. Git can work with GitHub Desktop 
and Popular IDE's have integration with Git. This means you can store your code and manage your repository 
on your IDE. Important to note that the unit of operation of Git is called a "repository" or "repo" for short.<br>
---
## Installing Git and making a creating a repository
Step 1: Go to [Git main website](http://git-scm.com/downloads) <br>
Step 2: Select the platform applicable to your system (Windows in this case) and follow the instructions.<br>
If the option to "Only Show new options" is available, toggle that. It will condense the intallation configuration. <br>
Step 3: At the final setup window, select "Launch Git Bash" and then "Finish" <br>
Step 4: Configure your username and email:

```bash
# Set your username
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"
```

In an individual contributor system an individual branch is normal. With a version control, you can experiment and test
your update. If the update fails you can revert effectively deletingthe updates. <br>
Branching is verbatum creating a separate (test) line of a code process that does not affect the main branch. If the test is
successful, you can merge the branch. Branching is important for collaboration. Common convention is naming the branch 
according to the feature that is being developed.<br>
There are 3 levels of confiurations in descending order:
- System [git config --system user.name]
- Global [git config --global user.name]
- Local [git config --local user.name]
<br>
---
<br> 

## Gitignore <br>
It is extrememly important to create a git ignore file when dealing with projects on repositories.
Presenting syntax that does not include your sensitive information is common practice and online platforms like GitHub have 
systems that can auto genetate .gitignore files for you. Manually creating your own is doable by following the next three steps:<br>
Step 1
```bash 
Open Notepad
notepad .gitignore

```
<br>
You will now have the opportunity to create a new Notepad file. If you chose a different text editor, you will likely still have 
to create a new file. <br>
Step 2 <br>
In the notepad file, enter the following characters excluding the quotation marks:<br>
"# Exclude all properties and files from my repo"<br>
"*.properties"

Step 3 <br>
Save the file. The second line ensures that properties files will not be controlled by Git

---
## Stage and commit files in Git
Git works as an opt in system meaning all files are exluded by default until you include files into the Staging area. <br>
Working Directory is the initial location. Using [git add] moves to the Staging Area (index) and [git commit] moves to
the Local Repository.

---

Verify your configuration: <br>
Before you continue, Verify your configuration w.r.t. permissions
```bash
git config --list
```

---

## Creating a Repository

A repository (repo) is where your project's files and Git history are stored.

### 1. Initialize a New Repository

Navigate to your project folder and run:

```bash
git init
```

This command creates a `.git` directory that tracks your project.

### 2. Add Files to the Repository

Add files to the staging area:

```bash
git add .
```

### 3. Commit Changes

Save your changes to the repository:

```bash
git commit -m "Initial commit"
```



## Summary

- Use `git init` to initialize a repository.
- Use `git add` and `git commit` to track changes.
- Use branches and pull requests to collaborate efficiently.

<br> 
Useful Commands Cheatsheet <br>

| Command                      | Description                                                                   |
|------------------------------|-------------------------------------------------------------------------------|
| clear                        | Clear current console log                                                     |
| pwd                          | Print working directory                                                       |
| mkdir                        | Create empty git repository in current directory                              |
| git init                     | Initialise current directory to be managed by Git                             |
| ls                           | List all files in current directory                                           |
| ls -al                       | List all files in current directory including hidden files                    |
| notepad .gitignore           | create a notepad file. The aim is to exclude sensitive data from repositories |
| git diff                     | Show difference between files on stage and                                    |
| git commit -m "`message`"    | Commit a staged file with a message. Use an appropriate descriptor            |
| git commit -a -m "`message`" | Add and commit a file all in one. Use an appropriate message                  |
| git status                   | Check the status of any files pending committal                               |
| git log                      | Track history of version changes                                              |
| git add                      | Opt a file into Git management                                                |

---
## Create GitHub account
To create a GitHub account, do the following: <br>
1 - Go to [GitHub website](https://github.com)<br>
2 - Follow the step by step process ensuring you use the same identification credentials 
i.e. Name and email as your Git Bash console
3 - Before jumping into the next stage, ensure you have validated your email and you have explored GitHub somewhat.

---
## Managing a repository online
- Ensure the `HTTPS` option is toggled for this setup
- Copy the https link to you bash console. It should look like this:
```bash 
 $ git remote add origin https://github.com/....
 
```
- You will now have to authenticate your connection if you are not on `master`. Here are detailed instruction [HTTPS Github setup](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)

- You can choose to use SSH to manage authentication. Should you choose SSH, in order to keep this guide short I will 
Recommend you use this link for detailed instructions [SSH instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
 

---

## Connecting to a Remote Repository

To collaborate with others, connect your local repository to a remote repository (e.g., on GitHub, GitLab). You will 
still need to send a link to your online profile to which the owner of the repository can add you to the contributor list.


### 1. Add a Remote Repository

```bash
git remote add origin https://github.com/username/repository-name.git
```

### 2. Push Changes to the Remote Repository

```bash
git push -u origin main
```

---

## Branching and Pull Requests

### 1. Create a New Branch

Branches allow you to work on new features without affecting the main codebase.

```bash
git checkout -b feature-branch
```

### 2. Make Changes and Commit

After making changes, add and commit them:

```bash
git add .
git commit -m "Add new feature"
```

### 3. Push Your Branch

```bash
git push origin feature-branch
```

### 4. Create a Pull Request

1. Go to your remote repository on GitHub.
2. Click **Pull Requests**.
3. Click **New Pull Request**.
4. Compare your branch with the `main` branch.
5. Add a title and description, then click **Create Pull Request**.

---

## Merging Pull Requests

1. Review the pull request.
2. Merge the pull request into the main branch.
3. Update your local repository:

```bash
git checkout main
git pull origin main
```
## Conflict
With user Stories and branching we can sandbox each operation which should streamline development 
but sometimes merge onflicts can arise for a myriad of reasons. Normally we will see a status message when we attempt to merge or pull changes.
<br>
Here are some guigelines to deal with conflicts:<br>
- Resolve locally. We do this by reviewing the code to make sure it works as intended first
- Use the command `git status` to see the list of conflicting files
- Edit the files to ensure that the branches will pass the next pull/merge request by validating the code (still local)
- Finally repeat the pull request to confirm problem has been resolved

---
## Final notes 
As we have seen with group projects, it is important to specialised roles in each development team.
One key member is the "Git Auth" who will manage the account, make new branches and assign reviewers for merge requests etc.
