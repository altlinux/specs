Group: Text tools
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-wa
Summary: Walloon hunspell dictionaries
Version: 0.4.17
Release: alt1_22
Source0: http://chanae.walon.org/walon/aspell-wa-%{version}.tar.bz2
URL: http://chanae.walon.org/walon/aspell.php
License: LGPL-2.1-or-later
BuildArch: noarch
Patch0: hunspell-wa-0.4.15-buildfix.patch
Source44: import.info



%description
Walloon hunspell dictionaries.

%prep
%setup -q -n aspell-wa-%{version}
%patch0 -p1 -b .buildfix

%build
make myspell
for i in TODO README; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p wa.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/wa_BE.dic
cp -p wa.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/wa_BE.aff


%files
%doc README LGPL ChangeLog TODO
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.4.17-alt1_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_7
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_5
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_2
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.17-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt1_5
- import from Fedora by fcimport

