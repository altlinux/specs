Name: wmupmon
Version: 0.1.3
Release: alt5

Summary: A dockapp to monitor system uptime
License: GPL
Group: Graphical desktop/Window Maker

Url: http://freshmeat.net/projects/wmupmon/
Source0: http://j-z-s.com/projects/downloads/%name-%version.tar.bz2
Source1: %name.menu
Patch0: %name-0.1.3-alt-warnings-fix.patch
Patch1: %name-0.1.2-alt-src-memory_leak_fix.patch

Packager: Alexey Voinov <voins@altlinux.ru>

# Automatically added by buildreq on Sun Mar 26 2006
BuildRequires: imake libICE-devel libX11-devel libXext-devel libXpm-devel libXt-devel xorg-cf-files xorg-proto-devel

%description
wmupmon is a program to monitor system uptime. It is a dockapp that is
supported by X window managers such as Window Maker, AfterStep, BlackBox,
Waimea, and Enlightenment.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure
make

%install
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README INSTALL ChangeLog THANKS AUTHORS NEWS
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Mon Jan 12 2015 Michael Shigorin <mike@altlinux.org> 0.1.3-alt5
- updated an URL (closes: #20235)
- minor spec cleanup

* Sun Apr 14 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt4.1
- Fix build with new xorg

* Wed Nov 04 2009 Alexey Voinov <voins@altlinux.ru> 0.1.3-alt4
- update_menus removed

* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 0.1.3-alt3
- menu file fixed, finally :) [#8162] (thanks to php-coder@)

* Sun Mar 26 2006 Alexey Voinov <voins@altlinux.ru> 0.1.3-alt2
- menu file updated, warnings suppressed [#8162] (thanks to php-coder@)
- memory leak fixed [#8971] (thanks to php-coder@)
- buildreqs updated

* Sat Sep 03 2005 Alexey Voinov <voins@altlinux.ru> 0.1.3-alt1
- new version (0.1.3) [#7678]
- url updated         [#7679]

* Mon Oct 06 2003 Alexey Voinov <voins@altlinux.ru> 0.1.1a-alt1
- new version
- buildreq fixed

* Mon May 26 2003  Alexey Voinov <voins@altlinux.ru> 0.1.0-alt1
- initial build

