%define _unpackaged_files_terminate_build 1

Name: fortunes-kernelnewbies
Version: 1
Release: alt1

Summary: kernelnewbies excuses fortune
License: Public Domain
Group: Games/Other
URL: https://fortunes.cat-v.org/kernelnewbies/

Source:	kernelnewbies

BuildArch: noarch
Requires: fortune
BuildRequires: fortune

Conflicts: fortune-mod <= 1.99.1

%description
This is a set of kernelnewbies excuses.

%prep
cp -a %SOURCE0 .

%build
/usr/bin/strfile kernelnewbies

%install
install -d -m 755 %buildroot%_gamesdatadir/fortune
install -m 644 kernelnewbies %buildroot%_gamesdatadir/fortune/kernelnewbies
install -m 644 kernelnewbies.dat %buildroot%_gamesdatadir/fortune/kernelnewbies.dat

%files
%_gamesdatadir/fortune/*

%changelog
* Mon Feb 15 2021 Konstantin Rybakov <kastet@altlinux.org> 1-alt1
- Built for Sisyphus
