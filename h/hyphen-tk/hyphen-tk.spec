# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-tk
Summary: Turkmen hyphenation rules
%define upstreamid 20110620
Version: 0.%{upstreamid}
Release: alt1_2
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex?view=co
Source: hyph-tk.tex
Group: Text tools
URL: http://tug.org/tex-hyphen
License: Public Domain
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-tk-cleantex.patch
Source44: import.info

%description
Turkmen hyphenation rules.

%prep
%setup -T -q -c -n hyphen-tk
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 15 hyph-tk.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_tk_TM.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/hyph_tk_TM.dic

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass

