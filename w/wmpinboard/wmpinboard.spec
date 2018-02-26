Name: wmpinboard
Version: 1.0
Release: alt7.qa1

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: Window Maker dock applet resembling a miniature pinboard
License: GPL
Group: Graphical desktop/Window Maker

#URL: http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/
URL: http://www.dockapps.org/file.php/id/93

Source0: %url/%name-%version.tar.bz2
Source1: %name.menu
Patch0: %name-%version-alt-unicode.patch
Patch1: %name-%version-fixes.patch

# Automatically added by buildreq on Sun Mar 26 2006
BuildRequires: imake libdnet-devel libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
wmpinboard is a Window Maker dock applet resembling a miniature
pinboard, intended to somewhat relieve heavily littered desktops by
allowing you to place reminders on a graphical on-screen pinboard
rather than producing a mess of real notes all around your keyboard.
Features include support for arbitrary 6x10 X fonts, XLocale support,
drawing capabilities, alarms, animations, themeability, and command
line interoperability.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -D -m 644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc AUTHORS ChangeLog CREDITS INSTALL NEWS README TODO
%doc wmpb-convert.pl wmpinboard.lsm themes-kit
%_bindir/*
%_mandir/man1/*
%_menudir/*

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt7.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmpinboard
  * postclean-05-filetriggers for spec file

* Tue Aug 14 2007 Alexey Voinov <voins@altlinux.ru> 1.0-alt7
- full unicode support
- borrowed fixes from debian
- some warnings fixed
- rusfont patch obsolete

* Sun Mar 26 2006 Alexey Voinov <voins@altlinux.ru> 1.0-alt6
- url now points to dockapps.org, old url is not available
- fixed build with new xorg
- buildreqs updated
- menu updated

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt5
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged
- conditional NoSource added.

* Wed Apr 18 2001 Alexey Voinov <voins@voins.program.ru>
- ugly patch to make koi8-r font default

* Tue Apr 17 2001 Alexey Voinov <voins@voins.program.ru>
- menu added
- Spring 2001 build

* Fri Feb 17 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

