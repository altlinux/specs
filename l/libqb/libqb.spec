# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen2man gcc-c++ pkgconfig(libsystemd) python3-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with check

Name:           libqb
Version:        2.0.6
Release:        alt1_4
Summary:        Library providing high performance logging, tracing, ipc, and poll

License:        LGPLv2+
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://github.com/ClusterLabs/libqb/releases/download/v%{version}/%{name}-%{version}.tar.xz

Patch0: connretry-recv.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  libcheck-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  procps
# for ipc.test only (part of check scriptlet)
BuildRequires:  pkgconfig(glib-2.0)
# git-style patch application
BuildRequires:  git-core
# For doxygen2man
BuildRequires:  libxml2-devel
Source44: import.info

%description
A "Quite Boring" library that provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%package -n libqb100
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libqb100
A "Quite Boring" library that provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

This package contains the shared library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .connretry-recv.patch

%build
./autogen.sh
%configure --disable-static
%{make_build}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*



%files
%{_sbindir}/qb-blackbox
%{_mandir}/man8/qb-blackbox.8*

%files -n libqb100
%doc --no-dereference COPYING
%_libdir/libqb.so.100
%_libdir/libqb.so.100.*

%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       libqb100 = %EVR
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*


%package -n     doxygen2man
Group: System/Libraries
Summary:        Program to create nicely-formatted man pages from Doxygen XML files
Requires:       libqb100 = %EVR


%description -n doxygen2man
This package contains a program to create nicely-formatted man pages from Doxygen XML files

%files -n       doxygen2man
%{_bindir}/doxygen2man
%{_mandir}/man1/doxygen2man.1*


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_4
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_1
- update to new release by fcimport

* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 2.0.4-alt1_2
- update to new release by fcimport

* Tue Nov 30 2021 Igor Vlasenko <viy@altlinux.org> 2.0.4-alt1_1
- update to new release by fcimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_1
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_2
- update to new release by fcimport

* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- new version

* Wed May 06 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.6-alt1
- 1.0.6

* Fri Apr 17 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5
- update to new release by fcimport

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_2
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_11
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_10
- update to new release by fcimport

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.17.2-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.17.2-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.17.1-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.17.1-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.17.0-alt1_3
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.17.0-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt2_2
- update to new release by fcimport

* Thu Apr 04 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.14.4-alt2
- spec cleanup
- define _localstatedir and add --with-socket-dir=%_runtimedir

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt1_2
- update to new release by fcimport

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt1_1
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.14.3-alt1_2
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_2
- update to new release by fcimport

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_1
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.14.1-alt1_1
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_1
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_2
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1
- initial import by fcimport

