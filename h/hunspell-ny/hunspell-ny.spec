# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ny
Summary: Chichewa hunspell dictionaries
#Epoch: 1
Version: 0.01
Release: alt2_3
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/4052/0/hunspell-chichewa-ny-dict-%{version}.oxt
URL: http://extensions.services.openoffice.org/en/project/chicspell
License: GPLv3+
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Chichewa hunspell dictionaries.

%prep
%setup -q -c

%build
for i in dictionaries/README_ny_MW.txt; do
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
cp -p dictionaries/ny_MW.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc LICENSES-en.txt dictionaries/README_ny_MW.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- import from Fedora by fcimport

