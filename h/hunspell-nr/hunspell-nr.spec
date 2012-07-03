# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-nr
Summary: Southern Ndebele hunspell dictionaries
%define upstreamid 20091030
Version: 0.%{upstreamid}
Release: alt2_3
Source: http://extensions.services.openoffice.org/e-files/3141/0/dict-nr_ZA-2009.10.30.oxt
Group: Text tools
URL: http://www.translate.org.za/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Southern Ndebele hunspell dictionaries.

%prep
%setup -q -c -n hunspell-nr

%build
for i in README-nr_ZA.txt release-notes-nr_ZA.txt package-description.txt; do
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README-nr_ZA.txt release-notes-nr_ZA.txt package-description.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091030-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091030-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091030-alt1_2
- import from Fedora by fcimport

