Name: libclucene
Version: 0.9.21
Release: alt3

Summary: CLucene is a C++ port of Lucene.
License: LGPL
Group: System/Libraries

URL: http://clucene.sf.net
Source0: clucene-core-%version.tar

# Automatically added by buildreq on Fri Sep 23 2011
BuildRequires: doxygen gcc-c++

%description
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.

%package devel
Summary: Development library and headers files fo CLucene
Group: Development/C++
Requires: %name = %version-%release

%description devel
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.

%prep
%setup -q -n clucene-core-%version

%build
%configure \
    --enable-multithreading \
    --disable-static

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README
%_libdir/%name.so.*

%files -n %name-devel
%dir %_includedir/CLucene
%dir %_libdir/CLucene
%_includedir/CLucene/*
%_includedir/CLucene.h
%_libdir/CLucene/clucene-config.h
%_libdir/%name.so

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.9.21-alt3
- rebuilt for debuginfo
- disabled static libraries

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.21-alt2
- rebuilt

* Fri Jan 29 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.21-alt0.M51.1
- built for M51

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.21-alt1
- 0.9.21b

* Tue Oct 23 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9.20-alt1
- new version

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9.16a-alt3
- fix 10497

* Sun Dec 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.9.16a-alt2
- remove obsolete configure parameter --disable-ucs2
- remove wrong configure parameter --disable-asci (bug 10388)

* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.9.16a-alt1
- new version

* Tue Sep 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.9.15-alt1
- new version

* Sun Jan 15 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.9.10-alt2
- cleanup specs

* Fri Dec 23 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.9.10-alt1
- initial release for ALTLinux


