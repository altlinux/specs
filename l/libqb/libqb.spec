# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/splint gcc-c++ pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%bcond_without check
%bcond_without syslog_tests

Name:           libqb
Version:        1.0.1
Release:        alt1_1
Summary:        An IPC library for high performance servers

Group:          System/Libraries
License:        LGPLv2+
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://github.com/ClusterLabs/libqb/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf-common automake-common libtool-common doxygen procps sysvinit-utils libcheck-devel
# https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires
BuildRequires:  gcc-common
Source44: import.info

%description
libqb provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%prep
%setup -q


## Make sure the timestamps are correct
#find . -exec touch \{\} \;

%build
./autogen.sh
%configure --disable-static \
           %{?with_syslog_tests:--enable-syslog-tests}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%files
%doc COPYING
%{_sbindir}/qb-blackbox
%{_libdir}/libqb.so.*
%{_mandir}/man8/qb-blackbox.8*

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version} pkg-config

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%doc README.markdown
%doc COPYING
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*

%changelog
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

