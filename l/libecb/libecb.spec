Group: Development/Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global snapshot 20230911
# Do not create debuginfo sub-package because there is no binary executable
%global debug_package %{nil}
Name:       libecb
# Upstream version is a 32-bit hexadecimal number with an internal structure.
# See ECB_VERSION macro. RPM cannot order them correctly. A decimal encoding
# would work, but would be uggly. Just use 0.
Version:    0.%{snapshot}
Release:    alt1_1
Summary:    Compiler built-ins
License:    BSD-2-Clause OR GPL-2.0-or-later
URL:        http://software.schmorp.de/pkg/libecb.html
# Snapshot from CVS :pserver:anonymous@cvs.schmorp.de/schmorpforge libecb 
Source0:    %{name}-%{snapshot}.tar.xz
BuildRequires:  coreutils
BuildRequires:  perl-podlators
Source44: import.info

%description
This project delivers you many GCC built-ins, attributes and a number of
generally useful low-level functions, such as popcount, expect, prefetch,
noinline, assume, unreachable and so on.

This is a dummy package. All the useful files are delivered by %{name}-devel
package.


%package devel
Group: Development/C
Summary:    Compiler built-ins
# Packaging guidelines require header-only packages:
# to be architecture-specific, to deliver headers in -devel package, to
# provide -static symbol for reverse build-requires.
# Replace libecb package:
Provides:   libecb-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:   libecb = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:  libecb < 0.20150218

%description devel
This project delivers you many GCC built-ins, attributes and a number of
generally useful low-level functions, such as popcount, expect, prefetch,
noinline, assume, unreachable and so on.

%prep
%setup -q -n %{name}-%{snapshot}


%build
pod2man ecb.pod > ecb.3

%install
install -d %{buildroot}%{_includedir}
install -m 0644 -t %{buildroot}%{_includedir} *.h 
install -d %{buildroot}%{_mandir}/man3
install -m 0644 -t %{buildroot}%{_mandir}/man3 *.3

%files devel
%doc --no-dereference LICENSE
%doc Changes README
%{_includedir}/ecb.h
%{_mandir}/man3/ecb.*

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.20230911-alt1_1
- update to new release by fcimport

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 0.20211217-alt1_1
- update to new release by fcimport

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 0.20211021-alt1_1
- update to new release by fcimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.20200430-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.20190722-alt1_2
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.20181119-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20161208-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20161208-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.20161208-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20160209-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20150608-alt1_2
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.20150218-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.20141029-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.20121022-alt1_2
- initial fc import

