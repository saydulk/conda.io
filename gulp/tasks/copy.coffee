gulp = require "gulp"

simpleCopyTask = require "../utils/simpleCopyTask"

simpleCopyTask "fonts"
simpleCopyTask "img"
simpleCopyTask "requirejs"

gulp.task "copy", ["copy-fonts", "copy-img", "copy-requirejs"]
