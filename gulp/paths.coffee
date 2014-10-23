module.exports =
  fonts:
    src: "static/vendor/font-awesome/font/*.*"
    dest: "static/font/"

  # TODO: Determine if we still actually need this
  img:
    src: "static/img/**/*.*"
    dest: "build/img"

  sass:
    src: "source/scss/*.scss"
    dest: "build/css"

  coffee:
    src: "source/coffee/index.coffee"
    dest_filename: "index.js"
    dest_path: "build/js"
