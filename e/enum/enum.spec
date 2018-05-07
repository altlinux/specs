# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: enum
Version: 1.1
Release: alt1_13
Summary: Seq- and jot-like enumerator

Group:   System/Base
License: BSD
URL:     https://fedorahosted.org/enum
Source0: https://fedorahosted.org/releases/e/n/enum/%{name}-%{version}.tar.bz2

BuildRequires: gcc
Source44: import.info

%description
Utility enum enumerates values (numbers) between two values, possibly
further adjusted by a step and/or a count, all given on the command line.
Before printing, values are passed through a formatter. Very fine control
over input interpretation and output is possible.


%prep
%setup -q


%build
%configure --disable-doc-rebuild
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check


%files
%doc COPYING ChangeLog
%_mandir/man1/enum.1*
%_bindir/enum


%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_9
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- rebuild with new radius-engine

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- initial release by fcimport

