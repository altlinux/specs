%define _unpackaged_files_terminate_build 1
%def_with docs

%ifarch %valgrind_arches
%def_enable valgrind
%endif

Name: rapidjson
Version: 1.1.0
Release: alt6.git473553bd

Summary: Fast JSON parser and generator for C++

License: MIT
Group: Development/C++
Url: https://rapidjson.org/
Vcs: https://github.com/Tencent/rapidjson.git

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
# Downstream-patch for gtest.
Patch1: rapidjson-1.1.0-do_not_include_gtest_src_dir.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: cmake gcc-c++
BuildRequires: libgtest-devel
%{?_enable_valgrind:BuildRequires: valgrind}
%{?_with_docs:BuildRequires: doxygen python3-module-pydot}

%description
RapidJSON is a fast JSON parser and generator for C++.  It was
inspired by RapidXml.

RapidJSON is small but complete.  It supports both SAX and DOM style
API. The SAX parser is only a half thousand lines of code.

RapidJSON is fast.  Its performance can be comparable to strlen().
It also optionally supports SSE2/SSE4.1 for acceleration.

RapidJSON is self-contained.  It does not depend on external
libraries such as BOOST.  It even does not depend on STL.

RapidJSON is memory friendly.  Each JSON value occupies exactly
16/20 bytes for most 32/64-bit machines (excluding text string). By
default it uses a fast memory allocator, and the parser allocates
memory compactly during parsing.

RapidJSON is Unicode friendly.  It supports UTF-8, UTF-16, UTF-32
(LE & BE), and their detection, validation and transcoding
internally. For example, you can read a UTF-8 file and let RapidJSON
transcode the JSON strings into UTF-16 in the DOM. It also supports
surrogates and "\u0000" (null character).

JSON(JavaScript Object Notation) is a light-weight data exchange
format. RapidJSON should be in fully compliance with RFC4627/ECMA-404.

%package devel
Summary: Fast JSON parser and generator for C++
Group: Development/C++
Provides: %name = %EVR

%description devel
RapidJSON is a fast JSON parser and generator for C++.  It was
inspired by RapidXml.

RapidJSON is small but complete.  It supports both SAX and DOM style
API. The SAX parser is only a half thousand lines of code.

RapidJSON is fast.  Its performance can be comparable to strlen().
It also optionally supports SSE2/SSE4.1 for acceleration.

RapidJSON is self-contained.  It does not depend on external
libraries such as BOOST.  It even does not depend on STL.

RapidJSON is memory friendly.  Each JSON value occupies exactly
16/20 bytes for most 32/64-bit machines (excluding text string). By
default it uses a fast memory allocator, and the parser allocates
memory compactly during parsing.

RapidJSON is Unicode friendly.  It supports UTF-8, UTF-16, UTF-32
(LE & BE), and their detection, validation and transcoding
internally. For example, you can read a UTF-8 file and let RapidJSON
transcode the JSON strings into UTF-16 in the DOM. It also supports
surrogates and "\u0000" (null character).

JSON(JavaScript Object Notation) is a light-weight data exchange
format. RapidJSON should be in fully compliance with RFC4627/ECMA-404.

%package doc
Summary: Documentation-files for %name
Group: Documentation
BuildArch: noarch

%description doc
This package contains the documentation-files for %name.

%prep
%setup
%autopatch -p1

# Fix 'W: wrong-file-end-of-line-encoding'.
find example -type f -name '*.c*' -print0 |
	xargs -r0 subst -p 's!\r$!!g' license.txt

# Create an uncluttered backup of examples for inclusion in %%doc.
cp -a example examples

# Disable -Werror.
find . -type f -name 'CMakeLists.txt' -print0 |
	xargs -r0 sed -i -e's![ \t]*-march=native!!g' -e's![ \t]*-Werror!!g'

# c++11 does not work with gtest 1.13+
sed -i 's/ -std=c++11//' CMakeLists.txt

%build
%cmake \
    -DDOC_INSTALL_DIR=%_docdir/%name-doc-%version \
    -DGTESTSRC_FOUND=TRUE \
    -DGTEST_SOURCE_DIR=.
%cmake_build

%install
%cmakeinstall_std

# Move pkgconfig and CMake-stuff to generic datadir.
mv -f %buildroot%_libdir/* %buildroot%_datadir

# Copy the documentation-files to final location.
cp -at %buildroot%_docdir/%name-doc-%version -- examples

#Removing duplicate readme.md with meta package devel.
rm -f %buildroot%_docdir/%name-doc-%version/readme.md

# Find and purge build-sys files.
find %buildroot -type f -name 'CMake*.txt' -print0 |
	xargs -r0 rm -fv --

%files devel
%doc license.txt CHANGELOG.md readme*.md
%_datadir/cmake
%ifarch x86_64 aarch64 ppc64le
%_libexecdir/cmake
%endif
%_datadir/pkgconfig/*
%_includedir/%name

%files doc
%doc %_docdir/%name-doc-%version/examples
%if_with docs
%doc %_docdir/%name-doc-%version/html
%endif # docs

%changelog
* Tue Sep 26 2023 Aleksei Kalinin <kaa@altlinux.org> 1.1.0-alt6.git473553bd
- Location of documentation files has been sepporated.
- Add missing cmake instructions file for x86_64 arch.
- Add option to spec for strict check unpacked files.

* Mon May 15 2023 Aleksei Kalinin <kaa@altlinux.org> 1.1.0-alt5.git473553bd
- Added cursor wrapper support. Required for OpenTimelineIO package.
- Changed GIT package strategy and worktree
- Other upstream updates.

* Tue Apr 04 2023 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt4
- rename package rapidjson to rapidjson-devel (Closes: 45742)
- Clear Packager

* Sat Jan 28 2023 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt3
- Don't force C++11 to fix FTBFS with gtest 1.13+

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- fix BR

* Wed Oct 09 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1.1.1
- Added the missing bit so that valgrind is not simply dropped out.

* Wed Oct 09 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1.1
- Move to rpm-macros-valgrind.
- Spec cleanup.

* Wed Nov 15 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus.
