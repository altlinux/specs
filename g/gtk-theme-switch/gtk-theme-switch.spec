Name: gtk-theme-switch
Version: 2.0.0
Release: alt0.3.qa2

%define beta rc2

Summary: Switch GTK themes on the fly
License: GPL
Group: Graphical desktop/GNOME

Url: http://www.muhri.net/nav.php3?node=gts
Packager: Evgenii Terechkov <evg@altlinux.ru>

Source0: %name-%version%beta.tar.gz
Source1: %name.desktop
Patch: gtk-theme-switch-2.0.0_rc2-gtk+-2.4_fix.patch

# Automatically added by buildreq on Tue Jan 16 2007
BuildRequires: libgtk+2-devel

%description
Tiny app to let you switch GTK2 themes on the fly.

%prep
%setup -q -n %name-%version%beta
%patch

%build
%make

%install
install -pD switch2 %buildroot%_bindir/%name
install -pD switch.1 %buildroot%_man1dir/%name.1
install -pD %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop

%changelog
* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt0.3.qa2
NMU: polished desktop file

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.0-alt0.3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gtk-theme-switch
  * postclean-05-filetriggers for spec file

* Thu Aug 23 2007 Terechkov Evgenii <evg@altlinux.ru> 2.0.0-alt0.3
- desktop file updated (Fixes #12591)
- Spec translations removed (Specspo)
- Packager tag added

* Tue Jan 16 2007 Michael Shigorin <mike@altlinux.org> 2.0.0-alt0.2
- 2.0.0rc2 (GTK2 only; if you need GTK1 (1.0.x), please get a package
  from 3.0 or 2.x) -- fixes #10668
- replaced Debian menu file with freedesktop one (from Sourcemage)
- dropped old makefile patch, added another one from Gentoo
- buildreq (one should do that once in four years, right?)
- NB: the fact that I've missed the major new version should
  tell someone more interested to take the package over

* Fri Dec 27 2002 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt1
- built for ALT Linux
- spec adapted from Cooker and *severely* cleaned up
- adresses #1771 ("addendum")

* Tue Jul 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- wrap too long description
- fix mandir location
- fix menu entry (section & default icon)
- from Austin Acton <aacton@yorku.ca> :
	- initial package creation for MDK 8.2+
