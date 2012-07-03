%define ver_major 3.4
%define api_ver 3.0
%def_enable introspection

Name: gnome-menus
Version: %ver_major.2
Release: alt1

Summary: GNOME desktop menu
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch1: %name-2.14-alt-add-config-dir.patch
Patch2: %name-alt-applications-menu-no-legacy-kde.patch

BuildPreReq: rpm-build-gnome rpm-build-xdg

# From configure.in
BuildPreReq: intltool >= 0.35 gnome-common
BuildPreReq: libgio-devel >= 2.29.15
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

%description
This package should not be in a repository. If you see this, please file
a bug to http://bugzilla.altlinux.org against gnome-menus component.

%package default
Summary: GNOME Menus common data
License: GPLv2+
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: gnome-menus = %version-%release
Obsoletes: gnome-menus < 2.26.2-alt2

%description default
The package contains an implementation of the draft "Desktop Menu
Specification" from http://www.freedesktop.org/Standards/menu-spec/

%package common
Summary: GNOME Menus common data
License: GPLv2+
Group: Graphical desktop/GNOME
BuildArch: noarch

%description common
The package contains data common to GNOME menus of any ALT Linux
distribution. Normally you should not install this package manually, it
will be installed as a dependency.

%package -n lib%name
Summary: Desktop Menu Library for GNOME
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package provides Desktop Menu Library for GNOME.

%package -n lib%name-devel
Summary: Development files for GNOME Desktop Menu Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Desktop Menu Library.

%package -n lib%name-devel-examples
Summary: Development utilities and examples for GNOME Desktop Menu Library
License: LGPLv2+
Group: Development/Python
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-devel-examples
This package provides some examples that use Desktop Menu Library.

%package -n lib%name-gir
Summary: GObject introspection data for the GNOME Desktop Menu Library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GNOME Desktop Menu Library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GNOME Desktop Menu Library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Desktop Menu Library

%package -n gnome-menu-editor
Summary: A simple GNOME menu editor
Group: Graphical desktop/GNOME

%description -n gnome-menu-editor
This package contains a simple GNOME menu editor.

%prep
%setup -q
%patch1 -p0
%patch2 -p1

%build
%autoreconf
%configure \
    --disable-static \
    %{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

mv %buildroot%_xdgmenusdir/{,gnome3-}applications.menu

%find_lang %name-%api_ver

%files default
%_datadir/desktop-directories/*
#%config %_xdgmenusdir/gnome3-applications.menu

%files common -f %name-%api_ver.lang
%dir %_datadir/gnome-menus

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%if 0
%files -n lib%name-devel-examples
# like the gnome-menu-spec-test
%dir %_datadir/%name/examples
%_datadir/%name/examples/gnome-menus-ls.py
%endif

%define editor_name gmenu-simple-editor

%files -n gnome-menu-editor
%_bindir/%editor_name
%_desktopdir/%editor_name.desktop
%dir %_datadir/gnome-menus/ui
%_datadir/gnome-menus/ui/%editor_name.ui
%dir %python_sitelibdir/GMenuSimpleEditor
%python_sitelibdir/GMenuSimpleEditor/*

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- don't package %%_xdgmenusdir/gnome3-applications.menu due conflict
  with separate altlinux-freedesktop-menu-gnome3 (gnome3-freedesktop-menu)

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.30.5-alt4
- added gnome2-menu-resources subpackage.
  1) to be shared among system and private menu implementations
  2) not included in common to help gnome3 migration.

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.30.5-alt3
- Dropped requires on altlinux-menus
- Dropped symlink /etc/xdg/menus/applications-common.menu

* Wed Mar 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt2
- fixed subpackage dependencies

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sat Apr 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- fixed dependencies

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- introspection support

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.0.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0.1-alt1
- 2.28.0.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Sun Aug 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt2
- ktirf@ in 2.26.2-alt4 (modified alt-applications-menu.patch):
  merge applications-altlinux.menu introduced in altlinux-menus 0.5.0
  (closing ALT #21166).
- ktirf@ in 2.26.2-alt3:
  added settings-merged directory, for System menu customizing
  fix a problem with KDE applications going nuts (closes ALT #21045)
- new devel-examples package

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5

* Mon Jul 27 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2.1
- added unowned directories

* Fri Jul 19 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2
- moved docs to lib%name from %name because lib%name can be used without
  %name
- put locale files to a separate subpackage (-common) to facilitate menu
  structure customization (closes ALT Bug 20797)
- don't use non-standard /etc/gnome/xdg path anymore
  (addresses ALT Bug 20829) - the fix requires a recent gnome-session
  build.
- packages with data were made noarch

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Mon Apr 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt2
- cleanup merging entries (fix #8738 - patch2)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- updated dependencies
- fix link with current python
- use gio for file monitoring (upstream drop support notify, gamin or fam)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.20.2-alt1.1
- Rebuilt with python-2.5.

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)

* Sat Jun 30 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- updated dependencies, removed unneeded Requires
- use a macro for GNOME FTP site

* Sun Jun 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- spec cleanup
- added --enable-inotify switch to the configure script
- removed 'enable_python' switch, Python bindings and a menu editor are
  always built and go to their respective subpackages.

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- added back-compatibility directories in /usr/share/gnome/

* Mon Sep 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt2
- replaced python-dev with python-devel, as told by ALT Python policy.
- fixed Group of python module subpackage, to comply with the policy.

* Sun Aug 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)

* Wed Jun 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version
- applied changes from the bug #9592.

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt1
- new version
- removed gnome-applications.menu file due to Bug #8866.
- introduced fam and gamin switches
- introduced a python bindings package and a menu editor package (both optional and disabled by default).

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Fri Sep 02 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Thu Mar 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1 release.
- hack to use *-gnome-merged as a DefaultMergeDirs.
- *LegacyDirs removed everywhere.
- ALT Linux applications menu merged with original GNOME menu.
- requires altlinux-menus.

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt0.1
- build current cvs snapshot.
- remove applications.menu we have it in altlinux-menus.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92

* Mon Jan 31 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- First build for Sisyphus.

