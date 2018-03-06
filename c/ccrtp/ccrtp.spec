%def_disable static

Name: ccrtp
Version: 2.1.2
Release: alt1.2
%define sover 3
%define libccrtp libccrtp%sover
%define docdir %_docdir/%name-%version

Summary: Common C++ class framework for RTP/RTCP

License: GPL
Group: System/Libraries
Url: http://www.gnu.org/software/ccrtp/

Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 24 2014 (-bi)
# optimized out: elfutils libcloog-isl4 libgpg-error libgpg-error-devel libstdc++-devel makeinfo pkg-config python-base ruby ruby-stdlibs
#BuildRequires: doxygen gcc-c++ glibc-devel-static libgcrypt-devel rpm-build-ruby ucommon-devel
BuildRequires: doxygen gcc-c++ glibc-devel libgcrypt-devel ucommon-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.

%package devel
Summary: Header files for ccrtp library
Group: Development/C++
Conflicts: libccrtp-devel
%description devel
Header files for ccrtp library.

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %version-%release
%description devel-static
Common C++ devel static files

%package doc
Summary: Documentation for %name
Group: Development/C++
%description doc
Documentation for %name

%package -n %libccrtp
Summary: %name library
Group: System/Libraries
%description -n %libccrtp
%name library


%prep
%setup
%autoreconf

%build
%configure %{subst_enable static}
make

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%docdir
cp -a AUTHORS COPYING.addendum README doc/srcmodel* doc/html %buildroot%docdir

%files -n %libccrtp
%dir %docdir
%docdir/[A-Z]*
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%sover.*

%files devel
%_libdir/lib*.so
%_includedir/ccrtp
%_pkgconfigdir/*.pc

%files doc
%docdir/html
%docdir/srcmodel*
%_infodir/*.info*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sun Mar 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1.2
- NMU: autorebuild with ucommon-7.0.0

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1.1
- NMU: added BR: texinfo

* Mon Jun 15 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.2-alt1
- new version

* Sun Jun 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.9-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Oct 23 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.9-alt0.M70P.1
- built for M70P

* Wed Sep 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.9-alt1
- initial build
