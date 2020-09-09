# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major	0
%define	libname	libnut%{major}
%define	devname	libnut-devel

Name:		libnut
%define	svnrev	675
Version:	0.0.%{svnrev}
Release:	alt1_10
Url:		http://wiki.multimedia.cx/index.php?title=NUT
License:	MIT
Group:		System/Libraries
Summary:	NUT Multimedia Container Library
# svn checkout svn://svn.mplayerhq.hu/nut/src/trunk libnut ; tar -Jcf libnut-r$(LC_ALL=C svn info libnut | sed -n 's/Revision: //p').tar.xz libnut
Source0:	%{name}-r%{svnrev}.tar.xz
Patch0:		libnut-libdir.patch
Patch1:		libnut-shared.patch
Patch2:		libnut-r675-ldflags.patch
Source44: import.info

%description
Library for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%package -n	%{libname}
Group:		System/Libraries
Summary:	NUT Multimedia Container Library
Conflicts: libnut < 0.0.675
Obsoletes: libnut < 0.0.675
Provides: libnut = %version

%description -n	%{libname}
Library for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%package -n	%{devname}
Group:		Development/C
Summary:	Development files for NUT Multimedia Container Library
Requires:	%{libname} = %{version}-%{release}
# package was not libified a long long time ago and an obsolete was forgotten
# at the time, causing file conflicts on upgrade (Anssi 03/2012):

%description -n	%{devname}
This package contains development files for the NUT Multimedia Container
Library.

%package	utils
Group:		Video
Summary:	NUT Multimedia Container Utilites

%description	utils
Utilities for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%prep
%setup -q -n %{name}
%patch0 -p0 -b .libdir~
%patch1 -p1 -b .shared~
%patch2 -p1 -b .ldflags~

%build

%make_build prefix=%{_prefix} libdir=%{_libdir}

%install
%makeinstall

%files utils
%{_bindir}/*

%files -n %{libname}
%doc COPYING README
%{_libdir}/libnut.so.%{major}*

%files -n %{devname}
%{_includedir}/libnut.h
%{_libdir}/libnut.so
%{_libdir}/libnut.a





%changelog
* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.675-alt1_10
- fixed build

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.675-alt1_9
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0-alt0.505.1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.505.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnut
  * postun_ldconfig for libnut

* Fri Aug 17 2007 Led <led@altlinux.ru> 0.0-alt0.505.1
- new SVN revision (505)
- fixed License
- updated %name-svn-r505-soname.patch
- added %name-svn-r505-makefile.patch
- added nutparse to %name-utils

* Mon Mar 12 2007 Led <led@altlinux.ru> 0.0-alt0.282.2
- added %name-svn-r282-soname.patch
- enabled build shared lib

* Mon Mar 12 2007 Led <led@altlinux.ru> 0.0-alt0.282.1
- new SVN revision (282)

* Wed Jan 31 2007 Led <led@altlinux.ru> 0.0-alt0.279.1
- new SVN revision (279)

* Mon Jan 29 2007 Led <led@altlinux.ru> 0.0-alt0.276.1
- new SVN revision (276)

* Mon Dec 25 2006 Led <led@altlinux.ru> 0.0-alt0.274.1
- new SVN revision (274)

* Mon Nov 27 2006 Led <led@altlinux.ru> 0.0-alt0.266.1
- new SVN revision (266)

* Thu Nov 21 2006 Led <led@altlinux.ru> 0.0-alt0.258.1
- new SVN revision (258)
- fixed %%install (for x86_64)

* Mon Nov 20 2006 Led <led@altlinux.ru> 0.0-alt0.255.1
- new SVN revision (255)
- renamed package nut-utils to %name-utils

* Fri Nov 17 2006 Led <led@altlinux.ru> 0.0-alt0.223.1
- new SVN revision (223)
- fixed %%install

* Mon Nov 13 2006 Led <led@altlinux.ru> 0.0-alt0.200.1
- new SVN revision (200)

* Fri Nov 10 2006 Led <led@altlinux.ru> 0.0-alt0.198.1
- new SVN revision (198)

* Thu Oct 19 2006 Led <led@altlinux.ru> 0.0-alt0.158.1
- initial build
