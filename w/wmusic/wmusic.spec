Name:		wmusic
Version:	1.5.0
Release:	alt4.1
Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	wmusic is a dockapp that remote-controls xmms
Group:		Graphical desktop/Window Maker
License: 	GPL
Url: 		http://home.jtan.com/~john/wmusic
Source0: 	%name-%version.tar.bz2
Source1: 	%name.menu
Source3:	%name-README.ALT
Patch0:   %name-1.5.0-alt-DSO.patch

# Automatically added by buildreq on Thu Jan 04 2007
BuildRequires: imake librcc-gtk libxmms-devel libX11-devel libXext-devel libXpm-devel libXt-devel libXxf86dga-devel libXxf86vm-devel xorg-cf-files

%description 
wmusic is a dockapp that remote-controls xmms. Here is a list of the features:

- VCR style controls including fast rewind and fast forward
- Time and Playlist position display
- Super stylee rotating arrow
- Hiding of the xmms windows (on startup and through middle-click)
- Multi-threaded

%prep
%setup -q
%patch0 -p2
cp %SOURCE3 ./README.ALT


%build
%configure
%make_build

%install
make PREFIX=$RPM_BUILD_ROOT%_prefix install
install -p -D -m644 debian/%name.1 $RPM_BUILD_ROOT%_man1dir/wmusic.1
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README README.ALT
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt4.1
- Fixed build

* Mon Nov 09 2009 Alexey Voinov <voins@altlinux.ru> 1.5.0-alt4
- update_menus removed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt3.1
- NMU:
  * updated build dependencies

* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 1.5.0-alt3
- menu file fixed

* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 1.5.0-alt2
- /usr/X11R6 -> /usr
- buildreqs updated

* Wed Mar 03 2004 Alexey Voinov <voins@altlinux.ru> 1.5.0-alt1
- new version (1.5.0) 

* Thu Feb 26 2004 Alexey Voinov <voins@altlinux.ru> 1.4.14-alt1
- new version (1.4.14)
- wmusic.1 is back in tarball :)

* Wed Feb 25 2004 Alexey Voinov <voins@altlinux.ru> 1.4.13-alt1
- new version (1.4.13)
- i18n patch got merged into upstream
- wmusic.1 manpage extracted from 1.4.12 (it's gone in 1.4.13)

* Sat Feb 07 2004 Alexey Voinov <voins@altlinux.ru> 1.4.12-alt1
- new version (1.4.12)
- i18n patch updated (cyr_yo added, applies to 1.4.12)

* Sat Mar 22 2003 Alexey Voinov <voins@voins.program.ru> 1.4.11-alt1
- new version (1.4.11)
- i18n patch updated (it will not conflict with new volume slider)

* Mon Dec 02 2002 Alexey Voinov <voins@voins.program.ru> 1.4.10-alt3
- i18n patch updated (thanks to Michael Shigorin <mike@osdn.org.ua>)

* Sat Nov 30 2002 Alexey Voinov <voins@voins.program.ru> 1.4.10-alt2
- ukrainian letters added to i18n-patch

* Wed Oct 09 2002 Alexey Voinov <voins@voins.program.ru> 1.4.10-alt1
- new version(1.4.10)
- arrays patch no longer needed
- i18n patch added (allows easy adding of new glyphs to internal font, 
  russian alphabet added)
- README.ALT added

* Thu Oct 03 2002 Alexey Voinov <voins@voins.program.ru> 1.4.9-alt1
- new version (1.4.9)
- buildreqs updated
- little spec cleanup
- url changed
- arrays patch added

* Tue Sep 11 2001 Alexey Voinov <voins@voins.program.ru>
- initial build
