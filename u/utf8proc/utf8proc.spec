Name: utf8proc
Version: 2.10.0
Release: alt1

Summary: Library for processing UTF-8 encoded Unicode strings
License: BSD
Group: System/Libraries
Url: https://julialang.org/utf8proc/

Source: %name-%version.tar

%package -n libutf8proc3
Summary: Library for processing UTF-8 encoded Unicode strings
Group: System/Libraries

%package -n libutf8proc-devel
Summary: Header files, libraries and development docs for utf8proc
Group: Development/C

%define desc\
utf8proc is a library for processing UTF-8 encoded Unicode strings.\
Some features are Unicode normalization, stripping of default ignorable\
characters, case folding and detection of grapheme cluster boundaries.

%description %desc

%description -n libutf8proc3 %desc
This package contains the utf8proc shared library only.

%description -n libutf8proc-devel %desc
Contains header files for developing applications that use the utf8proc
library.

%prep
%setup

%build
CFLAGS='%optflags' \
%make_build

%install
%makeinstall_std prefix=%prefix includedir=%_includedir libdir=%_libdir
rm %buildroot%_libdir/libutf8proc.a

%files -n libutf8proc3
%_libdir/*.so.*

%files -n libutf8proc-devel
%doc LICENSE* NEWS* README*
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jan 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.10.0-alt1
- 2.10.0 released

* Wed Jun 19 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.0-alt1
- 2.9.0 released

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
