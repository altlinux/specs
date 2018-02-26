%define translations ru be

Name: cog
Version: 0.8.0
Release: alt4.qa1

Summary: GNOME Configurator 
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://www.krakoa.dk/old-linux-software.html#COG

Source: http://www.krakoa.dk/progs/%name/%name-%version.tar.gz
Source1: %name-0.8.0.ru.po
Source2: %name-0.8.0.be.po
#Source3: %name-0.8.0.uk.po

Requires: GConf >= 2.6.0
BuildPreReq: menu-devel rpm-build-licenses

# From configure.in
BuildPreReq: libgnomeui-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.4.0
BuildPreReq: libglade-devel >= 2.3.0
BuildPreReq: libGConf-devel >= 2.6.0
BuildPreReq: gettext-tools 

%description
GNOME Configurator a program for editing advanced GNOME settings in an
easy way.

%prep
%setup -q
cp %SOURCE1 po/ru.po
cp %SOURCE2 po/be.po
#%__cp %SOURCE3 po/uk.po

%__subst 's,\(ALL_LINGUAS=\"\),\1%translations ,' configure*

%build
#export LDFLAGS=-export-dynamic
%configure
%make_build

%install
%makeinstall

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_pixmapsdir/*
%doc AUTHORS NEWS README TODO

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for cog
  * postclean-05-filetriggers for spec file

* Tue May 13 2008 Alexey Rusakov <ktirf@altlinux.org> 0.8.0-alt4
- Removed Debian menu support.
- Squeezed buildreqs, removing obsolete ones.
- Updated Url and License.
- Spec cleanup.

* Wed Mar 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.8.0-alt3
- Updated Russian translation.

* Wed Sep 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt2
- russian and belarussian translations (thanks vk@, slava@)

* Wed Sep 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1
- First build for Sisyphus.

