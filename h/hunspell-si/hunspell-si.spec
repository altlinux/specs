# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: alt2_4
Source: http://www.sandaru1.com/wp-content/uploads/2009/08/si-LK.tar.gz
Group: Text tools
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
License: GPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Sinhala hunspell dictionaries.

%prep
%setup -q -c -n hunspell-si

%build
#nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/si-LK.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.aff
cp -p dictionaries/si-LK.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.dic

%files
%doc LICENSE README
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- import from Fedora by fcimport

