# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-mi
Summary: Maori hyphenation rules
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: alt1_5
Source: http://packages.papakupu.maori.nz/hunspell-hyphen/hunspell-hyphen-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Text tools
URL: http://papakupu.maori.nz/
License: GPLv3+
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Maori hyphenation rules.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_mi_NZ.dic

%files
%doc mi.LICENSE mi.README
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_4
- import by fcmass

