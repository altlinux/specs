Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-fy
Summary: Frisian hunspell dictionaries
Version: 2.0.1
Release: alt2_10
Source: http://releases.mozilla.org/pub/mozilla.org/addons/5679/frysk_wurdboek-2.0.1-fx+tb+sm.xpi
URL: http://www.mozilla-nl.org/projecten/frysk
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Frisian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-fy

%build
for i in README-fy.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i | tr -d '\r' > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/fy.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/fy_NL.aff
cp -p dictionaries/fy.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/fy_NL.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
fy_NL_aliases="fy_DE"
for lang in $fy_NL_aliases; do
        ln -s fy_NL.aff $lang.aff
        ln -s fy_NL.dic $lang.dic
done
popd


%files
%doc README-fy.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- import from Fedora by fcimport

