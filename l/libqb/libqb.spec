# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/splint gcc-c++ libsocket pkgconfig(check) pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libqb
Version:        0.17.2
Release:        alt1_2
Summary:        An IPC library for high performance servers

Group:          System/Libraries
License:        LGPLv2+
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://fedorahosted.org/releases/q/u/quarterback/%{name}-%{version}.tar.xz
Patch1:         https://github.com/ClusterLabs/libqb/commit/aec4cde4312ada559888371554b0ae862cf91b9a.patch

BuildRequires:  autoconf automake libtool doxygen procps libcheck-devel
Source44: import.info

%description
libqb provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%prep
%setup -q
%patch1 -p1

# Make sure the timestamps are correct
find . -exec touch \{\} \;

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%files
%doc COPYING
%{_sbindir}/qb-blackbox
%{_libdir}/libqb.so.*

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version} pkgconfig

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
%{_mandir}/man8/qb-blackbox.8*

%changelog
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

