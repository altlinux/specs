%def_with x
%def_with directfb
%def_without svgalib

Name: links2
Version: 2.29
Release: alt1

Summary: Lynx-like text and graphics WWW browser
# actually GPLv2+ with OpenSSL exception, stupid SPDX doesn't grok that
License: GPLv2+ and MPL-2.0
Group: Networking/WWW

Url: http://links.twibright.com
Source0: %url/download/links-%version.tar.gz
Source100: %name.watch

%if_with directfb
BuildPreReq: libdirectfb-devel
%endif

%if_with svgalib
BuildPreReq: svgalib-devel
%endif

%if_with x
BuildPreReq: libXt-devel
%endif

# alternatives
%define weight 20
Requires(pre,postun): alternatives >= 0.2.0
BuildPreReq: alternatives >= 0.2.0

Provides: webclient, links
Provides: %_bindir/links
Obsoletes: links

# Automatically added by buildreq on Tue Apr 10 2012
# optimized out: alternatives libX11-devel libcom_err-devel libkrb5-devel libsysfs-devel pkg-config xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel libXt-devel libdirectfb-devel libgpm-devel libjpeg-devel liblzma-devel libpng-devel libssl-devel libtiff-devel

BuildRequires: libSDL-devel
BuildRequires: libevent-devel
BuildRequires: libbrotli-devel

Summary(ru_RU.UTF-8): Текстовый и графический веб-браузер, похожий на Lynx

%description
Links is a graphics and text mode web browser, released under GPL.
Links runs in graphics mode (mouse required) on X Window System (UN*X,
Cygwin), SVGAlib, Linux Framebuffer, OS/2 PMShell, AtheOS GUI.
Links runs in text mode (mouse optional) on UN*X console, ssh/telnet
virtual terminal, vt100 terminal, xterm, and virtually any other text
terminal. Mouse is supported for GPM, xterm, and OS/2. Links supports
colors on terminal.

%description -l ru_RU.UTF-8
Links - веб-браузер для графического и текстового режима, выпущенный
под лицензией GPL.

В графическом режиме требует мышь и работает на X Window System
(UN*X, Cygwin), SVGAlib, Linux Framebuffer, OS/2 PMShell, AtheOS GUI.

В текстовом режиме может использовать мышь и работает на UN*X-консоли,
виртуальных терминалах ssh/telnet, vt100, xterm и практически любых
других текстовых. Мышь поддерживается на GPM, xterm и OS/2.
Links умеет цвета в терминале.

%prep
%setup -n links-%version

%build
%add_optflags -Wno-pointer-sign -fno-strict-aliasing
%configure \
	--enable-graphics \
	%{subst_with x} \
	%{subst_with directfb} \
	%{subst_with svgalib} \
	--enable-debuglevel=0
	#--enable-javascript
%make_build

%install
%makeinstall

mv %buildroot%_bindir/links %buildroot%_bindir/links-%version
ln -s links-%version %buildroot%_bindir/%name
mv %buildroot%_man1dir/links.1 %buildroot%_man1dir/%name.1

install -pDm644 links_16x16_1.xpm %buildroot%_miconsdir/%name.xpm
install -pDm644 links_32x32.xpm %buildroot%_niconsdir/%name.xpm
install -pDm644 graphics/links.xpm %buildroot%_liconsdir/%name.xpm

mkdir -p %buildroot%_altdir
cat <<__EOF__ >%buildroot%_altdir/%name
%_bindir/links	%_bindir/%name	%weight
%_man1dir/links.1.gz	%_man1dir/%name.1.gz	%_bindir/%name
__EOF__

mkdir -p %buildroot%_desktopdir
cat <<__EOF__ >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=Links 2
Exec=xlinks2
Terminal=false
Categories=Network;WebBrowser;
Comment=Web browser running in both graphics and text mode
__EOF__

cat <<__EOF__ >%buildroot%_bindir/x%name
#!/bin/sh
exec links2 -g "$@"
__EOF__
chmod +x %buildroot%_bindir/x%name

%files
%_altdir/%name
%_bindir/%name
%_bindir/x%name
%_bindir/links-%version
%_desktopdir/%name.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_man1dir/*
%doc doc/
%doc AUTHORS BRAILLE_HOWTO ChangeLog INSTALL KEYS NEWS 
#doc PATCH-gpm-1.20.0-smooth-cursor PATCH-libpng-1.2.18 
%doc README SITES mailcap.pl

# TODO:
# - consider system publicsuffix like debian

%changelog
* Thu Mar 23 2023 Michael Shigorin <mike@altlinux.org> 2.29-alt1
- new version (watch file uupdate)

* Sun Oct 02 2022 Michael Shigorin <mike@altlinux.org> 2.28-alt1
- new version (watch file uupdate)

* Mon May 30 2022 Michael Shigorin <mike@altlinux.org> 2.27-alt1
- new version (watch file uupdate)

* Tue Apr 12 2022 Michael Shigorin <mike@altlinux.org> 2.26-alt1
- new version (watch file uupdate)

* Thu Oct 07 2021 Michael Shigorin <mike@altlinux.org> 2.25-alt1
- new version (watch file uupdate)

* Wed Sep 15 2021 Michael Shigorin <mike@altlinux.org> 2.24-alt1
- new version (watch file uupdate)

* Tue May 25 2021 Michael Shigorin <mike@altlinux.org> 2.23-alt1
- new version (watch file uupdate)

* Thu Mar 18 2021 Michael Shigorin <mike@altlinux.org> 2.22-alt1
- new version (watch file uupdate)
- "clarified" license (actually GPLv2+ with OpenSSL exceptions
  and MPL2-licensed public suffix list data)

* Sun Aug 09 2020 Michael Shigorin <mike@altlinux.org> 2.21-alt1
- new version (watch file uupdate)

* Thu Sep 26 2019 Michael Shigorin <mike@altlinux.org> 2.20.2-alt1
- new version (watch file uupdate)

* Fri Sep 06 2019 Michael Shigorin <mike@altlinux.org> 2.20.1-alt1
- new version (watch file uupdate)

* Thu Aug 29 2019 Michael Shigorin <mike@altlinux.org> 2.20-alt1
- new version (watch file uupdate)
- fixes DNS prefetch security problem present from 2.15 to 2.19

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 2.19-alt1
- new version (watch file uupdate) (closes: #36495)
- don't enable javascript explicitly (ftbfs)
- added a few BRs spotted in debian/opensuse packages

* Thu Jan 17 2019 Michael Shigorin <mike@altlinux.org> 2.18-alt1
- new version (watch file uupdate)

* Tue Sep 11 2018 Michael Shigorin <mike@altlinux.org> 2.17-alt1
- new version (watch file uupdate)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.15-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri May 11 2018 Michael Shigorin <mike@altlinux.org> 2.16-alt1
- new version (watch file uupdate)

* Sun Mar 25 2018 Michael Shigorin <mike@altlinux.org> 2.15-alt1
- new version (watch file uupdate)

* Sun Dec 04 2016 Michael Shigorin <mike@altlinux.org> 2.14-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 2.13-alt1
- new version (watch file uupdate)

* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 2.12-alt1
- new version (watch file uupdate)

* Mon Aug 31 2015 Michael Shigorin <mike@altlinux.org> 2.11-alt1
- new version (watch file uupdate)

* Mon Aug 10 2015 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- new version (watch file uupdate)

* Thu Jan 16 2014 Michael Shigorin <mike@altlinux.org> 2.8-alt1
- new version (watch file uupdate)
- added Russian package description

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.1
- Rebuilt with libpng15

* Tue Apr 10 2012 Michael Shigorin <mike@altlinux.org> 2.6-alt1
- 2.6
- buildreq

* Thu Nov 24 2011 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- 2.4 (update by Yurii Suhanov)
- minor spec cleanup

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 2.2-alt2.2
- rebuilt against openssl-1.0.0a

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for links2
  * postclean-05-filetriggers for spec file

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 2.2-alt2.1
- applied repocop patch

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 2.2-alt2
- added desktop file (#17784)
- well, better maintainer is still welcome

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Aug 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt1
- 2.2

* Sun Jul 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.1rel-alt1
- 2.1

* Sun May 18 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre36-alt1
- 2.1pre36

* Tue May 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre35-alt1
- 2.1pre35

* Wed Feb 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre33-alt1
- 2.1pre33
- use tabs in alternatives config (#13944)

* Mon Nov 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre31-alt1
- 2.1pre31

* Sat Oct 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre30-alt1
- 2.1pre30

* Thu Aug 02 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre29-alt1
- 2.1pre29

* Thu Apr 12 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre28-alt1
- 2.1pre28
- spec cleanup

* Wed Apr 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre27-alt1
- 2.1pre27

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre26-alt1
- 2.1pre26
- [CVE-2006-5925]

* Wed Aug 09 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.1pre23-alt1
- initial build
