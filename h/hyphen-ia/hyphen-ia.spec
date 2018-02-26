# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ia
Summary: Interlingua hyphenation rules
%define upstreamid 20050628
Version: 0.%{upstreamid}
Release: alt1_4
Source: http://www.ctan.org/get/language/hyphenation/iahyphen.tex
Group: Text tools
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/iahyphen.html
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-ia-cleantex.patch
Source44: import.info

%description
Interlingua hyphenation rules.

%prep
%setup -T -q -c -n hyphen-ia
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1
echo "Created with substring.pl by substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1" > README
echo "---" >> README
head -n 25 iahyphen.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ia.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_3
- import by fcmass

