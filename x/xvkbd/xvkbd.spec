Name: xvkbd
Version: 4.1
Release: alt1

Summary: Virtual (on-screen) keyboard for X
License: GPLv2+
Group: System/X11

Url: http://t-sato.in.coocan.jp/xvkbd/
Source: %url/%name-%version.tar.gz
Source100: xvkbd.watch
# one-space patch sent upstream
Patch: xvkbd-4.1-make.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: ImageMagick-tools imake libXaw-devel libXaw3d-devel
BuildRequires: libXext-devel libXp-devel libXpm-devel libXtst-devel
BuildRequires: xorg-cf-files xorg-sdk

Summary(ru_RU.UTF-8): Виртуальная (экранная) клавиатура для X
Summary(uk_UA.UTF-8): Віртуальна (екранна) клавіатура для X

%description
%name is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(softwares) by clicking on a keyboard displayed on the screen. This may
be used for systems without a hardware keyboard such as kiosk terminals
or handheld devices.
This program also has facility to send characters specified as the
command line option to another client, which can help when one wants to
fully utilize some modern mice with multiple buttons.

%description -l ru_RU.UTF-8
%name - виртуальная (графическая) программная клавиатура для X Window,
которая предоставляет возможность вводить символы в другие клиенты
(программы) щелчком по клавишам, отображаемым на экране.  Это может
быть полезно для систем без аппаратной клавиатуры, таким как
терминалы-киоски или носимые устройства.
Эта программа также имеет возможность отправки символов, указанных
в опции командной строки, другому клиенту, что может быть полезно,
когда хочется полностью задействовать дополнительные кнопки
некоторых нынешних мышей.

%prep
%setup
%patch -p1

%build
xmkmf
# make CFLAGS=... broke as of 4.1 (used to work for 3.9)
export CFLAGS+="%optflags"
%make_build
for s in 48 36 32 24 22 16; do
	convert %{name}_icon.xbm \
		-resize ${s}x$s \
		-monochrome \
		-depth 8 \
		%name-$s.png
done

%install
%makeinstall_std install.man
for s in 48 36 32 24 22 16; do
	install -pDm644 %name-$s.png \
		%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name.png
done
rm -rf %buildroot/%_datadir/X11

install -d -m 0755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Version=1.0
Name=%name
Exec=%name
Icon=%name
Categories=Utility;Accessibility;
Type=Application
X-MultipleArgs=true
Terminal=false
StartupNotify=true
Comment=On-screen keyboard for X
Comment[ru]=Виртуальная (экранная) клавиатура для X
__MENU__

%files
%_bindir/*
%_sysconfdir/X11/app-defaults/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon May 04 2020 Michael Shigorin <mike@altlinux.org> 4.1-alt1
- new version (watch file uupdate)
- minor build/installation fixup
- added Russian description translation
- updated Url:

* Sun Sep 01 2019 Michael Shigorin <mike@altlinux.org> 4.0-alt1
- new version (watch file uupdate)

* Sun Feb 25 2018 Michael Shigorin <mike@altlinux.org> 3.9-alt1
- new version (watch file uupdate)

* Fri Jun 16 2017 Michael Shigorin <mike@altlinux.org> 3.8-alt1
- new version (watch file uupdate)

* Sat Sep 12 2015 Michael Shigorin <mike@altlinux.org> 3.7-alt1
- new version (watch file uupdate)

* Thu May 14 2015 Michael Shigorin <mike@altlinux.org> 3.6-alt1
- added debian-based watch file
- new version (watch file uupdate)
- converted spec to utf8

* Tue Apr 03 2012 Michael Shigorin <mike@altlinux.org> 3.3-alt1
- 3.3 (thx aris@ for heads-up)

* Mon Sep 19 2011 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- 3.2
- dropped patch (merged upstream)

* Mon Dec 01 2008 Led <led@altlinux.ru> 3.0-alt5
- updated BuildRequires
- cleaned up spec

* Mon Nov 10 2008 Led <led@altlinux.ru> 3.0-alt4
- rebuilt with libXaw.so.7
- updated BuildRequires

* Thu Aug 07 2008 Led <led@altlinux.ru> 3.0-alt3
- fixed %name.desktop

* Thu May 08 2008 Led <led@altlinux.ru> 3.0-alt2
- fixed default path to dict/words
- set Automatic Click OFF by default

* Wed May 07 2008 Led <led@altlinux.ru> 3.0-alt1
- 3.0

* Mon Mar 31 2008 Led <led@altlinux.ru> 2.9-alt1
- 2.9
- fixed License

* Tue Mar 04 2008 Led <led@altlinux.ru> 2.8-alt2
- fixed %name.desktop

* Wed Sep 20 2006 Led <led@altlinux.ru> 2.8-alt1
- 2.8

* Thu Jun 01 2006 Led <led@altlinux.ru> 2.7a-alt1
- initial build for Sisyphus

* Tue Jan 17 2006 Franck Villaume <fvill@mandriva.org> 2.7a-3mdk
- fix url
- mkrel

* Thu May 19 2005 Franck Villaume <fvill@mandriva.org> 2.7a-2mdk
- buildrequires

* Mon May 16 2005 Franck Villaume <fvill@mandriva.org> 2.7a-1mdk
- 2.7a
- buildrequires

* Wed May 04 2005 Abel Cheung <deaddog@mandriva.org> 2.6-1mdk
- New version

* Fri Aug 20 2004 Austin Acton <austin@mandrake.org> 2.5a-2mdk
- new menu

* Tue Jun 29 2004 Austin Acton <austin@mandrake.org> 2.5a-1mdk
- initial package
