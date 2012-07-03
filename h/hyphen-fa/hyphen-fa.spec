# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-fa
Summary: Farsi hyphenation rules
%define upstreamid 20081119
Version: 0.%{upstreamid}
Release: alt1_4
Source: http://www.ctan.org/get/language/hyphenation/fahyph.zip
Group: Text tools
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/fahyph.html
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-fa-cleantex.patch
Source44: import.info

%description
Farsi hyphenation rules.

%prep
%setup -q -n fahyph
%patch0 -p1 -b .clean

%build
substrings.pl fahyph.tex hyph_fa_IR.dic UTF-8
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fa_IR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20081119-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081119-alt1_3
- import by fcmass

