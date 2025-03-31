%def_with check

%define oname md4c

Name: libmd4c
Version: 0.5.2
Release: alt1

Summary: MD4C is Markdown parser implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/mity/md4c
Vcs: https://github.com/mity/md4c

Source: %name-%version.tar

BuildRequires(pre): cmake

%if_with check
BuildRequires: python3
%endif

%description
%summary, with the following features.

* Compliance: Generally, MD4C aims to be compliant to the latest version of
CommonMark specification. Currently, we are fully compliant to
CommonMark 0.31.

* Extensions: MD4C supports some commonly requested and accepted extensions.
See below.

* Performance: MD4C is very fast.

* Compactness: MD4C parser is implemented in one source file and one header
file. There are no dependencies other than standard C library.

* Embedding: MD4C parser is easy to reuse in other projects, its API is
very straightforward: There is actually just one function, md_parse().

* Push model: MD4C parses the complete document and calls few callback
functions provided by the application to inform it about a start/end of
every block, a start/end of every span, and with any textual contents.

* Portability: MD4C builds and works on Windows and POSIX-compliant OSes.
(It should be simple to make it run also on most other platforms, at least as
long as the platform provides C standard library, including a heap memory
management.)

* Encoding: MD4C by default expects UTF-8 encoding of the input document.
But it can be compiled to recognize ASCII-only control characters (i.e. to
disable all Unicode-specific code), or (on Windows) to expect UTF-16 (i.e.
what is on Windows commonly called just "Unicode"). See more details below.

* Permissive license: MD4C is available under the MIT license.

%package devel
Summary: Development files for MD4C
Group: Development/C
Requires: %name = %EVR

%description devel
Contains the library and header files needed to develop applications using
MD4C.

%package -n md2html
Summary: Convert markdown to HTML
Group: Text tools
Requires: %name = %EVR

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
cd %_target_platform && bash ../scripts/run-tests.sh

%install
%cmake_install

%files
%_libdir/%name.so.*
%_libdir/%name-html.so.*

%files devel
%_libdir/%name.so
%_libdir/%name-html.so
%_libdir/cmake/%oname/%{oname}Config*.cmake
%_includedir/%oname.h
%_includedir/%oname-html.h
%_pkgconfigdir/%oname.pc
%_pkgconfigdir/%oname-html.pc

%files -n md2html
%_bindir/md2html
%_man1dir/md2html.1.xz

%changelog
* Wed Mar 26 2025 Ulysses Apokin <ulysses@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
