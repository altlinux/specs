
Name: 	 xrdp
Version: 0.6.1
Release: alt1

Summary: An open source remote desktop protocol (RDP) server

License: GPLv2+ with exceptions
Group: 	 System/Servers
Url: 	 http://xrdp.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

# Source-url: http://prdownloads.sourceforge.net/%name/%version/%name-v%version.tar
Source:  %name-%version.tar
Source1: %name.service
Source2: %name-sesman.service
Source3: %name.sysconfig
Source4: %name.logrotate
Source5: %name-init-alt
Source6: xrdp-keygen.8

BuildRequires: libpam-devel
BuildRequires: libssl-devel
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel

BuildPreReq: rpm-build-intro

Requires: tigervnc-server

# Patches from Fedora
Patch0: xrdp-pam-auth.patch
Patch1: xrdp-use-xinitrc-in-startwm-sh.patch
Patch2: xrdp-pam-session.patch
# https://sourceforge.net/tracker/?group_id=112022&atid=665248
# https://bugzilla.redhat.com/show_bug.cgi?id=905411
Patch3: xrdp-endian.patch

# patches from Debian
Patch4: xrdp-reuse-session.patch
Patch5: xrdp-quiet-start.patch
Patch6: xrdp-default-keymap.patch
Patch7: xrdp-pidfile-early.patch
Patch8: xrdp-format-security.patch

# Other patches
Patch10: xrdp-0.6.1-fix-build.patch
Patch11: xrdp-add-missing-manpages.patch

%description
The goal of this project is to provide a fully
functional Linux terminal server, capable of
accepting connections from rdesktop and
Microsoft's own terminal server / remote
desktop clients.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p2
%patch11 -p2

cp %SOURCE5 %name-init

subst "s|/usr/lib|%_libdir|g" %name-init

# remove unused modules from xrdp login combobox
sed -i -e '/\[xrdp2\]/,$d' xrdp/xrdp.ini

#Low is 40 bit key and everything from client to server is encrypted.
#Medium is 40 bit key, everything both ways is encrypted.
#High is 128 bit key everything both ways is encrypted.

# increase encryption to 128 bit's
sed -i 's/crypt_level=low/crypt_level=high/g' xrdp/xrdp.ini

# create 'bash -l' based startwm, to pick up PATH etc.
echo '#!/bin/bash -l
. %_sysconfdir/xrdp/startwm.sh' > sesman/startwm-bash.sh

# set 'bash -l' based startwm script as default
sed -i -e 's/DefaultWindowManager=startwm.sh/DefaultWindowManager=startwm-bash.sh/' sesman/sesman.ini

# Man page for xrdp-keygen
cp %SOURCE6 docs/man/


%build
%autoreconf
%configure --disable-static
%make_build

%install
# TODO: fix it in make
mkdir -p %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_man8dir %buildroot%_man5dir

%makeinstall_std

rm -f %buildroot/%_libdir/xrdp/startwm.sh
rm -f %buildroot/%_libdir/xrdp/xrdp_control.sh
install -D -m755 %name-init %buildroot%_initrddir/%name

# remove .la files
rm -f %buildroot%_libdir/%name/*.la

# install sesman pam config /etc/pam.d/xrdp-sesman
install -Dp -m 644 instfiles/pam.d/xrdp-sesman %buildroot%_sysconfdir/pam.d/xrdp-sesman

# install xrdp systemd units
install -Dp -m 644 %SOURCE1 %buildroot/lib/systemd/system/xrdp.service
install -Dp -m 644 %SOURCE2 %buildroot/lib/systemd/system/xrdp-sesman.service

# install xrdp sysconfig /etc/sysconfig/xrdp
install -Dp -m 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/xrdp

# install logrotate /etc/logrotate.d/xrdp
install -Dp -m 644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/xrdp

# install log file /var/log/xrdp-sesman.log
mkdir -p %buildroot%_localstatedir/log/
touch %buildroot%_localstatedir/log/xrdp-sesman.log

# rsakeys.ini
touch %buildroot%_sysconfdir/xrdp/rsakeys.ini
chmod 0600 %buildroot%_sysconfdir/xrdp/rsakeys.ini

# install 'bash -l' startwm script
install -Dp -m 755 sesman/startwm-bash.sh %buildroot%_sysconfdir/xrdp/startwm-bash.sh

%post
%post_service %name

%preun
%preun_service %name

%files
%config %_sysconfdir/pam.d/xrdp-sesman
%dir %_sysconfdir/xrdp/
%_sysconfdir/xrdp/km*.ini
%_sysconfdir/xrdp/startwm*.sh
%_sysconfdir/xrdp/xrdp.sh
%_initrddir/xrdp
%config(noreplace) %_sysconfdir/sysconfig/xrdp
/lib/systemd/system/*.service
%ghost %_localstatedir/log/xrdp-sesman.log
%attr(0600,root,root) %verify(not size md5 mtime) %_sysconfdir/xrdp/rsakeys.ini
%config %_sysconfdir/xrdp/sesman.ini
%config %_sysconfdir/xrdp/xrdp.ini
%_bindir/xrdp*
%_sbindir/xrdp*
%_libdir/%name/lib*.so*
%_logrotatedir/%name
%dir %_datadir/xrdp/
%_datadir/xrdp/*
%_man5dir/*
%_man8dir/*


%changelog
* Fri Feb 07 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- New version (ALT #19193)
- Use patches and init scripts from Fedora and Debian (ALT #27853)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Thu Aug 18 2011 Denis Baranov <baraka@altlinux.ru> 0.4.2-alt1
- new version (0.4.2) with rpmbs script

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- fix build, cleanup spec

* Tue Oct 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Sun Nov 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt4
- provide internal lib
- install generic init script, add ALT init script
- use config mark for ini files

* Mon Sep 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- NMU build
- fix source tarball url
- set all destination pathes from spec
- add rpath to fix linking
- use /etc/X11/xdm/Xsession instead sessionwm.sh

* Wed Sep 12 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt2
- added patch by Nickolay <sn@m2.sta.gov.ua>
- fixing bug this documentation.

* Mon Aug 27 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt1
- new version

* Wed Jan 17 2007 Lunar Child <luch@altlinux.ru> 0.3.2-alt1
- First Build for ALT Linux Sisyphus
