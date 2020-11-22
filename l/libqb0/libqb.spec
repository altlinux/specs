%define oldname libqb
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/splint gcc-c++ python-devel
# END SourceDeps(oneline)
Group: System/Legacy libraries
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without check

Name:           libqb0
Version:        1.0.6
Release:        alt2
Summary:        Library providing high performance logging, tracing, ipc, and poll

License:        LGPLv2+
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://github.com/ClusterLabs/libqb/releases/download/v%{version}/%{oldname}-%{version}.tar.xz

BuildRequires:  autoconf automake libtool
BuildRequires:  libcheck-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  procps
# for ipc.test only (part of check scriptlet)
BuildRequires:  pkgconfig(glib-2.0)
# git-style patch application
BuildRequires:  git-core
Source44: import.info
Conflicts: libqb < 1.0.6-alt2
Obsoletes: libqb < 1.0.6-alt2

%description
libqb provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%prep
%setup -n %{oldname}-%{version} -q # for when patches around

%build
./autogen.sh
%configure --disable-static
%{make_build}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*



%files
%doc --no-dereference COPYING
%{_libdir}/libqb.so.*
#%{_sbindir}/qb-blackbox
#%{_mandir}/man8/qb-blackbox.8*

%if 0
%package        devel
Group: Development/Other
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%files          devel
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*
%endif

%changelog
* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2
- compat library

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

