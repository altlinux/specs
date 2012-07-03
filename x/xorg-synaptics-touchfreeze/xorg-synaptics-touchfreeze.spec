Name: xorg-synaptics-touchfreeze
Version: 0.2
Release: alt1

Summary: Disable Synaptics touchpad temporarily when typing

License: Public domain
Group: System/X11
Url: http://howtolinux.ru/2010/05/02/отключение-случайных-нажатий-тачпад/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/%name.git
Source: %name-%version.tar

BuildArchitectures: noarch

%description
This package contains scripts for automatic
disabling Synaptics touchpad temporarily when typing.
Uses syndaemon.
See /etc/X11/sysconfig/synaptics-touchfreeze for options.

%prep
%setup

%install
install -D -m755 synaptics-touchfreeze.sh %buildroot%_x11sysconfdir/xinit.d/synaptics-touchfreeze.sh
install -D -m644 shmconfig.fdi %buildroot%_sysconfdir/hal/fdi/policy/shmconfig.fdi
install -D -m644 synaptics-touchfreeze %buildroot/%_x11sysconfdir/sysconfig/synaptics-touchfreeze

%files
%_sysconfdir/hal/fdi/policy/shmconfig.fdi
%_x11sysconfdir/xinit.d/synaptics-touchfreeze.sh
%_x11sysconfdir/sysconfig/synaptics-touchfreeze

%changelog
* Tue Jul 27 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- fix fdi file

* Tue Jul 27 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

