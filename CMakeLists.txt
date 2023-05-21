cmake_minimum_required(VERSION 3.26)

project(Unite)

include(FetchContent)

FetchContent_Declare(
  PDFHummus
  GIT_REPOSITORY https://github.com/galkahana/PDF-Writer.git
  GIT_TAG        v4.5.6
  FIND_PACKAGE_ARGS
)
FetchContent_MakeAvailable(PDFHummus)

add_executable(Unite Unite.cpp)

target_link_libraries(Unite PDFHummus::PDFWriter)

