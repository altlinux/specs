# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-br
Summary: Breton hunspell dictionaries
#Epoch: 1
Version: 0.8
Release: alt1_2
Group: Text tools
URL: http://www.drouizig.org/
Source: http://extensions.services.openoffice.org/e-files/2207/6/dict-br_0.8.oxt
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Breton hunspell dictionaries.

%prep
%setup -q -c -n hunspell-br-%{version}

%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/br_FR.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc LICENSES-en.txt package-description.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- import from Fedora by fcimport

