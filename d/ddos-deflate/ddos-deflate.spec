Name: ddos-deflate
Version: 0.6
Release: alt1
License: Artistic License
Group: Networking/Other
Summary: (D)DoS Deflate

Source0: %name-%version.tar
Source1: ddos-deflate.cron

BuildArch: noarch

%description
(D)DoS Deflate is a lightweight bash shell script designed to
assist in the process of blocking a denial of service attack.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_sysconfdir/%name
mkdir -p %buildroot/%_datadir/%name
mkdir -p %buildroot/%_sysconfdir/cron.d
install -m755 ddos.sh %buildroot/%_sbindir/%name
install -m644 ddos.conf %buildroot/%_sysconfdir/%name/
install -m644 ignore.ip.list %buildroot/%_sysconfdir/%name/
install -m644 LICENSE %buildroot/%_datadir/%name/
install -m644 %SOURCE1 %buildroot/%_sysconfdir/cron.d/%name

%files
%_sbindir/%name
%_sysconfdir/%name
%_sysconfdir/%name/*
%_datadir/%name
%_datadir/%name/*
%_sysconfdir/cron.d/*

%changelog
* Fri Jul 04 2014 Timur Aitov <timonbl4@altlinux.org> 0.6-alt1
- Version 0.6

