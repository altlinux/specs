# vim: set ft=spec: -*- rpm-spec -*-
%define _fname taow

Name: fortunes-%_fname
Version: 1.0
Release: alt1

Summary: Quotes from Sun-Tzu's "The Art of War"
Group: Games/Other
License: GPL
Url: http://www.gutenberg.org/

BuildArch: noarch

Source: fortunes-%_fname-%version.tar.gz

PreReq: fortune-mod

%description
This is a collection of quotes from the famous book "The Art of War"
for use with 'fortune' program

%prep
%setup -q

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -p -m 644 %{_fname}* %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*
%doc README LICENSE.GUTENBERG 132a.txt

%changelog
* Thu Sep 01 2005 Nick S. Grechukh <gns@altlinux.ru> 1.0-alt1
- initial build for ALTLinux Sisyphus

