Name: Supybot-data
Version: 20040909
Release: alt1

Summary: Optional data files for Supybot
License: distributable
Group: Networking/IRC

BuildArch: noarch

Source: %name.tar.bz2

Requires: Supybot

%description
Supybot is a flexible IRC bot written in python.
It features many plugins, is easy to extend and to use.

This package contains .supyfact files for Lookup plugin.

%prep
%setup -q -c -n supybot-data

%install
mkdir -p %buildroot%_datadir/Supybot
cp -a supybot-data %buildroot%_datadir/Supybot

%files
%_datadir/Supybot/supybot-data

%changelog
* Tue Apr 04 2006 Andrey Rahmatullin <wrar@altlinux.ru> 20040909-alt1
- initial build