%def_with check

%global descr MD4C is a fast, compact, and portable Markdown parser in C, fully compliant\
with CommonMark 0.31. It supports extensions, uses a push model with\
callbacks, and is easy to embed in other projects. MD4C is MIT-licensed,\
depends only on the standard C library, and supports UTF-8, ASCII, and\
UTF-16 encodings.

%global oname md4c

Name: libmd4c
Version: 0.5.3
Release: alt1

Summary: MD4C is Markdown parser implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/mity/md4c
Vcs: https://github.com/mity/md4c

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

%if_with check
BuildRequires(pre): rpm-build-python3
%endif

%description
%descr

%package devel
Summary: Development files for MD4C
Group: Development/C
Requires: %name

%description devel
Contains the library and header files needed to develop applications using
MD4C.
%descr

%package -n md2html
Summary: Convert markdown to HTML
Group: Text tools
Requires: %name

%description -n md2html
md2html is a small program that uses the minimalistic MD4C library.
It is designed to convert text with the markdown extension into an html
document. The program supports various command line arguments for configuring
the conversion.

%prep
%setup

%build
%cmake
%cmake_build

%check
# Tests should be run from the build directory
cd %_target_platform && %__python3 ../scripts/run-tests.py

%install
%cmake_install

%files
%_libdir/%name.so.*
%_libdir/%name-html.so.*

%files devel
%_libdir/%name.so
%_libdir/%name-html.so
%_libdir/cmake/%oname
%_includedir/%oname.h
%_includedir/%oname-html.h
%_pkgconfigdir/%oname.pc
%_pkgconfigdir/%oname-html.pc

%files -n md2html
%_bindir/md2html
%_man1dir/md2html.1.xz

%changelog
* Fri May 15 2026 Ulysses Apokin <ulysses@altlinux.org> 0.5.3-alt1
- New version.

* Wed Mar 26 2025 Ulysses Apokin <ulysses@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
