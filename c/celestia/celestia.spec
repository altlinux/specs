Name: celestia
Version: 1.6.1
Release: alt2.1
License: GPL
Group: Education
Summary: A real-time visual space simulation
URL: http://www.shatters.net/celestia/
Source: %{name}-%{version}.tar.gz
Patch1: celestia-1.4.0-desktop-fix.patch
Patch2: celestia-1.6.1-alt-gcc4.6.patch
Patch3: celestia-1.6.1-alt-DSO.patch

BuildRequires: fontconfig freetype2 gcc-c++ kdelibs-devel libtqt-devel
BuildRequires: libjpeg-devel libpng-devel libqt3-devel
BuildRequires: libqt3-settings libstdc++-devel xml-utils 
BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXau-devel, libXaw-devel, libXrandr-devel, libXdmcp-devel, libXext-devel, libXfixes-devel, libXfont-devel, libXft-devel, libXi-devel, libXmu-devel, libXpm-devel, libXrender-devel, libXres-devel, libXScrnSaver-devel, libXinerama-devel, libXt-devel, libXtst-devel, libXxf86dga-devel, libXcomposite-devel, libXxf86vm-devel, libdmx-devel, libfontenc-devel, libGLU-devel, libXdamage-devel, libxkbfile-devel, xcursorgen, xorg-font-utils, libXvMC-devel, libXcursor-devel, libXevie-devel, libXv-devel, xorg-xtrans-devel, xorg-util-macros, xorg-sgml-doctools, xorg-compat-devel
BuildRequires: zlib-devel liblua5-devel libtheora-devel

BuildRequires: libGConf2-devel GConf libgtk+2-devel glib-devel libgnomeui-devel libgtkglext-devel
Requires(post): GConf
Requires: libpng12 >= 1.2.38 


%description
Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package common
Group: Education
Summary: A real-time visual space simulation (common part)
Requires: celestia-ui = %version-%release
Obsoletes: celestia

%description common
This is a common part of Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package kde
Group: Education
Summary: A real-time visual space simulation (KDE frontend)
Requires: celestia-common = %version-%release
Provides: celestia-ui = %version-%release
Provides: celestia
Obsoletes: celestia

%description kde
This is a KDE3 frontend to Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.


%package gnome
Group: Education
Summary: A real-time visual space simulation (GNOME frontend)
Requires: celestia-common = %version-%release
Provides: celestia-ui = %version-%release

%description gnome
This is a GNOME frontend ro Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.


%prep
%setup -q 
%patch1 -p0
%patch2 -p2
%patch3 -p2
##%__aclocal --force
##%__automake --foreign
autoreconf
##%__subst 's,\.la,\.so,' configure


%build
PATH=$PATH:/usr/lib/kde3/
export PATH
%add_optflags -fpermissive
%configure --disable-rpath --with-kde --without-arts
make echo=echo
mv src/celestia/celestia src/celestia/celestia-kde
mkdir -p  %buildroot{%_bindir,%_datadir,%_desktopdir,%_liconsdir}
make install DESTDIR=%buildroot echo=echo


make clean
%configure --disable-rpath --with-gnome --without-arts
make echo=echo


export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_SCHEMA_FILE_DIR="%{buildroot}%{_sysconfdir}/gconf/schemas"
make install DESTDIR=%buildroot echo=echo
## По непонятной (пока?) причине, файлы дублируются в каталоге %buildroot%buildroot
%__rm -f %buildroot%buildroot
find %buildroot%_datadir -name %{name}.desktop -exec rm {} \;
%__install src/celestia/kde/data/%{name}.desktop %buildroot%_desktopdir
install -D -m 644 src/celestia/gtk/data/%{name}.png %buildroot%_liconsdir/%{name}.png
install -m 755 src/celestia/celestia-kde %buildroot/%_bindir
install -m 755 src/celestia/celestia %buildroot/%_bindir/celestia-gnome
rm %buildroot/%_bindir/celestia

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-kde <<__EOF__
%_bindir/celestia      %_bindir/celestia-kde 20
__EOF__

cat >%buildroot/etc/alternatives/packages.d/%name-gnome <<__EOF__
%_bindir/celestia      %_bindir/celestia-gnome 10
__EOF__

%find_lang %{name}
##(cd %buildroot/%_datadir/apps && symlinks -c .)

%pre
[ ! -d %_datadir/apps/%name ] || %__rm -fr %_datadir/apps/%name

%post gnome
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :

%preun gnome
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :

%files -f %{name}.lang common
%_datadir/apps/*
%_datadir/applnk/*
%_datadir/config/*
## %_datadir/locale/*
%_datadir/locale/*/*/celestia_constellations.mo
%_datadir/mimelnk/*
%_datadir/services/*
%_datadir/%{name}
%_liconsdir/%{name}.png
%_desktopdir/%{name}.desktop
%doc ChangeLog TRANSLATORS README NEWS 

%files gnome
%_bindir/celestia-gnome
/etc/gconf/schemas/celestia.schemas
/etc/alternatives/packages.d/%name-gnome

%files kde
%_bindir/celestia-kde
/etc/alternatives/packages.d/%name-kde

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.6.1-alt2
- Build for TDE 3.5.13 release

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6.1
- build fixd

* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6
- build fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt5
- build fixed

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for celestia
  * postclean-05-filetriggers for spec file

* Tue Aug 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt4
- encoding bug fixed

* Wed Aug 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt3
- Theora support added
- two subpackages for gnome and kde interfaces

* Mon Aug 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- russian in bookmarks fixed

* Mon Jul 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- release 1.6.0

* Tue Jun 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1.1
- rebuild with libpng.git=1.2.37-alt2 

* Mon Jun 08 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1
- release 1.5.1

* Fri Feb 22 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt2
- add i18n to new release

* Wed Feb 20 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt1
- release 1.5.0

* Fri Oct 19 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt5
- fix requirement

* Thu Oct 18 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt4
- added requirement to GConf2

* Mon Apr 09 2007 Eugine V. Kosenko <maverik@altlinux.ru> 1.4.1-alt3.i18n
- add trial i18n (fonts and fixes)

* Mon May 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt2
- fix compile woth gcc4.1 (patch from fedoraproject.org)

* Sat Mar 25 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Mar 12 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt2
- fixed build with LDFLAGS="-Wl,--as-needed"
- removed .la->.so replacement
- fixed update from previous versions (thanks to shrek@)

* Sat Feb 18 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt1
- new version (1.4.0)
- rebuild with new xorg (#8813)
- menu-file replaced with celestia.desktop
- installation fix (/usr/share/apps/celestia -> /usr/share/celestia)

* Tue Jan 18 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.3.2-alt2
- this build make more gcc3.4 compatible

* Wed Sep 22 2004 Eugene V. Horohorin <genix@altlinux.org> 1.3.2-alt1
- new version

* Wed Jun 23 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt2
- spec clean up

* Sat May 08 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt1
- First build.

