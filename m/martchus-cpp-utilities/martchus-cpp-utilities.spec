%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: martchus-cpp-utilities
Version: 5.33.0
Release: alt1

Summary: useful C++ classes and routines used by Martchus' applications
License: GPL-2.0-or-later
Group: Development/C++
Url: https://github.com/Martchus/cpp-utilities

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

%description
%summary

%package -n libmartchus-c++utilities5
Summary: useful C++ classes and routines used by Martchus' applications
Group: System/Libraries

%description -n libmartchus-c++utilities5
Martchus-cpp-utilities is a library that contains helpers for:

* parsing command-line arguments and providing Bash completions
* working with dates and times
* converting primitive data types to byte-buffers, and vice versa
  (eg, between litte-endian and big-endian)
* common string conversions/operations
* using standard IO streams
* using SFINAE by providing additional traits (eg, for checking whether a
  type is iteratable)
* testing with *CppUnit*
* CMake, with convenient modules and templates

It also provides the following convenience functions and data structures:

* min() and max(), for any number of arguments
* digitsum(), factorial(), powerModulo(), inverseModulo(), and orderModulo()
* Damerau-Levenshtein distance
* *N*-dimensional arrays

%package -n libmartchus-c++utilities-devel
Summary: useful C++ classes and routines used by Martchus' applications (headers)
Group: Development/C++

%description -n libmartchus-c++utilities-devel
Martchus-cpp-utilities is a library that contains helpers for:

* parsing command-line arguments and providing Bash completions
* working with dates and times
* converting primitive data types to byte-buffers, and vice versa
  (eg, between litte-endian and big-endian)
* common string conversions/operations
* using standard IO streams
* using SFINAE by providing additional traits (eg, for checking whether a
  type is iteratable)
* testing with *CppUnit*
* CMake, with convenient modules and templates

It also provides the following convenience functions and data structures:

* min() and max(), for any number of arguments
* digitsum(), factorial(), powerModulo(), inverseModulo(), and orderModulo()
* Damerau-Levenshtein distance
* *N*-dimensional arrays

This is the development version of the library. You will need this only if
you intend to compile programs that use this library.

%prep
%setup
sed -i "s|https://github.com/Martchus/cpp-utilities/blob/master/doc/buildvariables.md|buildvariables.md|" README.md

%build
%cmake \
       -DBUILD_SHARED_LIBS=ON \
       -DNAMESPACE=martchus
%cmake_build

%install
%cmake_install

%files -n libmartchus-c++utilities5
%_libdir/libmartchus-c++utilities.so.5*

%files -n libmartchus-c++utilities-devel
%doc LICENSE README.md
%doc doc/buildvariables.md doc/testapplication.md
%dir %_includedir/martchus-c++utilities
%dir %_includedir/martchus-c++utilities/c++utilities
%dir %_includedir/martchus-c++utilities/c++utilities/application
%_includedir/martchus-c++utilities/c++utilities/application/argumentparser.h
%_includedir/martchus-c++utilities/c++utilities/application/commandlineutils.h
%_includedir/martchus-c++utilities/c++utilities/application/fakeqtconfigarguments.h
%_includedir/martchus-c++utilities/c++utilities/application/global.h
%_includedir/martchus-c++utilities/c++utilities/c++utilities-definitions.h
%dir %_includedir/martchus-c++utilities/c++utilities/chrono
%_includedir/martchus-c++utilities/c++utilities/chrono/datetime.h
%_includedir/martchus-c++utilities/c++utilities/chrono/format.h
%_includedir/martchus-c++utilities/c++utilities/chrono/period.h
%_includedir/martchus-c++utilities/c++utilities/chrono/timespan.h
%dir %_includedir/martchus-c++utilities/c++utilities/conversion
%_includedir/martchus-c++utilities/c++utilities/conversion/binaryconversion.h
%_includedir/martchus-c++utilities/c++utilities/conversion/binaryconversionprivate.h
%_includedir/martchus-c++utilities/c++utilities/conversion/conversionexception.h
%_includedir/martchus-c++utilities/c++utilities/conversion/stringbuilder.h
%_includedir/martchus-c++utilities/c++utilities/conversion/stringconversion.h
%_includedir/martchus-c++utilities/c++utilities/global.h
%dir %_includedir/martchus-c++utilities/c++utilities/io
%_includedir/martchus-c++utilities/c++utilities/io/ansiescapecodes.h
%_includedir/martchus-c++utilities/c++utilities/io/binaryreader.h
%_includedir/martchus-c++utilities/c++utilities/io/binarywriter.h
%_includedir/martchus-c++utilities/c++utilities/io/bitreader.h
%_includedir/martchus-c++utilities/c++utilities/io/buffersearch.h
%_includedir/martchus-c++utilities/c++utilities/io/copy.h
%_includedir/martchus-c++utilities/c++utilities/io/inifile.h
%_includedir/martchus-c++utilities/c++utilities/io/misc.h
%_includedir/martchus-c++utilities/c++utilities/io/nativefilestream.h
%_includedir/martchus-c++utilities/c++utilities/io/path.h
%dir %_includedir/martchus-c++utilities/c++utilities/misc
%_includedir/martchus-c++utilities/c++utilities/misc/flagenumclass.h
%_includedir/martchus-c++utilities/c++utilities/misc/levenshtein.h
%_includedir/martchus-c++utilities/c++utilities/misc/math.h
%_includedir/martchus-c++utilities/c++utilities/misc/multiarray.h
%_includedir/martchus-c++utilities/c++utilities/misc/parseerror.h
%_includedir/martchus-c++utilities/c++utilities/misc/signingkeys.h
%_includedir/martchus-c++utilities/c++utilities/misc/traits.h
%_includedir/martchus-c++utilities/c++utilities/misc/verification.h
%dir %_includedir/martchus-c++utilities/c++utilities/tests
%_includedir/martchus-c++utilities/c++utilities/tests/cppunit.h
%_includedir/martchus-c++utilities/c++utilities/tests/outputcheck.h
%_includedir/martchus-c++utilities/c++utilities/tests/testutils.h
%_includedir/martchus-c++utilities/c++utilities/version.h
%_libdir/libmartchus-c++utilities.so
%_pkgconfigdir/martchus-c++utilities.pc
%dir %_datadir/martchus-c++utilities
%dir %_datadir/martchus-c++utilities/cmake/
%_datadir/martchus-c++utilities/cmake/martchus-c++utilitiesConfig.cmake
%_datadir/martchus-c++utilities/cmake/martchus-c++utilitiesConfigVersion.cmake
%_datadir/martchus-c++utilities/cmake/martchus-c++utilitiesTargets-*.cmake
%_datadir/martchus-c++utilities/cmake/martchus-c++utilitiesTargets.cmake
%dir %_datadir/martchus-c++utilities/cmake/modules
%_datadir/martchus-c++utilities/cmake/modules/3rdParty.cmake
%_datadir/martchus-c++utilities/cmake/modules/3rdPartyFunctions.cmake
%_datadir/martchus-c++utilities/cmake/modules/AppTarget.cmake
%_datadir/martchus-c++utilities/cmake/modules/AppUtilities.cmake
%_datadir/martchus-c++utilities/cmake/modules/BasicConfig.cmake
%_datadir/martchus-c++utilities/cmake/modules/ConfigHeader.cmake
%_datadir/martchus-c++utilities/cmake/modules/DevelUtilities.cmake
%_datadir/martchus-c++utilities/cmake/modules/Doxygen.cmake
%_datadir/martchus-c++utilities/cmake/modules/LibraryTarget.cmake
%_datadir/martchus-c++utilities/cmake/modules/ListToString.cmake
%_datadir/martchus-c++utilities/cmake/modules/ShellCompletion.cmake
%_datadir/martchus-c++utilities/cmake/modules/Sphinx.cmake
%_datadir/martchus-c++utilities/cmake/modules/TemplateFinder.cmake
%_datadir/martchus-c++utilities/cmake/modules/TestTarget.cmake
%_datadir/martchus-c++utilities/cmake/modules/TestUtilities.cmake
%_datadir/martchus-c++utilities/cmake/modules/WindowsResources.cmake
%dir %_datadir/martchus-c++utilities/cmake/templates
%_datadir/martchus-c++utilities/cmake/templates/Config.cmake.in
%_datadir/martchus-c++utilities/cmake/templates/appdata.xml.in
%_datadir/martchus-c++utilities/cmake/templates/bash-completion.sh.in
%_datadir/martchus-c++utilities/cmake/templates/config.h.in
%_datadir/martchus-c++utilities/cmake/templates/desktop.in
%_datadir/martchus-c++utilities/cmake/templates/doxygen.in
%_datadir/martchus-c++utilities/cmake/templates/global.h.in
%_datadir/martchus-c++utilities/cmake/templates/sphinx-conf.py.in
%_datadir/martchus-c++utilities/cmake/templates/template.pc.in
%_datadir/martchus-c++utilities/cmake/templates/version.h.in
%_datadir/martchus-c++utilities/coding-style.clang-format
%dir %_datadir/martchus-c++utilities/tests
%_datadir/martchus-c++utilities/tests/calculateoverallcoverage.awk

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 5.33.0-alt1
- New version 5.33.0.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 5.32.1-alt1
- New version 5.32.1.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 5.32.0-alt1
- New version 5.32.0.

* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 5.31.1-alt1
- Initial build for Sisyphus
