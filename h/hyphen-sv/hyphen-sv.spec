# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-sv
Summary: Swedish hyphenation rules
Version: 1.00.1
Release: alt1_13
Source: http://extensions.services.openoffice.org/files/1966/4/hyph_sv_SE.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/node/1968
License: LGPLv2+ or GPLv2+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Swedish hyphenation rules.

%prep
%setup -q -c -n hyphen-sv

%build
chmod -x *
for i in README_sv_SE.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sv_SE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s hyph_sv_SE.dic hyph_$lang.dic
done
popd

%files
%doc README_sv_SE.txt
%{_datadir}/hyphen/*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.00.1-alt1_6
- import by fcmass

