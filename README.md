# chat
GitHub repository for my chatroom.

# Development
To set up:
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
To contribute:
<ol>
	<li>
		Create a new branch. This is where you'll work:
		'''git checkout -b [branch name]'''
	</li>
	<li>
		If you want to work on an existing branch:
		'''git pull origin [branch name]'''
	</li>
</ol>
To publish:
<ol>
	<li>
		Commit everything to your branch:
		'''git commit -m "[message]"'''
	</li>
	<li>
		Open a pull request:
		Go to '''https://github.com/W1nd0w55/chat/pull/new/[branch name]'''
	</li>
	<li>
		Once it is approved, delete your local branch:
		'''git branch -D [branch name]''',
		and pull from master:
		'''git pull origin master'''
	</li>
</ol>
