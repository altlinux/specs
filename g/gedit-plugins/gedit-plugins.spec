%def_disable snapshot

%define ver_major 44
%define beta %nil
%def_enable python
# removed since 3.36
%def_disable zeitgeist
%define gedit_pluginsdir %_libdir/gedit/plugins
%add_python3_path %gedit_pluginsdir

Name: gedit-plugins
Version: %ver_major.1
Release: alt1%beta

Summary: Plugins for GEdit
License: GPL-2.0
Group: Editors
Url: https://wiki.gnome.org/Apps/Gedit/ShippedPlugins

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.40.0
%define gtk_ver 3.24
%define gtksourceview_ver 4.8.4
%define gedit_ver 44.0
%define peas_ver 1.14.1
%define git2_ver 0.0.12
%define vte_ver 0.38

Requires: gedit >= %ver_major
Requires: libpeas-python3-loader
Requires: libvte3-gir >= %vte_ver
%{?_enable_zeitgeist:Requires: zeitgeist}

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-gnome
BuildRequires: meson gnome-common libappstream-glib-devel
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview4-devel >= %gtksourceview_ver
BuildRequires: gedit-devel >= %gedit_ver
BuildRequires: libpeas-devel >= %peas_ver
BuildRequires: yelp-tools
# for git plugin
BuildRequires: libgit2-glib-devel >= %git2_ver
# for Charmap plugin
BuildRequires: libgucharmap-devel >= 3.0.0 libgucharmap-gir-devel
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel libzeitgeist2.0-gir-devel}
%if_enabled python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pygobject3-devel
%endif
BuildRequires: libxml2-devel python3-module-dbus-devel libvte3-gir-devel

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

It includes such features as split-screen mode, a plugin API, which
allows gEdit to be extended to support many features while remaining
small at its core, multiple document editing through the use of a
'tabbed' notebook and many more functions.

This package contains various plugins for gEdit, including Charmap, Terminal, and others.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang gedit %name

%files -f %name.lang
%dir %_datadir/gedit/plugins
%_datadir/gedit/plugins/*
%gedit_pluginsdir/*
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
#%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.translate.gschema.xml
%_datadir/metainfo/gedit-*.metainfo.xml


%changelog
* Fri Jan 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Mon Jan 02 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Mon Apr 04 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Wed Apr 28 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Mar 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed May 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu Apr 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.28.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun May 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- used %%_python3_path instead of %%_python3_compile_include

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Thu Nov 06 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- updated to 3.14.0_811c94af

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu Apr 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt2
- rebuilt to update dependencies

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Apr 23 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Mar 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.4-alt1
- 3.3.4

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Sep 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Sun Aug 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Fri Jun 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu Apr 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.2-alt1
- 2.91.2

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sun Jan 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Fri Dec 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.0-alt1.1
- Rebuilt with python 2.6

* Sat Sep 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Jul 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Sun Oct 26 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- new version

* Fri Oct 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.4-alt1
- new version

* Wed Oct 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Sun Mar 23 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 2.20.0-alt1.1
- Rebuilt with python-2.5.

* Mon Dec 03 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version (2.20.0)

* Mon Jul 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- use %%gedit_pluginsdir macro from rpm-build-gnome-0.6
- updated dependencies
- mention plugins explicitly in the files list (one step towards plugins split
  out into subpackages).

* Mon Oct 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1.1
- rebuild

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Mon Sep 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.5-alt1
- Initial Sisyphus package

