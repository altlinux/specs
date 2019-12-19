Name: xlockmore
Version: 5.61
Release: alt1

Summary: An X terminal locking program
License: MIT
Group: Graphical desktop/Other
Url: http://sillycycle.com/xlockmore.html

Source: %name-%version.tar.xz
Source1: icons.tar.gz
Source2: pam.d.tar
Source3: po.tar.gz

Patch0001: 0001-Fix-install-modes.patch
Patch0002: 0002-Use-PAM-for-authorization.patch
Patch0003: 0003-Localize-and-translate.patch
Patch0004: 0004-Use-KBD-monitoring.patch
Patch0005: 0005-Provide-nologout-option-for-user-switching.patch
Patch0006: 0006-Use-Droid-fonts-instead-of-legacy-ones.patch
Patch0007: 0007-Switch-from-_BSD_SOURCE-to-_DEFAULT_SOURCE.patch
Patch0008: 0008-Fix-freetype2-detection.patch

PreReq: /etc/tcb
Requires: fortune-mod
Requires: fonts-ttf-google-droid-sans fonts-ttf-google-droid-sans-mono fonts-ttf-google-droid-serif

BuildPreReq: gcc-c++
# Automatically added by buildreq on Sun Jun 29 2014
# optimized out: gnu-config libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXt-devel libcloog-isl4 libfreetype-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libXdmcp-devel libXext-devel libXinerama-devel libXmu-devel libXpm-devel libftgl-devel libpam-devel xorg-cf-files autoconf-archive

%description
The %name utility is an enhanced version of the standard xlock
program, which allows you to lock an X session so that other users
can't access it. Xlockmore runs a provided screensaver until you type
in your password.

Install the %name package if you need a locking program to secure
X sessions.

%prep
%setup -a1 -a2 -a3
%patch0001 -p2
#patch0002 -p2
%patch0003 -p2
%patch0004 -p2
%patch0005 -p2
%patch0006 -p2
#patch0007 -p2
%patch0008 -p2

%build
cp /usr/share/aclocal/ax_pthread.m4 .
autoconf
ftgl_includes=%_includedir/FTGL %configure \
	--without-motif \
	--without-gtk \
	--without-esound \
	--disable-def-play \
	--enable-pam \
	--enable-bad-pam \
	--enable-vtlock \
	--enable-button-logout=85 \
	--enable-kbdmon
# Hack a little
echo '#define FTGL213' >> config.h

%make_build \
	xapploaddir=%_sysconfdir/X11/app-defaults

%install
install -p -m640 -D pam.d/xlock %buildroot%_sysconfdir/pam.d/xlock
install -p -m644 -D xlock/xlock.man %buildroot%_mandir/man1/xlock.1
install -p -m644 -D xlock/XLock.ad %buildroot%_sysconfdir/X11/app-defaults/XLock
install -p -m644 -D xlock/XLock-ja.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.ja_JP.EUCJP
install -p -m644 -D xlock/XLock-zh_TW.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.zh_TW.UTF-8
install -p -m644 -D xlock/XLock-ru.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.ru_RU.UTF-8

install -D -m 644 icons/xlock-16x16.xpm %buildroot%_miconsdir/%name.xpm
install -D -m 644 icons/xlock-32x32.xpm %buildroot%_iconsdir/%name.xpm
install -D -m 644 icons/xlock-48x48.xpm %buildroot%_liconsdir/%name.xpm

%make_install install \
	prefix=%buildroot%prefix \
	bindir=%buildroot%_bindir \
	mandir=%buildroot%_mandir \
	datadir=%buildroot%_datadir \
	xapploaddir=%buildroot%_sysconfdir/X11/app-defaults

chmod 755 %buildroot%_bindir/*
install -d %buildroot%_datadir/xlock/fonts

%post
find %_datadir/fonts/ttf -type f -iname \*.ttf | xargs -I. ln -sf . %_datadir/xlock/fonts/

%postun
rm -rf %_datadir/xlock/fonts/

%files
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%attr(2711,root,chkpwd) %_bindir/*
%attr(0640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%_mandir/man?/*
%_iconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm
%_datadir/locale/*/*/xlock.mo
%_datadir/xlock
%exclude %_mandir/xlock.1*

%changelog
* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 5.61-alt1
- Autobuild version bump to 5.61

* Mon Oct 21 2019 Fr. Br. George <george@altlinux.ru> 5.59-alt1
- Autobuild version bump to 5.59

* Thu Oct 03 2019 Fr. Br. George <george@altlinux.ru> 5.58-alt1
- Autobuild version bump to 5.58

* Wed Jun 26 2019 Fr. Br. George <george@altlinux.ru> 5.57-alt1
- Autobuild version bump to 5.57

* Tue Aug 28 2018 Fr. Br. George <george@altlinux.ru> 5.56-alt1
- Autobuild version bump to 5.56
- Drop some patches

* Tue May 29 2018 Fr. Br. George <george@altlinux.ru> 5.55-alt1
- Autobuild version bump to 5.55
- Update patches

* Wed Apr 20 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.46-alt2
- Fixed build with freetype.
- Switched from _BSD_SOURCE to _DEFAULT_SOURCE.

* Mon Apr 20 2015 Fr. Br. George <george@altlinux.ru> 5.46-alt1
- Autobuild version bump to 5.46
- Fix patches

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 5.45-alt1
- Autobuild version bump to 5.45

* Sun Jun 29 2014 Fr. Br. George <george@altlinux.ru> 5.43-alt2
- Add ftgl support
- Provide -nologout option for user switching
- Change default fonts to Droid ones

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 5.43-alt1
- Autobuild version bump to 5.43

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 5.42-alt1
- Autobuild version bump to 5.42
- Fix patch

* Tue Feb 12 2013 Fr. Br. George <george@altlinux.ru> 5.41-alt1
- Autobuild version bump to 5.41

* Wed Jan 14 2009 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt5
- Keyboard state monitor added.

* Wed Jan 14 2009 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt4
- Gettext/X11 resource based localization support.

* Tue Nov 18 2008 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt3
- Fix of the ReadXString() wrapper argument list.

* Fri Oct 10 2008 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt2
- Further PAM-integration: using interactive PAM-conversation
  without a pre-prompting for a password.

* Wed Oct 08 2008 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt1
- New version 5.27 geared.
