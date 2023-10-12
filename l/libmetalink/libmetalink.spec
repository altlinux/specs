Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 32

Name:           libmetalink
Version:        0.1.3
%global so_version 3
Release:        alt1_%autorelease
Summary:        Metalink library written in C

# SPDX
License:        MIT
URL:            https://github.com/metalink-dev/libmetalink
Source:         https://github.com/metalink-dev/libmetalink/archive/release-%{version}/libmetalink-release-%{version}.tar.gz

# NULL ptr deref in initial_state_start_fun
# https://bugs.launchpad.net/libmetalink/+bug/1888672
Patch0:          https://bugs.launchpad.net/libmetalink/+bug/1888672/+attachment/5395227/+files/libmetalink-0.1.3-ns_uri.patch
# Fix few issues found by the Coverity static analysis tool
# https://bugs.launchpad.net/libmetalink/+bug/1784359
# https://github.com/metalink-dev/libmetalink/pull/2
Patch1:          https://bugs.launchpad.net/libmetalink/+bug/1784359/+attachment/5169495/+files/0001-fix-covscan-issues.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc

BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(cunit)
# Required for AM_PATH_XML2 m4 macro so we can a.'autoreconfa.'; however, expat is
# used preferentially where available.
BuildRequires:  libxml2-devel
Source44: import.info

%description
libmetalink is a Metalink C library. It adds Metalink functionality such as
parsing Metalink XML files to programs written in C.


%package        devel
Group: Development/Other
Summary:        Files needed for developing with libmetalink

Requires:       libmetalink = %{version}-%{release}

%description    devel
Files needed for building applications with libmetalink.


%prep
%setup -q -n libmetalink-release-%{version}
%patch0 -p1
%patch1 -p1



%build
autoreconf --force --install --verbose
%configure --disable-static
%make_build


%check
%make_build check


%install
%makeinstall_std
find '%{buildroot}' -type f -name '*la' -print -delete


%files
%doc --no-dereference COPYING
%doc AUTHORS
%doc ChangeLog
%doc NEWS
%doc README
%{_libdir}/libmetalink.so.%{so_version}
%{_libdir}/libmetalink.so.%{so_version}.*


%files devel
%{_includedir}/metalink/
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/libmetalink.pc
%{_mandir}/man3/metalink*.3*


%changelog
* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt1_32
- update to new release by fcimport

* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt1_24
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_13
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_8
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_4
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt3_7
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_6
- initial import by fcimport

