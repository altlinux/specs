# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/zip gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname skstream
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name skstream
%define version 0.3.9
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:           libskstream
Version:        0.3.9
Release:        alt1_5
Summary:        C++ I/O library for WorldForge clients/servers

Group:          Development/C++
License:        GPLv2+
URL:            http://worldforge.org/dev/eng/libraries/skstream
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2
Patch1:         skstream-0.3.6-gcc44.patch

BuildRequires:  cppunit-devel doxygen
Source44: import.info
Provides: skstream = %{version}-%{release}

%description
skstream is an iotream C++ socket library and is recommended for use as a
transport for Atlas-C++. It is capable of creating iostream-based socket
connections for both clients and servers.


%package devel
Summary:        Development files for skstream
Group:   Development/C++
Requires: %{name} = %{version}-%{release}
Provides: skstream-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use skstream.


%prep
%setup -n %{oldname}-%{version} -q
%patch1 -p0


%build
%configure
make %{?_smp_mflags}
make docs


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}-0.3.la

# Fix one file that gets installed incorrectly
mv $RPM_BUILD_ROOT%{_libdir}/%{oldname}-0.3/include/%{oldname}/*.h $RPM_BUILD_ROOT%{_includedir}/%{oldname}-0.3/%{oldname}

install -dm 755 $RPM_BUILD_ROOT%{_pkgdocdir}
cp -pR AUTHORS ChangeLog COPYING README README.FreeSockets TODO doc/* $RPM_BUILD_ROOT%{_pkgdocdir}

%check
# The tests hang on the koji builders so we need to skip them
# Run tests in debug mode so asserts won't be skipped
# sed -i -e 's/-DNDEBUG/-DDEBUG/' test/Makefile
# make %{?_smp_mflags} check || :

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/COPYING
%{_pkgdocdir}/README
%{_pkgdocdir}/README.FreeSockets
%{_pkgdocdir}/TODO
%{_libdir}/lib%{oldname}-0.3.so.*

%files devel
%{_pkgdocdir}/html
%{_pkgdocdir}/latex
%{_includedir}/%{oldname}-0.3
%{_libdir}/lib%{oldname}-0.3.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_2
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_4
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_2
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_1
- initial release by fcimport

