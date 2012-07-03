# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-hil
Summary: Hiligaynon hunspell dictionaries
#Epoch: 1
Version: 0.14
Release: alt2_3
Group: Text tools
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://extensions.services.openoffice.org/project/hunspell-hil
License: GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Hiligaynon hunspell dictionaries.

%prep
%setup -q -c

%build
for i in dictionaries/README_hil_PH.txt; do
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
cp -p dictionaries/hil_PH.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc LICENSES-en.txt dictionaries/README_hil_PH.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- import from Fedora by fcimport

