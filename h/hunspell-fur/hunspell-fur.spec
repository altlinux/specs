Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fur
Summary: Friulian hunspell dictionaries
%global upstreamid 20050912
Version: 0.%{upstreamid}
Release: alt2_29
Source: http://digilander.libero.it/paganf/coretors/myspell-fur-12092005.zip
URL: http://digilander.libero.it/paganf/coretors/dizionaris.html
License: GPL-2.0-or-later
BuildArch: noarch
Source44: import.info


%description
Friulian hunspell dictionaries.

%prep
%setup -q -n myspell-fur-12092005

%build
chmod -x *
for i in COPYING.txt LICENCE.txt LEIMI.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-15 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p fur_IT.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc COPYING.txt LEIMI.txt LICENCE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.20050912-alt2_29
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt1_5
- import from Fedora by fcimport

