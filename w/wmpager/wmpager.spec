# vim: set ft=spec: -*- rpm-spec -*-
# $Id: wmpager,v 1.2 2006/02/06 07:47:20 raorn Exp $

Summary: Simple pager docklet for the WindowMaker
Name: wmpager
Version: 1.2
Release: alt5.qa1
Group: Graphical desktop/Window Maker
License: BSD
URL: http://wmpager.sourceforge.net/

Conflicts: WindowMaker < 0.91.0

Source: http://download.sourceforge.net/%name/%name-%version.tar.gz

Patch: %name-1.2-alt-tooltip.patch
Patch1: %name-1.2-alt-EWMH.patch

# Automatically added by buildreq on Mon Feb 06 2006
BuildRequires: libX11-devel libXext-devel libXpm-devel xorg-x11-proto-devel

%description
%name is a simple pager docklet for the Window Maker.

%name offers the following features:

 * convenient workspace switching using the mouse for up to nine workspaces

 * automatic configuration according to the number of workspaces (you may
   however if you like also specify the number of workspaces and the layour of
   wmpager yourself)

 * automagic adjustment to the currently active workspace (if you happen to
   switch workspaces using the keyboard or some other Window Maker means)

 * configurable look and feel to match your Window Maker theme

 * tooltips for the workspace names (if you happen to have to many workspaces
   and can't remember which is which ;-))

%prep
%setup -q
%patch -p1
sed -i 's,/usr/local/share/wmpager,%_datadir/%name,' src/wmpager.c
%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot{%_bindir,%_man1dir,%_datadir/%name,%_menudir}
install -m755 src/wmpager %buildroot%_bindir/%name
install -m644 man/man1/wmpager.1x %buildroot%_man1dir/%name.1x
install -m644 themes/*.xpm %buildroot%_datadir/%name

cat <<__EOF > %buildroot%_menudir/%name
?package(%name): command="EXEC %_bindir/%name" \
	needs=wmaker \
	section="Window Maker/DockApps" title="%name"
__EOF

%files
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_man1dir/%name.1*
%_menudir/%name

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmpager
  * postclean-03-private-rpm-macros for ([not specified])

* Mon Feb 06 2006 Sir Raorn <raorn@altlinux.ru> 1.2-alt5
- Rebuilt with new Xorg, buildreqs updated

* Sat Jun 04 2005 Sir Raorn <raorn@altlinux.ru> 1.2-alt4
- EWMH support
- Temporary disabled tooltips

* Tue Jan 21 2003 Sir Raorn <raorn@altlinux.ru> 1.2-alt3
- Fix SEGV when "dragging" button with enabled tooltips

* Thu Sep 12 2002 Sir Raorn <raorn@altlinux.ru> 1.2-alt2
- Argh! Fix subst operation (I'm too lazy to make patch for it...)

* Thu Sep 12 2002 Sir Raorn <raorn@altlinux.ru> 1.2-alt1
- Built for Sisyphys


