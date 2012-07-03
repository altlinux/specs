# vim: set ft=spec: -*- rpm-spec -*-
%define _name fortune-hitchhiker

Name: fortunes-hitchhiker
Version: 20050611
Release: alt1

Summary: Quotes from Douglas Adams' "Hitchhiker's Guide to the Galaxy".
Group: Games/Other
License: Freely distributable
Url: http://www.splitbrain.org

BuildArch: noarch

Source: %_name.tgz

PreReq: fortune-mod

%description
This is a collection of quotes from Douglas Adams' famous "Hitchhiker's
Guide to the Galaxy" for use with 'fortune' program.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -p -m 644 hitchhiker* %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*
%doc README

%changelog
* Sun Jun 12 2005 Alexey Rusakov <ktirf@altlinux.ru> 20050611-alt1
- Initial Sisyphus package.

