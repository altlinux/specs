Name: xlockmore
Version: 5.41
Release: alt1

Summary: An X terminal locking program
License: MIT
Group: Graphical desktop/Other
Url: http://www.tux.org/~bagleyd/xlockmore.html
Packager: Damir Shayhutdinov <damir@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name-v5.27-icons.tar.gz
Source2: %name-v5.27-pam.d.tar
Source3: po.tar.gz

Patch: %name-v5.27-imode.patch
Patch1: %name-v5.27-pam.patch
Patch2: %name-v5.27-l10n.patch
Patch3: %name-v5.27-kbdmon.patch

PreReq: /etc/tcb
Requires: fortune-mod
Requires: terminus-font

BuildPreReq: gcc-c++
BuildPreReq: libXpm-devel libXmu-devel

# Automatically added by buildreq on Tue Feb 12 2013
# optimized out: gnu-config libGL-devel libICE-devel libSM-devel libX11-devel libXt-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libGLU-devel libXdmcp-devel libXext-devel libXinerama-devel libXmu-devel libXpm-devel libfreetype-devel libpam-devel xorg-cf-files

%description
The %name utility is an enhanced version of the standard xlock
program, which allows you to lock an X session so that other users
can't access it. Xlockmore runs a provided screensaver until you type
in your password.

Install the %name package if you need a locking program to secure
X sessions.

%prep
%setup -b1 -b2 -a3
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
%configure \
	--without-motif \
	--without-gtk \
	--without-esound \
	--enable-pam \
	--enable-bad-pam \
	--enable-vtlock \
	--enable-button-logout=85 \
	--enable-use_mb \
	--enable-kbdmon

%make_build \
	xapploaddir=%_sysconfdir/X11/app-defaults

%install
install -p -m640 -D ../%name-v5.27-pam.d/xlock %buildroot%_sysconfdir/pam.d/xlock
install -p -m644 -D xlock/xlock.man %buildroot%_mandir/man1/xlock.1
install -p -m644 -D xlock/XLock.ad %buildroot%_sysconfdir/X11/app-defaults/XLock
install -p -m644 -D xlock/XLock-ja.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.ja_JP.EUCJP
install -p -m644 -D xlock/XLock-zh_TW.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.zh_TW.UTF-8
install -p -m644 -D xlock/XLock-ru.ad %buildroot%_sysconfdir/X11/app-defaults/XLock.ru_RU.UTF-8

install -D -m 644 ../%name-v5.27-icons/xlock-16x16.xpm %buildroot%_miconsdir/%name.xpm
install -D -m 644 ../%name-v5.27-icons/xlock-32x32.xpm %buildroot%_iconsdir/%name.xpm
install -D -m 644 ../%name-v5.27-icons/xlock-48x48.xpm %buildroot%_liconsdir/%name.xpm

%make_install install \
	prefix=%buildroot%prefix \
	bindir=%buildroot%_bindir \
	mandir=%buildroot%_mandir \
	datadir=%buildroot%_datadir \
	xapploaddir=%buildroot%_sysconfdir/X11/app-defaults

chmod 755 %buildroot%_bindir/*

%files
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%attr(2711,root,chkpwd) %_bindir/*
%attr(0640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%_mandir/man?/*
%_iconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm
%_datadir/locale/*/*/xlock.mo
%exclude %_mandir/xlock.1*

%changelog
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
