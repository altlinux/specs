Name: utf8proc
Version: 2.8.0
Release: alt1

Summary: Library for processing UTF-8 encoded Unicode strings
License: BSD
Group: System/Libraries

Url: http://julialang.org/utf8proc/
Source: https://github.com/JuliaLang/utf8proc/archive/v%version.tar.gz#/%name-%version.tar.gz

%description
utf8proc is a library for processing UTF-8 encoded Unicode strings

%package -n lib%name
Summary: Library for processing UTF-8 encoded Unicode strings
Group: System/Libraries

%description -n lib%name
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

The currently supported Unicode version is 14.
This package only contains the C library.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/Other

%description -n lib%name-devel
Contains header files for developing applications that use the %name
library.

The documentation for the C library is found in the utf8proc.h header file.
"utf8proc_map" is most likely the function you will be using for mapping UTF-8
strings, unless you want to allocate memory yourself.

%prep
%setup

%build
CFLAGS='%optflags' \
%make_build

%check
%make_build test/normtest test/graphemetest test/printproperty \
     test/charwidth test/normtest test/graphemetest test/charwidth

%install
%makeinstall_std prefix=%prefix includedir=%_includedir libdir=%_libdir
rm %buildroot%_libdir/libutf8proc.a

%files
%doc *.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Jan 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0 released

* Wed May 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Fri Apr 27 2018 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1
- 2.1.1: fixes a serious composition bug, thanks upstream for heads-up

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- initial build for ALT Linux Sisyphus (based on fedora spec)
