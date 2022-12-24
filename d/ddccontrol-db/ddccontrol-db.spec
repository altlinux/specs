Group: System/Base
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             ddccontrol-db
URL:              https://github.com/ddccontrol/ddccontrol-db
Version:          20220829
Release:          alt1_1
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
License:          GPLv2+
Summary:          DDC/CI control database for ddccontrol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# use autopoint instead of gettextize that is interactive tool
BuildRequires:    gettext gettext-tools gettext-tools libasprintf-devel, libtool, intltool, perl(XML/Parser.pm)
BuildArch:        noarch
Source44: import.info
Patch33: ddccontrol-db-0.4.2-russian.patch
Conflicts: ddccontrol < 0.4.2-alt15

%description
DDC/CU control database for DDCcontrol.

%prep
%setup -q

./autogen.sh
%patch33 -p2

%build
%configure
%make_build

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/%{name}

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 20220829-alt1_1
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 20220629-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 20220414-alt1_1
- update to new release by fcimport

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20220119-alt1_1
- update to new release by fcimport

* Fri Oct 15 2021 Igor Vlasenko <viy@altlinux.org> 20210812-alt1_1
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 20210804-alt1_1
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 20210505-alt1_1
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 20201221-alt1_1
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 20190825-alt1_1
- update to new release by fcimport

* Sat Jun 09 2018 Igor Vlasenko <viy@altlinux.ru> 20180602-alt1_1
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 20171217-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20170716-alt1_2
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 20170716-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_9.20120904gite8cc385a
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_8.20120904gite8cc385a
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_7.20120904gite8cc385a
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_6.20120904gite8cc385a
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_5.20120904gite8cc385a
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_4.20120904git%(echo e8cc385a6321e7c99783150001193ec6e9e0c436 | cut -c -8)
- update to new release by fcimport

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_3.20120904gite8cc385a
- fc import for more frequent updates

