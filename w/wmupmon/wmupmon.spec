Name: wmupmon
Version: 0.1.3
Release: alt4

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: A dockapp to monitor system uptime
License: GPL
Group: Graphical desktop/Window Maker
Url: http://j-z-s.com/projects/index.php?project=wmupmon

Source0: http://j-z-s.com/projects/downloads/%name-%version.tar.bz2
Source1: %name.menu

Patch0: %name-0.1.3-alt-warnings-fix.patch
Patch1: %name-0.1.2-alt-src-memory_leak_fix.patch

# Automatically added by buildreq on Sun Mar 26 2006
BuildRequires: imake libICE-devel libX11-devel libXext-devel libXpm-devel libXt-devel xorg-cf-files xorg-x11-proto-devel

%description
wmupmon  is a program to monitor system uptime. It is a dockapp that is
supported by X window managers such as Window Maker, AfterStep,  BlackBox,
Waimea, and Enlightenment.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make

%install
%makeinstall
install -D -pm644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name


%files
%doc README INSTALL ChangeLog THANKS AUTHORS NEWS
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
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

