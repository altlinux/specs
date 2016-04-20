Name: xlockmore
Version: 5.46
Release: alt2

Summary: An X terminal locking program
License: MIT
Group: Graphical desktop/Other
Url: http://www.tux.org/~bagleyd/xlockmore.html

Source: %name-%version.tar.xz
Source1: %name-v5.27-icons.tar.gz
Source2: %name-v5.27-pam.d.tar
Source3: po.tar.gz

Patch: xlockmore-5.46-imode.patch
Patch1: xlockmore-5.46-pam.patch
Patch2: xlockmore-5.46-l10n.patch
Patch3: xlockmore-5.46-kbdmon.patch
Patch4: xlockmore-5.46-nologout.patch
Patch5: xlockmore-5.46-droidfonts.patch
Patch6: xlockmore-5.46-alt-BSD_SOURCE.patch
Patch7: xlockmore-5.46-alt-build-freetype.patch


PreReq: /etc/tcb
Requires: fortune-mod
Requires: fonts-ttf-google-droid-sans fonts-ttf-google-droid-sans-mono fonts-ttf-google-droid-serif

BuildPreReq: gcc-c++
# Automatically added by buildreq on Sun Jun 29 2014
# optimized out: gnu-config libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXt-devel libcloog-isl4 libfreetype-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libXdmcp-devel libXext-devel libXinerama-devel libXmu-devel libXpm-devel libftgl-devel libpam-devel xorg-cf-files

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
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoconf
ftgl_includes=%_includedir/FTGL %configure \
	--without-motif \
	--without-gtk \
	--without-esound \
	--enable-pam \
	--enable-bad-pam \
	--enable-vtlock \
	--enable-button-logout=85 \
	--enable-use_mb \
	--enable-kbdmon
# Hack a little
echo '#define FTGL213' >> config.h

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
