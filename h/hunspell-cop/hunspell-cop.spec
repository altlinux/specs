# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-cop
Summary: Coptic hunspell dictionaries
Version: 0.3
Release: alt2_2
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/793/2/dict-cop_EG_v03.oxt
URL: http://www.moheb.de/coptic_oo.html
License: GPLv3+
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Coptic hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p cop_EG-Bohairic/cop_EG.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README.txt license-gpl.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_1
- import from Fedora by fcimport

