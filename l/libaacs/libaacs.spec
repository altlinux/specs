Name: libaacs
Version: 0.4.0
Release: alt1
Summary: BD AACS library

Group: System/Libraries
License: LGPL
Url: http://bd.videolan.org/

Source: %name-%version-%release.tar

BuildRequires: flex libgcrypt-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libaacs development.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/aacs_info

%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Fri May 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Tue Oct 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- 0.2 released

* Wed May 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- initial

