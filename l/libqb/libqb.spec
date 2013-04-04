Name: libqb
Version: 0.14.4
Release: alt2
Summary: An IPC library for high performance servers

Group: System/Libraries
License: LGPLv2+
Url: http://www.libqb.org
Source0: https://fedorahosted.org/releases/q/u/quarterback/%name-%version.tar.xz
Source44: import.info

BuildRequires: /proc doxygen procps libcheck-devel gcc-c++

%define _localstatedir %_var

%description
libqb provides high performance client server reusable features.
Initially these are IPC and poll.

%prep
%setup

%build
%autoreconf
%configure --disable-static --with-socket-dir=%_runtimedir
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc COPYING
%_sbindir/qb-blackbox
%_libdir/libqb.so.*

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%files devel
%doc COPYING README.markdown
%_includedir/qb/
%_libdir/libqb.so
%_libdir/pkgconfig/libqb.pc
%_mandir/man3/qb*3*
%_mandir/man8/qb-blackbox.8*

%changelog
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

