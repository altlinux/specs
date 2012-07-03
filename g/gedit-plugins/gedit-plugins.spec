%define ver_major 3.4
%def_enable python
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins
Version: %ver_major.0
Release: alt1

Summary: Plugins for GEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.in
%define glib_ver 2.31.0
%define gtk_ver 3.3.7
%define gtksourceview_ver 3.3.0
%define gedit_ver 3.3.7
%define peas_ver 1.2.0

BuildPreReq: rpm-build-gnome >= 0.6

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-doc-utils >= 0.3.2
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgtksourceview3-devel >= %gtksourceview_ver
BuildPreReq: gedit-devel >= %gedit_ver
BuildPreReq: libpeas-devel >= %peas_ver
# For Charmap plugin
BuildPreReq: libgucharmap-devel >= 3.0.0
%{?_enable_python:BuildRequires: python-module-pygobject3-devel}
BuildRequires: libSM-devel libxml2-devel python-module-dbus-devel libvte3-devel

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

It includes such features as split-screen mode, a plugin API, which
allows gEdit to be extended to support many features while remaining
small at its core, multiple document editing through the use of a
'tabbed' notebook and many more functions.

This package contains various plugins for gEdit, including Charmap, Terminal, and others.

%prep
%setup -q

%build
%configure \
    --disable-static \
    --disable-schemas-compile \

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome --output=files_list %name

# All the dancing below is about potential splitting of plugins into
# subpackages.
%define fill_plugin_fileset() \
for f in %{1}.{plugin,py,pyc,pyo} lib%{1}.so; do \
    [ -r "%buildroot%gedit_pluginsdir/$f" ] && echo "%gedit_pluginsdir/$f"; \
done >>files_list_%{1}; \
if [ -d "%buildroot%gedit_pluginsdir/%{1}" ]; then \
    echo "%%dir %gedit_pluginsdir/%{1}" \
    for e in py pyc pyo; do \
        [ -r "%buildroot%gedit_pluginsdir/%{1}" ] && \
            echo "%gedit_pluginsdir/%{1}/*.$e" \
    done \
fi >>files_list_%{1}

%define plugins bookmarks drawspaces dashboard bracketcompletion charmap codecomment colorpicker gpdefs joinlines showtabbar smartspaces terminal multiedit wordcompletion sessionsaver commander textsize synctex taglist

# commander plugin has subdirectories
echo "%gedit_pluginsdir/commander/commands/" > files_list_commander

for p in %plugins; do
    %fill_plugin_fileset $p
    cat files_list_$p >>files_list
done

%files -f files_list
%dir %_datadir/gedit/plugins
%_datadir/gedit/plugins/*
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml

%exclude %gedit_pluginsdir/*.la

%changelog
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

