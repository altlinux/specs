# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-sa
Summary: Sanskrit hyphenation rules
%define upstreamid 20110915
Version: 0.%{upstreamid}
Release: alt1_2
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex?view=co
Source: hyph-sa.tex
Group: Text tools
URL: http://tug.org/tex-hyphen
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-sa-cleantex.patch
Source44: import.info

%description
Sanskrit hyphenation rules.

%prep
%setup -T -q -c -n hyphen-sa
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 17 hyph-sa.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sa_IN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/hyph_sa_IN.dic

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110915-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110915-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass

