# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-nso
Summary: Northern Sotho hunspell dictionaries
%define upstreamid 20091201
Version: 0.%{upstreamid}
Release: alt2_3
Source: http://extensions.services.openoffice.org/files/3139/1/dict-ns_ZA-2009.12.01.oxt
Group: Text tools
URL: http://www.translate.org.za/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Northern Sotho hunspell dictionaries.

%prep
%setup -q -c -n hunspell-nso

%build
for i in README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ns_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.dic
cp -p ns_ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nso_ZA.aff

%files
%doc README-ns_ZA.txt package-description.txt release-notes-ns_ZA.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091201-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091201-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091201-alt1_2
- import from Fedora by fcimport

