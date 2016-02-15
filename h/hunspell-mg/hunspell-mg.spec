# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mg
Summary: Malagasy hunspell dictionaries
%define upstreamid 20050109
Version: 0.%{upstreamid}
Release: alt2_13
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/mg_MG.zip
Group: Text tools
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Malagasy hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mg

%build
for i in README_mg_MG.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mg_MG.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/plt.aff
cp -p mg_MG.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/plt.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
plt_aliases="mg"
for lang in $plt_aliases; do
        ln -s plt.aff $lang.aff
        ln -s plt.dic $lang.dic
done
popd

%files
%doc README_mg_MG.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt1_6
- import from Fedora by fcimport

