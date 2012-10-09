
%define msn_sover 0.3
%define beta %nil
Name: libmsn
Version: 4.2.1
Release: alt2

Group: Development/C++
Summary: Reusable, open-source and fully documented library for MSN
Url: http://sourceforge.net/projects/libmsn
License: GPLv2+

Source: %name-%version%beta.tar.bz2
Patch1: alt-gcc47.patch

BuildRequires: cmake gcc-c++ libcom_err-devel libssl-devel
BuildRequires: kde-common-devel

%description
Libmsn is a reusable, open-source, fully documented library for
connecting to Microsoft's MSN Messenger service.

%package -n libmsn%msn_sover
Summary: %name library
Group: System/Libraries
%description -n libmsn%msn_sover
%name library

%package test
Summary: Connection test utility
Group: Development/C++
%description test
Connection test utility.

%package devel
Summary: Devel stuff for %name
Group: Development/C++
Requires: libmsn%msn_sover = %version-%release
%description devel
Files needed to build applications based on %name.


%prep
%setup -q -n %name-%version%beta
%patch1 -p1

%build
%Kbuild

%install
%Kinstall


%files -n libmsn%msn_sover
%_libdir/libmsn.so.%{msn_sover}*

%files test
%_bindir/*

%files devel
%doc doc/html doc/OVERVIEW README THANKS TODO
%_libdir/pkgconfig/*
%_includedir/msn
%_libdir/libmsn.so

%changelog
* Tue Oct 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt2
- fix to build with gcc 4.7

* Tue Aug 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt0.M60P.1
- built for M60P

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt2
- rebuilt with new ssl

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt0.M51.1
- build for M51

* Fri Apr 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.0-alt1
- 4.0 release

* Mon Jan 19 2009 Sergey V Turchin <zerg at altlinux dot org> 4.0-alt0.1
- 4.0-beta2
- initial specfile
