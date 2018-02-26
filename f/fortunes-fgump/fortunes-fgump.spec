# vim: set ft=spec: -*- rpm-spec -*-
%define _name fortune-fgump

Name: fortunes-fgump
Version: 20000725
Release: alt1

Summary: Quotes from the movie "Forrest Gump"
Group: Games/Other
License: Freely distributable
Url: http://www.splitbrain.org/Fortunes/fgump/

BuildArch: noarch

Source: %_name.tgz

PreReq: fortune-mod

%description
This is a collection of quotes from the movie "Forrest Gump"
for use with 'fortune' program.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -p -m 644 fgump* %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*
%doc README

%changelog
* Sun Aug 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 20000725-alt1
- Initial Sisyphus package.

