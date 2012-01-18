%define _name gDesklets
%define menu_group Applications/Monitoring/%_name

Name:    gdesklets
Version: 0.36.3
Release: alt1

Summary: gDesklets - an advanced architecture for desktop applets
License: GPL
Group:   Graphical desktop/GNOME
Url:     http://%name.de
Packager: Andrey Cherepanov <cas@altlinux.org>


Source0: http://gdesklets.de/files/gdesklets-%{version}.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name.watch

Patch1:  %name-alt-desktopfile.patch
Patch2:  %name-transition.patch
Patch3:  %name-vfs.patch

%define gdesklets_dir %_libdir/%name

%add_python_lib_path gdesklets_dir
# provided by libdesklets/system/_glibtopmodule.so
%add_python_req_skip _glibtop
# provided by utils/_systraymodule.so
%add_python_req_skip _systray

# temporarely
Autoreq: yes, nopython
Requires: python%__python_version(libglade)
Requires: python%__python_version(bonobo)
Requires: python%__python_version(gnomecanvas)
Requires: python%__python_version(gconf)
Requires: python%__python_version(ORBit)

# Typical environment for GNOME program
#Requires(post): GConf2
Requires(post,postun): scrollkeeper
BuildPreReq: GConf2

# to avoid rpm-build-python/hasher/apt bug (#4795)
BuildPreReq: python-module-pygnome

# manually removed: eric gcc-g77 gdesklets 
# Automatically added by buildreq on Mon Sep 19 2005 (-bi)
BuildRequires: GConf2 ORBit2-devel fontconfig-devel freetype2-devel gcc-c++ glib2-devel gnome-vfs2-devel libGConf2-devel 
BuildRequires: libart_lgpl-devel libatk-devel libbonobo2-devel libbonoboui-devel libcairo-devel libg2c-devel libglitz-devel libgnome-devel 
BuildRequires: libgnome-keyring-devel libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libgtop2-devel libpango-devel libpng-devel libpopt-devel 
BuildRequires: librsvg-devel libxml2-devel menu-devel perl-XML-Parser pkg-config python-base python-dev python-module-pygnome-devel 
BuildRequires: python-module-pygtk-devel python-module-pyorbit-devel python-modules-compiler python-modules-encodings 
BuildRequires: zlib-devel 
BuildRequires: intltool >= 0.35.0 

%description
gDesklets provides an advanced architecture for desktop applets - tiny
displays sitting on your desktop in a symbiotic relationship of eye
candy and usefulness.

#%package devel
#Summary: Development files for %_name
#Group: Development/C
#Requires: %name = %version-%release

#%description devel
#This package contains files needed to develop desklets and sensors for %_name.


%prep
%setup -q -n gDesklets-%version
%patch1 -p2
%patch2 -p1
%patch3 -p0

# install *.mo files in proper location
#%%__subst 's,\(installdir = \)${coredir},\1$(datadir),' locale/Makefile*
# fix path to locale directory
#%%__subst 's@\(Translator(NAME.lower(), \).*$@\1"/usr/share/locale")@' main/__init__.py

%build
%configure \
	--disable-schemas-install
%make_build

%install
#export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
#mkdir -p %buildroot{%gdesklets_displays_dir,%gdesklets_themes_dir/{Displays,Themes}}
%make_install DESTDIR=%buildroot install
#unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
mkdir -p %buildroot%_liconsdir/ %buildroot%_niconsdir/ %buildroot%_miconsdir/
cp  %buildroot%_libdir/%name/data/%name.png %buildroot%_liconsdir/
install -m 0644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 0644 %SOURCE2 %buildroot%_niconsdir/%name.png

%find_lang --with-gnome %name

%define schemas gdesklets-display-thumbnail

%preun
if [$1 = 0]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc README AUTHORS NEWS ChangeLog
%_bindir/*
%_datadir/applications/*
#%_datadir/application-registry/*
%gdesklets_dir
%_datadir/mime/packages/*
#%_libdir/%name/*
%_iconsdir/gnome/48x48/mimetypes/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_man1dir/*
##%config %_sysconfdir/gconf/schemas/*
%_sysconfdir/xdg/autostart/*.desktop

#%files devel
#%_pkgconfigdir/*

%changelog
* Wed Jan 18 2012 Andrey Cherepanov <cas@altlinux.org> 0.36.3-alt1
- New version 0.36.3
- Add watch file
- Apply patches from Fedora
- Pack autostart file

* Wed Jan 18 2012 Andrey Cherepanov <cas@altlinux.org> 0.36.1-alt1.2.qa1.1
- new version 0.36.3

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.36.1-alt1.2.qa1
- Fix librsvg-devel requirement

* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.36.1-alt1.2
- NMU: removed debian menu, fixed categories, xorg-devel...

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36.1-alt1.1
- Rebuilt with python 2.6

* Thu Nov 20 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.36.1-alt1
- New version 0.36.1
- Apply repocop patch

* Fri Oct 17 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.36-alt4
- Some changes in desktop-file

* Fri Oct 03 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.36-alt3
- Added icons
- Update buildreq
- Added menu-related additional categories

* Thu Sep 11 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.36-alt2
- Apply repocop patch
- Some changes in spec file

* Sun Aug 31 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.36-alt1
- New version

* Sun Sep 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.35.2-alt0.1
- new version

* Fri Jul 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.26.2-alt0.2
- move all desklets to Applications/Monitoring in menu hierarhy.
- use freedesktop2menu.pl to build menu file.
- update buildreqs to fix python dependencies.

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.26.2-alt0.1
- 0.26.2

* Fri Feb 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.26-alt0.1
- 0.26

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.25.1-alt0.1
- 0.25.1

* Mon Nov 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.24-alt0.1
- First build for Sisyphus.
