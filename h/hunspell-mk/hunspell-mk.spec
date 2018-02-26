# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mk
Summary: Macedonian hunspell dictionaries
%define upstreamid 20051126
Version: 0.%{upstreamid}
Release: alt2_5
Source: http://mk.openoffice.org/files/documents/215/3053/mk_MK.zip
Group: Text tools
URL: http://mk.openoffice.org
License: GPL+
BuildArch: noarch
Patch0: hunspell-mk-iconv.patch

Requires: hunspell
Source44: import.info

%description
Macedonian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mk
#change encoding name to use the name that iconv knows this under
%patch0 -p1 -b .iconv.patch

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_mk_MK.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt1_4
- import from Fedora by fcimport

