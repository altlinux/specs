Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-kn
Summary: Kannada hunspell dictionaries
Version: 1.0.3
Release: alt2_21
Source: https://downloads.sourceforge.net/project/aoo-extensions/2628/1/kannada.oxt
URL: https://extensions.openoffice.org/project/kannada
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Kannada hunspell dictionaries.

%prep
%setup -q -c -n hunspell-kn


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p kn_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_kn_IN.txt
%doc --no-dereference COPYING COPYING.MPL COPYING.GPL COPYING.LGPL
%{_datadir}/myspell/kn_IN.aff
%{_datadir}/myspell/kn_IN.dic

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_21
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_11
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_3
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- import from Fedora by fcimport

