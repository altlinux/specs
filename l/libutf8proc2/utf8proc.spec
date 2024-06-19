Name: libutf8proc2
Version: 2.8.0
Release: alt2

Summary: Library for processing UTF-8 encoded Unicode strings
License: BSD
Group: System/Legacy libraries

Url: http://julialang.org/utf8proc/
Source: https://github.com/JuliaLang/utf8proc/archive/v%version.tar.gz#/%name-%version.tar.gz

%package -n utf8proc
Summary: Library for processing UTF-8 encoded Unicode strings
Group: System/Legacy libraries

%define desc\
utf8proc is a library for processing UTF-8 encoded Unicode strings.\
Some features are Unicode normalization, stripping of default ignorable\
characters, case folding and detection of grapheme cluster boundaries.\
The currently supported Unicode version is 14.

%description %desc

%description -n utf8proc %desc
This package only contains the shared library.

%prep
%setup

%build
CFLAGS='%optflags' \
%make_build

%install
%makeinstall_std prefix=%prefix includedir=%_includedir libdir=%_libdir
rm %buildroot%_libdir/libutf8proc.a

%files -n utf8proc
%_libdir/*.so.*

%changelog
* Wed Jun 19 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.0-alt2
- rebuilt as legacy shared library

* Tue Jan 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0 released

* Wed May 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Fri Apr 27 2018 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1
- 2.1.1: fixes a serious composition bug, thanks upstream for heads-up

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- initial build for ALT Linux Sisyphus (based on fedora spec)
