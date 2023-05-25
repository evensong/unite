# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-src"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-build"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/tmp"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/src/pdfhummus-populate-stamp"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/src"
  "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/src/pdfhummus-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/src/pdfhummus-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/APP/source/repos/unite/out/build/x64-Debug/_deps/pdfhummus-subbuild/pdfhummus-populate-prefix/src/pdfhummus-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
