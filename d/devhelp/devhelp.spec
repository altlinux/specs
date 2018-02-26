%define ver_major 3.4

Name: devhelp
Version: %ver_major.0
Release: alt1

Summary: Developer's help program
Summary(be_BY.UTF-8): Сыстэма даведкі для распрацоўніка ў асяродьдзі GNOME
Summary(ru_RU.UTF-8): Справочная система для разработчика в среде GNOME
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
License: %gpl2plus
Group: Development/Other
Url: http://www.gnome.org
#VCS: git:git://git.gnome.org/devhelp
Source: %name-%version.tar

# From configure.in
%define gtk_ver 3.0.2
%define GConf_ver 2.6.0

Requires: lib%name = %version-%release

BuildPreReq: rpm-build-gnome >= 0.6 gnome-common
BuildPreReq: rpm-build-licenses
BuildPreReq: gtk-doc

# From configure.in
BuildPreReq: intltool >= 0.40.0
BuildPreReq: glib2-devel >= 2.25.11
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: GConf libGConf-devel >= %GConf_ver
BuildPreReq: libwebkitgtk3-devel
BuildPreReq: zlib-devel
BuildPreReq: gettext-tools

%description
A developers help program.

%description -l be_BY.UTF-8
Даведкавая сыстэма для распрацоўніка у асяродзьдзі GNOME.

%description -l ru_RU.UTF-8
Справочная система для разработчика в среде GNOME.

%package -n lib%name
Summary: Devhelp widgets library
Summary(be_BY.UTF-8): Бібліятэка віджэтаў Devhelp
Summary(ru_RU.UTF-8): Библиотека виджетов Devhelp
Group: System/Libraries

%description -n lib%name
This package provides shared library required for Devhelp to work.

%description -l be_BY.UTF-8 -n lib%name
Гэты пакет утрымлівае неабходную для працы Devhelp бібіліятэку.

%description -l ru_RU.UTF-8 -n lib%name
Пакет предостовляет необходимую для работы  Devhelp библиотеку.

%package -n lib%name-devel
Summary: Devhelp widgets headers
Summary(be_BY.UTF-8):	Файлы распрацоўкі патрэбныя для пабудовы дастасаваньняў з %name
Summary(ru_RU.UTF-8):	Файлы разработки нужные для построения приложений с %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Devhelp widgets.

%description -n lib%name-devel -l be_BY.UTF-8
Файлы распрацоўкі патрэбныя для пабудовы дастасаваньняў з %name

%description -n lib%name-devel -l ru_RU.UTF-8
Файлы разработки нужные для построения приложений с %name

%package -n gedit-plugin-%name
Summary: DevHelp integration into GEdit
Group: Development/Other

%description -n gedit-plugin-%name
This plugin for GEdit enables using DevHelp from inside the editor.

%define _devhelpdir %_datadir/%name
%define  gedit_pluginsdir %_libdir/gedit/plugins

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--disable-schemas-install

%make_build

%install
%make_install install DESTDIR=%buildroot

# Create some directories in %name hierarchy
mkdir -p %buildroot%_devhelpdir/{specs,books}

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%dir %_devhelpdir
%_devhelpdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/devhelp.*
%config %gconf_schemasdir/*
%doc AUTHORS COPYING NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/lib%name-*.pc

%files -n gedit-plugin-%name
%gedit_pluginsdir/*

%changelog
* Thu Apr 05 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt1.1
- Rebuild with Python-2.7

* Thu May 26 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.92-alt1
- 2.91.92

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt2
- add default value for books_disabled to GConf schema

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Mon Sep 13 2010 Alexey Shabalin <shaba@altlinux.ru> 2.31.92-alt1
- 2.31.92

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Wed Feb 10 2010 Alexey Shabalin <shaba@altlinux.ru> 0.29.90-alt1
- 0.29.90

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28.1-alt1.1
- Rebuilt with python 2.6

* Tue Oct 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.1-alt1
- 0.28.1

* Mon Sep 28 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.0.1-alt1
- 0.28.0.1

* Mon Sep 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.0-alt1
- 0.28.0

* Tue Aug 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.23.1-alt1
- 0.23.1

* Fri Apr 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.23-alt1
- 0.23
- cleanup spec (drop all about cvsdate)

* Sat Dec 06 2008 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22 (move to WebKit)

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt2
- 0.21
- fixed build for x86_64

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu Jul 10 2008 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- new version
- build against xulrunner.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for devhelp
 * update_menus for devhelp

* Mon Feb 25 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt2
- Rebuilt with Python 2.5.

* Mon Feb 11 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Tue Jan 08 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- New version (0.17).
- The patch for the .pc file went upstream.
- Updated dependencies.

* Tue Oct 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16.1-alt1
- new version (0.16.1)
- fixed excess dependencies mentioned in the .pc file.

* Mon Sep 10 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- new version (0.16)
- more macros used, including license macro.

* Sat Jun 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14-alt1
- new version (0.14)
- updated dependencies
- package GEdit plugin

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.13-alt1
- new version 0.13 (with rpmrb script)

* Tue Dec 19 2006 Alexey Rusakov <ktirf@altlinux.org> 0.12-alt2
- switch Gecko backend to Firefox.
- minor cleanup.

* Fri Jul 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.12-alt1
- new version 0.12.
- updated files list (GEdit plugin is not included yet).

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.11-alt1
- new version (0.11)
- cleaned up the spec, revised dependencies
- introduced gecko_provider switch (choose from mozilla, seamonkey, FF, and TB).
- removed Debian menu support.

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.10-alt1
- 0.10

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue Aug 17 2004 Vital Khilko <vk@altlinux.ru> 0.9.1-alt2
- updated belarusian translations.

* Sun Jul 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- 0.9.1
- use freedesktop2menu.pl to build menu file.
- updated translations.

* Fri Jul 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1.1
- rebuild against new mozilla-1.7

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1
- 0.9

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt2
- fixed buildreqs.

* Sun Jun 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Mon Apr 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Mar 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt0.7
- 0.5.0

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.99-alt0.6cvs20030204
- gnome2 version from cvs crashes on startup.

* Sun May 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.
