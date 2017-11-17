Epoch: 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 1
%define libname libmpd%{major}
%define develname libmpd-devel

Summary:	Music Player Daemon Library
Name:		libmpd
Version:	11.8.17
Release:	alt1_8
License:	GPLv2+
Group:		System/Libraries
Url:		http://sarine.nl/libmpd
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0) >= 2.16
Source44: import.info

%description
Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package -n %{libname}
Summary:	Music Player Daemon Library
Group:		System/Libraries

%description -n %{libname}
Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package -n %{develname}
Summary:	Header files for developing programs with libmpd
Requires:	%{libname} = %{?epoch:%epoch:}%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Group:		Development/Other

%description -n %{develname}
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
%setup -q

%build
# _XOPEN_SOURCE=700 is to get strndup()
%configure \
    CPPFLAGS=-D_XOPEN_SOURCE=700 \
	--disable-static

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/%{name}.la

%files -n %{libname}
%{_libdir}/libmpd.so.%{major}
%{_libdir}/libmpd.so.%{major}.*

%files -n %{develname}
%doc ChangeLog README
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd-1.0


%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:11.8.17-alt1_8
- restored as import

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.8.90-alt1.git20130319
- Version 11.8.90

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.19.0-alt3.qa1
- NMU: rebuilt for updated dependencies.

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.19.0-alt3
- Disabled %libname-devel-static.
- Rebuilt for debuginfo.

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19.0-alt2
- Rebuilt for soname set-versions

* Sun Sep 20 2009 Alexey Rusakov <ktirf@altlinux.org> 0.19.0-alt1
- 0.19.0 release

* Tue Sep 01 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.100-alt1
- 0.19 RC (updated from git)

* Tue Jul 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt2
- fixed a wrong macro for a buffer size passed to snprintf

* Thu Mar 12 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- 0.18.0
- new Packager

* Thu Jan 08 2009 Led <led@altlinux.ru> 0.17.0-alt1
- 0.17.0
- cleaned up spec

* Wed Nov 12 2008 Led <led@altlinux.ru> 0.16.5-alt0.1
- 0.16.5 beta1

* Sun Oct 19 2008 Led <led@altlinux.ru> 0.16.1-alt2
- updated from upstream SCM for some fixes

* Sat Oct 04 2008 Led <led@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Fri Oct 03 2008 Led <led@altlinux.ru> 0.16.0-alt1
- 0.16.0
- fixed License
- fixed Group
- fixed URL
- cleaned up BuildRequires
- cleaned up spec
- added doc package

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.0-alt1
-  new version.

* Tue Jun 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14.0-alt1
- new version (0.14.0)
- updated Url and Source links
- removed unneeded buildreq of gcc-c++
- pass --disable-static to configure script.
- updated description and summary

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.5rev4832-alt1
-  initial build for ALTLinux Sisyphus.
