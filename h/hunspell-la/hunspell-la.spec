# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-la
Summary: Latin hunspell dictionaries
%define upstreamid 20110807
Version: 0.%{upstreamid}
Release: alt1_2
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/1141/2/dict-la_2011-08-07.oxt
URL: http://extensions.services.openoffice.org/project/dict-la
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Latin hunspell dictionaries.

%prep
%setup -q -c -n hunspell-la

%build
for i in README_extension_owner-la.txt la/README_la.txt la/COPYING*; do
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
cp -p la/la.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/la.dic
cp -p la/la.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/la.aff

%files
%doc README_extension_owner-la.txt la/README_la.txt la/COPYING_*
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110807-alt1_2
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110807-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100823-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100823-alt1_2
- import from Fedora by fcimport

