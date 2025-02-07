# chat
GitHub repository for my chatroom.

# Development
## Setup
<ol>
	<li>Set up your project directory</li>
	<li>
		Initialize:
		'''git init'''
	</li>
	<li>
		 Add this repository:
		'''git remote add origin https://github.com/W1nd0w55/chat.git'''
	</li>
	<li>Finally, run '''git pull origin master''' to get the '''master''' branch (or whatevet branch you want)</li>
</ol>
## Contributing
<ol>
	<li>
		Create a new branch. This is where you'll work:
		'''git checkout -b [branch]'''
	</li>
	<li>
		If you want to work on an existing branch:
		'''git pull origin [branch]'''
	</li>
</ol>
## Publishing
<ol>
	<li>
		Commit everything to your branch:
		'''git commit -m "[message]"'''
	</li>
	<li>
		Open a pull request:
		Go to '''https://github.com/W1nd0w55/chat/pull/new/[branch]'''
	</li>
	<li>
		Once it is approved, delete your local branch:
		'''git branch -D [branch]''',
		and pull from master:
		'''git pull origin master'''
	</li>
</ol>
