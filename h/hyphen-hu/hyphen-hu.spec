# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-hu
Summary: Hungarian hyphenation rules
%define upstreamid 20090612
Version: 0.%{upstreamid}
Release: alt1_6
Source: http://download.github.com/nagybence-huhyphn-aa3fc85.tar.gz
Group: Text tools
URL: http://www.tipogral.hu/
License: GPLv2+
BuildArch: noarch
#BuildRequires: eruby, texlive
Requires: libhyphen
Source44: import.info

%description
Hungarian hyphenation rules.

%prep
%setup -q -n nagybence-huhyphn-aa3fc85
#disable for now as built-in patgen has too small a limit to rebuild
#ln -sf /usr/bin/patgen patgen
#touch words/*.txt

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hu.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hu_HR.dic

%files
%doc gpl.txt README doc/huhyphn.pdf
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090612-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090612-alt1_5
- import by fcmass

