# BEGIN SourceDeps(oneline):
BuildRequires: libdict-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 15
%define libname libosip2_%{major}
%define libname_devel libosip2-devel

Summary:	Implementation of SIP - rfc3261
Name:		libosip2
Version: 	5.3.1
Release: 	alt1_1
License: 	LGPLv2+
Group:		System/Libraries
URL: 		https://savannah.gnu.org/projects/osip/
Source0:	https://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
Source44: import.info

%description
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
https://www.ietf.org/rfc/rfc3261.txt

%package -n	%{libname}
Summary:	Implementation of SIP - rfc2543
Group:		System/Libraries
Obsoletes:	libosip2 < %version
Obsoletes:	%{_lib}osip2_4 < %version
Conflicts:	libosip2_7 < %version

%description -n	%{libname}
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
https://www.ietf.org/rfc/rfc3261.txt

%package -n	%{libname_devel}
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname_devel}
Developments files for %{libname} (oSIP Library). Needed to build
apps such as linphone and siproxd.

%prep
%setup -q


%build
autoreconf -fi -Iscripts
%configure --disable-static
%make_build

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

# don't ship .a, .la
rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*
%{_mandir}/man1/*

%files -n %{libname_devel}
%{_libdir}/*.so
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.3.1-alt1_1
- update by mgaimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3
- new version

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.5.0-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.5.0-alt1
- 3.5.0

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.git.5a3da085.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1.git.5a3da085
- 3.4.0

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libosip2
  * postun_ldconfig for libosip2

* Mon Apr 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Fri Dec 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt3
- fixed build with new auto*

* Sat Oct 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt2
- drop MD5 functions (close #13086)

* Wed Aug 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Wed Jan 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1-alt1
- 3.0.1:
  + Fix memory leaks (not likely to happen).
  + Fix buffer overrun in url.

* Sat Sep 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Jun 29 2004 Gor <vg@altlinux.ru> 2.0.8-alt1
- try to package for Sisyphus

