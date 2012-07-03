# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mr
Summary: Marathi hunspell dictionaries
Version: 20060920 
Release: alt2_9
Source: http://ftp.freepark.org/OpenOffice.org/contrib/dictionaries/mr_IN.zip
Patch0: hunspell-mr-get-rid-of-broken-line.patch 
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Marathi hunspell dictionaries.

%prep
%setup -q -c -n mr-IN
%patch0 -p1

%build
#nothing to do here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mr_IN.dic mr_IN.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_mr_IN.txt LICENCE
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20060920-alt2_9
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20060920-alt2_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20060920-alt2_7
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20060920-alt1_7
- import from Fedora by fcimport

