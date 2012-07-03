# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-vi
Summary: Vietnamese hunspell dictionaries
%define upstreamid 20080604
Version: 0.%{upstreamid}
Release: alt2_5
Source: http://hunspell-spellcheck-vi.googlecode.com/files/vi_VN.zip
Group: Text tools
URL: http://code.google.com/p/hunspell-spellcheck-vi
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Vietnamese hunspell dictionaries.

%prep
%setup -q -c -n hunspell-vi

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_vi_VN.txt Copyright
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080604-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080604-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080604-alt1_4
- import from Fedora by fcimport

