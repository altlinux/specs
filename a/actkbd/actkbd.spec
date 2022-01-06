Summary:        A keyboard shortcut daemon
Name:           actkbd
Version:        0.2.8
Release:        alt2.qa1
URL:            http://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:	GPL-2.0-only
Group:		System/Configuration/Other

Source:		%name-%version.tar

%description
actkbd is a daemon that reacts to user defined keys and launches
specific commands. It can be used to utilize multimedia keys on
simple setups, or assigned custom actions to rarely used keys

%prep
%setup -q

%build
%make

%install
install -D -m 755 %name %buildroot%_sbindir/%name
install -D -m 644 %name.conf %buildroot%_sysconfdir/%name.conf

install -pD -m 755 %name.init  %buildroot%_initrddir/%name
install -pD -m 644 %name.service %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS ChangeLog COPYING FAQ NEWS README TODO samples/*
%config %_sysconfdir/%name.conf
%_sbindir/%name
%_initrddir/%name
%_unitdir/%name.service

%changelog
* Tue Jan 04 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.8-alt2.qa1
- Fixed path in %name.service systemd unit.
- Fixed License: tag.

* Sun Jul 06 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.2.8-alt2
- Fix lsb header in init script

* Fri Jul 04 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.2.8-alt1
- Initial build

