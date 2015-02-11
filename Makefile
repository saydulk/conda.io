gh-pages:
	git checkout gh-pages
	rm -rf public/

	git checkout master .
	git reset HEAD
	git checkout -- .gitignore  # make sure to ignore node_modules and bower_components

	gulp build
	python freeze.py

	git clean -fd

	rsync -av --remove-source-files ./public/ ./
	rm -rf ./public

	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" \
	&& git push conda gh-pages \
	; git checkout master
	rm -rf static/bower_components/  # final thing artifact that needs clearing
