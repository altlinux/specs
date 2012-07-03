# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-hsb
Summary: Upper Sorbian hyphenation rules
%define upstreamid 20110620
Version: 0.%{upstreamid}
Release: alt1_2
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex?view=co
Source0: hyph-hsb.tex
Group: Text tools
URL: http://tug.org/tex-hyphen
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-hsb-cleantex.patch
Source44: import.info

%description
Upper Sorbian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-hsb
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8
echo "created with substring.pl by substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8" > README
echo "---" >> README
head -n 70 hyph-hsb.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hsb_DE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass

