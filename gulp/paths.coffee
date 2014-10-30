module.exports =
  html:
    src: "static/**/*.html"
    dest: "build/"

  bower:
    src: "bower_components/**"
    dest: "build/bower_components"

  fonts:
    src: "static/fonts/**/*.*"
    dest: "build/fonts/"

  images:
    src: "static/images/**/*.*"
    dest: "build/images/"

  # TODO: Determine if we still actually need this
  img:
    src: "static/img/**/*.*"
    dest: "build/img"

  sass:
    src: "static/scss/*.scss"
    watch: "static/scss/**/*.scss"
    dest: "build/css"

  coffee:
    src: "static/coffee/app.coffee"
    dest_filename: "app.js"
    dest_path: "build/js"
