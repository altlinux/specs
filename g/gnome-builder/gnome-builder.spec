%define _name org.gnome.Builder
%define ver_major 3.18
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

Name: gnome-builder
Version: %ver_major.1
Release: alt1

Summary: Builder - Develop software for GNOME
License: LGPLv2+
Group: Development/GNOME and GTK+
Url: https://wiki.gnome.org/Apps/Builder

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%set_typelibdir %_libdir/%name/girepository-1.0

%define gtk_ver 3.17.8
%define gtksourceview_ver 3.17.8
%define git2_ver 0.23.5
%define devhelp_ver 3.16.0
%define gjs_ver 1.42
%define xml_ver 2.9.0
%define vala_ver 0.30

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_compile_include %_libdir/%name/plugins

PreReq: %name-data = %version-%release
Requires: devhelp uncrustify ctags
Requires: libpeas-python3-loader

BuildRequires: /proc gcc-c++ intltool yelp-tools gtk-doc libappstream-glib-devel
BuildRequires: clang-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview3-devel >= %gtksourceview_ver
BuildRequires: libgit2-glib-devel >= %git2_ver libdevhelp-devel >= %devhelp_ver
BuildRequires: libpcre-devel libgjs-devel >= %gjs_ver libwebkit2gtk-devel
BuildRequires: libxml2-devel >= %xml_ver libpeas-devel libvte3-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgtksourceview3-gir-devel libgit2-glib-gir-devel libpeas-gir-devel
BuildRequires: libvala-devel >= %vala_ver vala-tools

%description
Builder attempts to be an IDE for writing software for GNOME. It does not
try to be a generic IDE, but one specialized for writing GNOME software.
We believe that this focus will help us to build something great.

%package data
Summary: Arch independent files for GNOME Builder
Group: Development/GNOME and GTK+
BuildArch: noarch

%description data
This package provides noarch data needed for Gnome Builder to work.


%prep
%setup

%build
export CFLAGS="$CFLAGS `pkg-config --cflags libpcre`"
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/ide-build
%_libexecdir/%name/ide-list-build-flags
%_libexecdir/%name/ide-list-counters
%_libexecdir/%name/ide-list-devices
%_libexecdir/%name/ide-list-diagnostics
%_libexecdir/%name/ide-list-file-settings
%_libexecdir/%name/ide-list-files
%_libexecdir/%name/ide-mine-projects
%_libexecdir/%name/ide-search
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libautotools-plugin.so
%_libdir/%name/plugins/libclang-plugin.so
%_libdir/%name/plugins/libcommand-bar.so
%_libdir/%name/plugins/libc-pack-plugin.so
%_libdir/%name/plugins/libctags-plugin.so
%_libdir/%name/plugins/libdevhelp-plugin.so
%_libdir/%name/plugins/libfallback-plugin.so
%_libdir/%name/plugins/libfile-search.so
%_libdir/%name/plugins/libgnome-code-assistance-plugin.so
%_libdir/%name/plugins/libhtml-completion-plugin.so
%_libdir/%name/plugins/libpython-pack-plugin.so
%_libdir/%name/plugins/libsymbol-tree.so
%_libdir/%name/plugins/libsysmon.so
%_libdir/%name/plugins/libterminal.so
%_libdir/%name/plugins/libvala-pack-plugin.so
%_libdir/%name/plugins/libxml-pack-plugin.so
%_libdir/%name/plugins/jedi_plugin.py
%_libdir/%name/plugins/python_gi_imports_completion.py
%_libdir/%name/plugins/__pycache__/
%_libdir/%name/plugins/html_preview_plugin/
%_libdir/%name/plugins/*.plugin
%exclude %_libdir/%name/plugins/*.la
#%files -n libide
%_libdir/%name/libide-%api_ver.so
%_libdir/%name/libegg-private.so.*
%_libdir/%name/libgnome-builder.so.*
%_libdir/%name/librg.so.*
%_libdir/%name/libsearch.so.*

%exclude %_libdir/%name/*.la
%exclude %_libdir/%name/libegg-private.so
%exclude %_libdir/%name/libgnome-builder.so
%exclude %_libdir/%name/librg.so
%exclude %_libdir/%name/libsearch.so

#%files -n libide-gir
%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Egg-%api_ver.typelib
%_libdir/%name/girepository-1.0/Ide-%api_ver.typelib
%_libdir/%name/girepository-1.0/Builder-%api_ver.typelib
%doc README AUTHORS NEWS

%files data
%_desktopdir/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%_datadir/gtksourceview-3.0/styles/*.xml
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/builder.png
%_iconsdir/hicolor/scalable/apps/builder-symbolic.svg
%_datadir/appdata/%_name.appdata.xml

#%files -n libide-devel
%exclude %_pkgconfigdir/libide-%api_ver.pc

#%files -n libide-gir-devel
#%exclude %_girdir/Ide-%api_ver.gir
#%exclude %_girdir/Builder-%api_ver.gir

#%files -n libide-devel-doc
%exclude %_datadir/gtk-doc/html/libide/

%changelog
* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Fri May 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt0.1
- 3.16.3_c04d920e

* Fri Apr 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Mon Jan 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4.1-alt1
- first preview for people/gnome

