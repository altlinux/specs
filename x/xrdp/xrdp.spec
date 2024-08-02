%global _unpackaged_files_terminate_build 1
Name: 	 xrdp
Version: 0.10.1
Release: alt1

Summary: An open source remote desktop protocol (RDP) server

License: GPLv2+ with exceptions and Apache-2.0
Group: 	 System/Servers
Url: 	 http://xrdp.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
# VCS:   https://github.com/neutrinolabs/xrdp
Source1: %name.sysconfig
Source2: %name.logrotate
Source3: %name-init-alt
Source4: submodules.tar
Source6: xorgxrdp.tar
Source7: xrdp-sesman.pam
Source8: xrdp-polkit-1.rules

# patches from Debian
Patch2: asm-xorgxrdp.diff
Patch3: make-fixes.diff
Patch5: misc-fixes.diff
Patch10: lfs.diff

# Other patches
Patch12: xrdp-alt-startwm.patch
Patch13: alt-add-russian-keyboard.patch
Patch14: xrdp-alt-add-comment-about-windows_xp.patch
Patch16: xrdp-alt-ppc64le-support.patch

# Fedora patches
Patch21: xrdp-service.patch
Patch22: xrdp-0.9.6-script-interpreter.patch
Patch23: xrdp-0.9.9-sesman.patch
Patch24: xrdp-0.9.10-scripts-libexec.patch
Patch25: xrdp-0.9.14-arch.patch
Patch28: xrdp-0.9.14-vnc-uninit.patch
Patch30: xrdp-0.9.14-xrdp-ini.patch
Patch31: xrdp-0.9.15-g_check_user_in_group.patch

BuildPreReq: rpm-build-intro rpm-macros-intro-conflicts
BuildRequires: libjpeg-devel
BuildRequires: libpam-devel
BuildRequires: libssl-devel
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: xorg-resourceproto-devel
BuildRequires: xorg-scrnsaverproto-devel
BuildRequires: libXfont2-devel
BuildRequires: libfuse-devel
BuildRequires: libfreerdp-devel
BuildRequires: libopus-devel
BuildRequires: openssl
BuildRequires: xorg-sdk
BuildRequires: nasm
# For glamor support
BuildRequires: libgbm-devel
BuildRequires: libepoxy-devel
BuildRequires: libdrm-devel
BuildRequires: imlib2-devel
BuildRequires: libfreetype-devel
BuildRequires: libpixman-devel
BuildRequires: fdkaac
BuildRequires: libjpeg-devel
BuildRequires: liblame-devel
BuildRequires: libfdk-aac-devel

Requires: xorg-drv-xrdp = %EVR
Requires: xinitrc

Provides: librfxcodec = %EVR
Obsoletes: librfxcodec < %EVR
Provides: librfxcodec-devel = %EVR
Obsoletes: librfxcodec-devel < %EVR

%filter_from_requires \,^/etc/X11/xinit/Xsession,d
%filter_from_requires \,^/usr/etc/X11/xdm/Xsession,d
%filter_from_requires \,^/etc/X11/xdm/Xsession,d
%filter_from_requires \,^/etc/X11/xinit/xinitrc,d
%filter_from_requires \,^/etc/sysconfig/i18n,d

%description
xrdp offers a graphical login to a remote client using
RDP (the Remote Desktop Protocol). xrdp can connect to
a locally created X.org session with the xorgxrdp drivers,
to a VNC X11 server, and forward to another RDP server.

xrdp accepts connections from freerdp, rdesktop, and the
built-in terminal server / remote desktop clients of
Microsoft Windows operating systems.
In the xorgxrdp (which replaces X11RDP) and VNC modes,
it provides a fully functional Linux terminal server,
offering an X-Window desktop to the user. In the RDP
or VNC forwarding mode, any sort of desktop can be used.

%package -n xorg-drv-%name
Summary: Remote Desktop Protocol (RDP) modules for X.org
Group: System/X11
Provides: xorgxrdp = %EVR

%description -n xorg-drv-xrdp
xorgxrdp is a set of drivers (screen device, keyboard, and mouse)
for X.org enabling use through an RDP session with xrdp. For full
operation, most standard X11 fonts and tools need to be installed.

%prep
%setup
tar xf %SOURCE4
tar xf %SOURCE6
#patch2 -p1
%patch3 -p1
%patch5 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch21 -p1
%patch22 -p1
%patch25 -p1
%patch28 -p1
%patch31 -p1
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' configure.ac
%endif

cp %SOURCE3 %name-init

subst "s|/usr/lib|%_libdir|g" %name-init
find . -type f -name Makefile.am -exec subst "s|\${localstatedir}\/run|/var/run|g" {} \;

# remove unused modules from xrdp login combobox
subst '/^\[Xvnc\]/,$s/^\([a-z[]\)/#\1/' xrdp/xrdp.ini.in

# create 'bash -l' based startwm, to pick up PATH etc.
echo '#!/bin/bash -l
. %_sysconfdir/xrdp/startwm.sh' > sesman/startwm-bash.sh

%build
%add_optflags -I%_includedir/libdrm
%add_optflags -Wno-error=int-to-pointer-cast
%ifarch %ix86
%add_optflags -fPIC
%set_verify_elf_method textrel=relaxed
%endif
./bootstrap
for dir in xorgxrdp librfxcodec libpainter; do
	pushd $dir
	./bootstrap
	popd
done
#autoreconf
%configure \ #--disable-static \
	   --enable-jpeg \
	   --enable-fuse \
	   --enable-rfxcodec \
	   --enable-opus \
	   --enable-painter \
	   --enable-pixman \
	   --with-imlib2=yes \
	   --enable-tjpeg \
	   --with-freetype2=yes \
	   --enable-mp3lame \
	   --enable-vsock \
	   --enable-rdpsndaudin \
	   --enable-fdkaac \
	   --with-systemdsystemunitdir=%_unitdir
pushd xorgxrdp
PKG_CONFIG_PATH=../pkgconfig ./configure --enable-glamor
popd
pushd librfxcodec
./configure \
	    --disable-shared \
	    --enable-static
popd
pushd libpainter
./configure \
	    --disable-shared \
	    --enable-static
popd
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/xrdp

rm -f %buildroot/%_libdir/xrdp/startwm.sh
rm -f %buildroot/%_libdir/xrdp/xrdp_control.sh
install -D -m755 %name-init %buildroot%_initdir/%name
rm -rf %buildroot%_sysconfdir/init.d

# install sesman pam config 
install -Dp -m 644 %SOURCE7 %buildroot%_sysconfdir/pam.d/xrdp-sesman

# install xrdp systemd units
install -Dp -m 644 instfiles/xrdp.service %buildroot%_unitdir/xrdp.service
install -Dp -m 644 instfiles/xrdp-sesman.service %buildroot%_unitdir/xrdp-sesman.service

# install xrdp sysconfig /etc/sysconfig/xrdp
install -Dp -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/xrdp

# install logrotate /etc/logrotate.d/xrdp
install -Dp -m 644 %SOURCE2 %buildroot%_logrotatedir/%name

# install log file /var/log/xrdp-sesman.log
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/xrdp-sesman.log

# rsakeys.ini
touch %buildroot%_sysconfdir/xrdp/rsakeys.ini
chmod 0600 %buildroot%_sysconfdir/xrdp/rsakeys.ini

# install 'bash -l' startwm script
install -Dp -m 755 sesman/startwm-bash.sh %buildroot%_sysconfdir/xrdp/startwm-bash.sh

# install openssl config for key generation
install -Dp -m 644 keygen/openssl.conf %buildroot%_sysconfdir/xrdp/openssl.conf

#install xrdp.rules /usr/share/polkit-1/rules.d
install -Dp -m 644 %SOURCE8 %buildroot%_datadir/polkit-1/rules.d/xrdp.rules

# Clean unnecessary files
find %buildroot -name *.a -delete -o -name *.la -delete
rm -rf %buildroot{/usr/local,%_includedir,%_pkgconfigdir}

%pre
groupadd -r -f tsusers 2>/dev/null ||:
groupadd -r -f tsadmins 2>/dev/null ||:

%post
# Generate keys if they are missing
if [ ! -s %_sysconfdir/xrdp/rsakeys.ini ]; then
  (umask 377; %_bindir/xrdp-keygen xrdp %_sysconfdir/xrdp/rsakeys.ini >/dev/null)
  chmod 400 %_sysconfdir/xrdp/rsakeys.ini
fi

if [ ! -s %_sysconfdir/xrdp/cert.pem ]; then
  (umask 377; openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 3652 \
    -keyout %_sysconfdir/xrdp/key.pem \
    -out %_sysconfdir/xrdp/cert.pem \
    -subj /C=US/ST=CA/L=Sunnyvale/O=xrdp/CN=www.xrdp.org \
    -config %_sysconfdir/xrdp/openssl.conf >/dev/null 2>&1)
  chmod 400 %_sysconfdir/xrdp/cert.pem
  chmod 400 %_sysconfdir/xrdp/key.pem
fi
%post_service %{name}-sesman
%post_service %name

%preun
%preun_service %name
%preun_service %{name}-sesman

%files
%config(noreplace) %_sysconfdir/pam.d/xrdp-sesman
%dir %_sysconfdir/xrdp
%_sysconfdir/xrdp/km*.ini
%_sysconfdir/xrdp/*.sh
%dir %_sysconfdir/xrdp/pulse
%_sysconfdir/xrdp/pulse/default.pa
%_sysconfdir/xrdp/xrdp_keyboard.ini
%_sysconfdir/xrdp/openssl.conf
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/xrdp
%_unitdir/*.service
%ghost %_logdir/xrdp-sesman.log
%ghost %config(noreplace) %attr(0400,root,root) %verify(not size md5 mtime) %_sysconfdir/xrdp/rsakeys.ini
%ghost %config(noreplace) %attr(0400,root,root) %verify(not size md5 mtime) %_sysconfdir/xrdp/*.pem
%config(noreplace) %_sysconfdir/xrdp/sesman.ini
%config(noreplace) %_sysconfdir/xrdp/xrdp.ini
%_bindir/xrdp*
%_libexecdir/xrdp/*
%_sbindir/xrdp*
%_libdir/%name
%_logrotatedir/%name
%dir %_datadir/xrdp
%_datadir/xrdp/*
%_datadir/polkit-1/rules.d/xrdp.rules
%_man1dir/*
%_man5dir/*
%_man8dir/*

%files -n xorg-drv-xrdp
%_sysconfdir/X11/%name/xorg.conf
%_x11modulesdir/*.so
%_x11modulesdir/drivers/*.so
%_x11modulesdir/input/*.so

%changelog
* Thu Aug 01 2024 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version.

* Wed Jul 03 2024 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt4
- Remove autoreq on /etc/sysconfig/i18n.

* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt3
- Fix rpm macros in %%install and %%files.

* Mon May 13 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.10.0-alt2
- E2K: build fix

* Sun May 12 2024 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- New version.

* Thu Mar 14 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.25.1-alt1
- New version.

* Tue Mar 12 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.25-alt1
- New version.

* Wed Jan 03 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.24-alt1
- New version.

* Thu Sep 28 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.23.1-alt1
- New version.
- Security fixes:
  + CVE-2023-42822: Unchecked access to font glyph info

* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.23-alt1
- New version.
- Security fixes:
  + CVE-2023-40184: Improper handling of session establishment errors allows bypassing OS-level session restrictions

* Tue May 23 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.22.1-alt1
- New version.

* Sun May 07 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.22-alt1
- New version.

* Tue Dec 20 2022 Alexander Danilov <admsasha@altlinux.org> 0.9.21.1-alt2
- added filter_from_requires.

* Wed Dec 14 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.21.1-alt1
- New version.

* Sun Dec 11 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.21-alt1
- New version.
- Security fixes: CVE-2022-23468, CVE-2022-23477, CVE-2022-23478,
  CVE-2022-23479, CVE-2022-23480, CVE-2022-23481, CVE-2022-23483,
  CVE-2022-23482, CVE-2022-23484, CVE-2022-23493

* Sun Sep 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.20-alt1
- New version.

* Thu Mar 17 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.19-alt1
- New version.

* Tue Feb 08 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.18.1-alt1
- New version.
- Security fixes:
  + CVE-2022-23613: Privilege escalation on xrdp-sesman

* Wed Jan 12 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.18-alt1
- New version.

* Wed Dec 08 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2
- Enable glamor support for xorgxrdp.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt1
- New version.

* Fri Jun 11 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.16-alt2
- Do not replace sesman.ini and xrdp.ini during package update.

* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.16-alt1
- New version.

* Thu Apr 01 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.15-alt3
- Allow DISPLAY=:0 for chansrv (https://github.com/neutrinolabs/xrdp/issues/1846).

* Thu Mar 04 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.15-alt2
- Update g_check_user_in_group() with using getgrouplist() for group membership check.

* Tue Dec 29 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.15-alt1
- New version.

* Mon Dec 21 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.14-alt5
- Change PAM rules from system-auth to common-login.
- Build with -fPIC for i586.

* Wed Nov 18 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.14-alt4
- Use patches and polkit rules from Fedora.

* Mon Oct 12 2020 Michael Shigorin <mike@altlinux.org> 0.9.14-alt3
- E2K: ftbfs workaround

* Mon Sep 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.14-alt2
- Use system-auth pam rules instead of local unix users.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.14-alt1
- New version.

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.13.1-alt1
- New version.

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.13-alt1
- New version.

* Sun Dec 29 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.12.1-alt1
- New version.

* Mon Oct  7 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.11-alt2
- Keep keys in /etc/xrdp/ on upgrade and removal. (Important on upgrade
  from <= 0.9.3-alt1, which used to own these files. They would be removed,
  but now this package owns them again, so that they are not removed on upgrade.
  It also marks them as config, so that they are not removed on removal.)

* Sat Aug 24 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt1
- New version.

* Tue May 28 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt2
- Add sample configuration for Windows XP to xrdp.ini.

* Fri Apr 19 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt1
- New version.

* Fri Apr 19 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt3
- Run %%post_service after certificate generation.

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt2
- Remove autorequirement of xterm.

* Tue Dec 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt1
- New version.

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.7-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jun 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt1
- New version.

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version.

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt2
- clean build

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1
- New version

* Thu Aug 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.3.1-alt1
- New version
- Add Rissian keyboard example to /etc/xrdp/xrdp_keyboard.ini
- Do not package generated keys to prevent overwrite existing keys
- Restart both services xrdp and xrdp-sesman

* Wed Jul 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version (ALT #33674)
- xrdp requires xorg-drv-xrdp
- Create keys if they do not exist

* Fri Mar 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version

* Tue Mar 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.gitf422461
- New version from Git repository
- Enable fuse for drive redirection or clipboard file transfer

* Mon Sep 21 2015 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt1.1
- fix pidfile path and sysv init script.

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
