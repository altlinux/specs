Name: idesk
Version: 0.7.5
Release: alt3
Serial: 1

Summary: Desktop icon manager with support for PNG/SVG icons and antialiased text
License: BSD
Group: Graphical desktop/Other

Url: http://idesk.sourceforge.net
Source0: http://osdl.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.bz2
Source1: %name.desktop
Source2: start%name
Packager: Michael Shigorin <mike@altlinux.org>

Requires: xterm menu-icons-default >= 0.1-alt2

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: gcc-c++ imake imlib2-devel libXext-devel libXft-devel

Summary(ru_RU.UTF-8): Менеджер пиктограмм рабочего стола с поддержкой SVG/PNG и сглаживания шрифтов

%description
%name plops icons down on your root window (desktop) of graphical environment.
It includes support for PNG alpha layers, and pretty antialiased text with Xft.
..
Look to README file in documentation folder for description of usage.
Minimal configuration is created automatically in your home directory
when startidesk helper is running first time.

%description -l ru_RU.UTF-8
%name служит для размещения пиктограмм на корневом окне графической среды,
т.е. на десктопе. %name поддерживает форматы PNG и SVG, прозрачность,
а также сглаженный масштабируемый текст с применением Xft.

Смотрите файл README в каталоге с документацией для описания использования.
Минимальная конфигурация автоматически создаётся в вашем домашнем каталоге
в файле .ideskrc и подкаталоге .idesktop при первом запуске утилиты startidesk.

%prep
%setup

%build
autoreconf -fisv
%configure
%make_build

%install
install -pD -m755 src/%name %buildroot%_x11bindir/%name
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pD -m755 %SOURCE2 %buildroot%_x11bindir/start%name

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO examples
%_x11bindir/*
%_desktopdir/*

%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1:0.7.5-alt3
- applied repocop patch

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 1:0.7.5-alt2
- fixed build
- replaced Debian menu file with original desktop one
- spec cleanup
- me as a Packager:
- description translation converted to utf-8

* Fri Dec  2 2005 Ilya G. Evseev <evseev@altlinux.ru> 1:0.7.5-alt1
- update to new version 0.7.5,
- applied changes from dimajin(BigAt)mail(LittleDot)ru:
   + added COPYING file for conforming GNU reqs
   + changed .link suffix to .lnk for created shortcuts
   + use xvt instead of xterm as X console

* Tue Aug 30 2005 Ilya G. Evseev <evseev@altlinux.ru> 1:0.7.3-alt1
- update to new version

* Mon May 23 2005 Ilya G. Evseev <evseev@altlinux.ru> 1:0.7.2-alt1
- update to new version
- added examples folder

* Mon Feb 28 2005 Ilya G. Evseev <evseev@altlinux.ru> 1:0.7.1-alt1
- 0.7.1

* Mon Feb 14 2005 Ilya G. Evseev <evseev@altlinux.ru> 1:0.7.0-alt1
- version 0.7.0
- all patches are removed since their fuctionality is already in upstream
- README.ALT-* and EXAMPLE.idesk* are removed since they are obsoleted
- startidesk is rewritten for accoring new settings format
- spec cleanups: changed URL, description, other small stuff.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.3.5-alt8.1.1
- Rebuilt with libstdc++.so.6.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.3.5-alt8.1
- Rebuilt with libtiff.so.4.

* Sun May 02 2004 Anton V. Denisov <avd@altlinux.org> 1:0.3.5-alt8
- fixed path for icon in 'startidesk' script.
- added Requires: menu-icons-default >= 0.1-alt2 acordingly.
- updated BuildRequires in ALT Linux Sisyphus (20040402) env.

* Thu Oct 09 2003 Anton V. Denisov <avd@altlinux.org> 1:0.3.5-alt7
- idesk-0.3.5-kvinokurov-dblclick.patch added (now we can launch
	programs by single-click on icon,
	thanks to Konstantin Vinokurov).
- README.ALT.*, EXAMPLE.ideskrc and start%name updated accordingly.

* Mon Jun 23 2003 Anton V. Denisov <avd@altlinux.org> 1:0.3.5-alt6
- added bugfix patch from Dmitry Ovechkin <garuda(AT)newmail.ru>.
- s/%buildroot%%buildroot/g in spec file.

* Thu May 22 2003 Anton V. Denisov <avd@altlinux.org> 1:0.3.5-alt5
- minor fixes in start%name script.
- %name-0.3.5-alt-utf8.patch added (now we can use russian titles
	in UTF-8 encoding,
	thanks to Alexandr R.Ogurtzov <isa(AT)mercuri.mk.ua>).
- README.ALT.* updated.

* Tue Mar 25 2003 Anton V. Denisov <avd@altlinux.org> 1:0.3.5-alt4
- start%name script added (now we provide a default configuration
	at first startup).
- %name.menu updated to use start%name.
- added Requires(post,postun): menu (for %%{clean,update}_menus).
- added Requires: XFree86-utils xterm (for start%name script).
- README.ALT updated.
- TODO: incorporate patches from http://linuxhelp.hn.org/%name.php

* Fri Dec 06 2002 Anton V. Denisov <avd@altlinux.ru> 1:0.3.5-alt3
- %name-0.3.5-alt-src-clickinterval.patch fixed (hope now it work
	like must).
- %name-0.3.5-alt-xft2.patch improved (now we use optimization
	flags from rpm).
- Serial:1 added.
- BuildRequires updated for current Sisyphus (thanks to AEN).

* Thu Nov 21 2002 AEN <aen@altlinux.ru> 0.3.5-alt2
- Patch2 for libXft2 support added
- Patch3 -- compile fix

* Thu Nov 21 2002 Anton V. Denisov <avd@altlinux.ru> 0.3.5-alt1
- New version 0.3.5.
- README.ALT updated, renamed and converted into CP1251 too.
- Patches regenerated for new version.
- EXAMPLE.iconfile added.
- Summary and description translated to Russian.
- Url fixed.
- BuildRequires updated.

* Fri Sep 20 2002 Anton V. Denisov <avd@altlinux.ru> 0.22-alt2
- README.ALT added (description of our patches).
- %name-0.22-alt-src-shutdown.patch added
  (doubleclick of 3rd mouse button now shutdowns idesk).

* Tue Sep 17 2002 Anton V. Denisov <avd@altlinux.ru> 0.22-alt1
- Initial release for Sisyphus.

## EOF ##
