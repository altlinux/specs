%define _unpackaged_files_terminate_build 1

Name: fortunes-bofh
Version: 1.2
Release: alt2

Summary: BOFH excuses fortune
License: Public Domain
Group: Games/Other
URL: http://www.cs.wisc.edu/~ballard/bofh

#http://pages.cs.wisc.edu/~ballard/bofh/excuses
Source:	excuses

BuildArch: noarch
Requires: fortune
BuildRequires: fortune

Conflicts: fortune-mod <= 1.99.1

%description
This is a set of BOFH-style excuses.

%prep
cp -a %SOURCE0 .

%build
perl -ni -e 'print "BOFH excuse #" . ++$i . ":\n\n$_%\n"' excuses
/usr/bin/strfile excuses

%install
install -d -m 755 %buildroot%_gamesdatadir/fortune
install -m 644 excuses %buildroot%_gamesdatadir/fortune/bofh-excuses
install -m 644 excuses.dat %buildroot%_gamesdatadir/fortune/bofh-excuses.dat

%files
%_gamesdatadir/fortune/*

%changelog
* Tue Feb 16 2021 Konstantin Rybakov <kastet@altlinux.org> 1.2-alt2
- Built for Sisyphus

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6
- converted for ALT Linux by srpmconvert tools

