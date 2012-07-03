# vim: set ft=spec: -*- rpm-spec -*-

Name: fortunes-politicians
Version: 20050616
Release: alt2

Summary: Politicians quotes
Group: Games/Other
License: distributable

BuildArch: noarch

Source: politicians.bz2

PreReq: fortune-mod >= 1.0-ipl33mdk

# Automatically added by buildreq on Mon Jun 27 2005
BuildRequires: fortune-mod

%description
Politicians quotes.

%prep
%__bzip2 -d %SOURCE0 -c > politicians

%build
/usr/bin/strfile politicians

%install
%__mkdir -p %buildroot%_gamesdatadir/fortune
%__install -m 0644 politicians* %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*

%changelog
* Mon Jul 04 2005 Kirill A. Shutemov <kas@altlinux.ru> 20050616-alt2
- #7250 fixed

* Thu Jun 16 2005 Kirill A. Shutemov <kas@altlinux.ru> 20050616-alt1
- first build
