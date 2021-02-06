''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 3: Version Control and Introduction to Containers 
        
    Overview: In this script, we will look at the version control system, "Git"
Of the numerous version control systems available (Git, Subversion, CVS, Mercurial),
Git seems to be the most popular, and in general, it is great for 

   - Collaborating with others on code
   - Supporting multiple concurrent versions (branches)
   - Tagging releases or snapshots in time
   - Restoring previous versions of files
   - What it lacks in user-friendliness it makes up for in good documentation
   - Intuitive web platforms available 


"GitHub" is a web platform where you can host and share Git repositories (repos).
Repositories can be public or private. 

                                     The Basics of Git 
                                     
Version Control Systems start with a base version of the document and then 
record cahnges that are made each step of the way. Two or more users can 
make changes on the same document. Unless there are conflicts, two or more
sets of changes can also be incorporated into the same base document. 
A version control system is a tool that keeps track of these changes for us, 
effectively creating different versions of our files. It allows for us to 
decide which changes will be made to the next version (each record of these
changes is called "commit", and keeps useful metadata about them. The complete
history for a particular project and their metadata make up a "repository").
Repositories can be kept in sync across different computers, facilitating 
collaboration among different people. 

Git uses the special directory "./git" to store all of the information about
a project, including all files and sub-directories located within the 
project's directory. If the "./git" sub-directory is ever deleted, the 
project's history will be lost. 

We can check that everything is set up correctly by asking Git to tell us 
about the status of our project: 
    
"git status" 

The command "git add <filename> can be used to add files in the current directory
to a git repository in that directory". After a file is added to the repository, 
the command "git commit -m "Some Optional Message"" then takes everything 
that we have told Git to save from using "git add", and stores a copy permanently
inside the special ".git" directory. This permanent copy is called a "commit", 
or a "revision".

The "-m" flag is used to record a short descriptive, and specific comment that 
will help us remember later on what we did and why. Good commit messages start
with a brief (<50 characters) statement about the changes made in the commit. 
Generally, the message should complete the sentence "If applied, this commit 
will <commit message here>." If you want to go into more detail, add a blank
line between the summary line and your additional notes. Use this additional 
space to explain why you made the changes and/or what their impact will be. 

If we want to know what we have done recently, we can ask Git to show us 
the project's history using "git log". This command lists all commits made to 
a repository in reverse chronological order. The listing for each commit includes

- the commit's full identifier (which starts with the same characters as the 
short identifier printed by the "git commit" command

- the commit's author

- when the commit was created

'- the log message Git was given when the commit was created 

- The command "git diff <filename>", shows us the differences between the current state
of the file and the most recently saved version      

If you create a directory in your Git repository and populate it with files, 
you can add all files in the directory at once using the command

"git add <directory-with-files>"                            


                        Restoring Old Versions of Files 
                        
The command "echo "" > <filename>" can be used to overwrite a file with an 
empty string which essentially deletes the contents of the file from memory.
The contents of the file can be restored using "git checkout", and by referring
to the most recent commit of the working directory by using the identifier 
"HEAD". An example would be "git checkout HEAD json_ex.py". 
If we want to go back even further, we can use a commit identifier as 
"git checkout <commit identifier> <filename>"                        
                        
 
                            Link a Local Repository to GitHub
                            
Systems like Git allow for us to move work between any two repositories. In 
practice though, it's easiest to use one copy as a central hub, and to keep 
it on the web rather than on someone's laptop.

An existing repository can be pushed from a local directory to a GitHub 
repository (web-accessible interface) using the command 
"git remote add origin <https link>" 

A branch in a local repository can be renamed using "git branch -M <newname>"

The command "git push -u origin main" pushes all of the local code and 
changes up to the cloud, and sets the upstream(the location that should be 
pushed to origin)
                        
Anyone can make a full copy of a repository on GitHub including all the 
commit history by performing "git clone <url address>" 


                                   Fork
                                   
A fork is a personal copy of another user's repository that lives on your 
account. Forks allow you to freely make changes to a project without affecting
the original. Forks remain attached to the original, allowing you to submit
a pull request to the original's author to update with your changes. You can 
also keep your fork up to date by pulling in updates from the original. 


                                    Branch
                                    
A branch is a parallel version of a repository. It is contained within the 
repository but it does not affect the primary or master branch, allowing you
to work freely without disrupting the "live" version. When you've made the 
changes you want to make, you can merge your branch back into the master branch
to publish your changes.'

                                  Pull Request / Merge Request

Pull requests are proposed changes to a repository submitted by a user and 
accepted or rejected by a repository's collaborators. '                                    

"README.md" is the landing page of the repository which is a good place to 
describe the project and list appropriate citations
                  