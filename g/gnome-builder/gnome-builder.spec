%def_disable snapshot

%define xdg_name org.gnome.Builder
%define ver_major 3.22
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_enable sysprof_plugin
%def_enable gtk_doc

Name: gnome-builder
Version: %ver_major.2
Release: alt1

Summary: Builder - Develop software for GNOME
License: LGPLv2+
Group: Development/GNOME and GTK+
Url: https://wiki.gnome.org/Apps/Builder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%set_typelibdir %_libdir/%name/girepository-1.0

%define gtk_ver 3.20.0
%define gtksourceview_ver 3.20.0
%define git2_ver 0.24.0
%define devhelp_ver 3.20.0
%define gjs_ver 1.42
%define xml_ver 2.9.0
%define vala_ver 0.30
%define sysprof_ver 3.22.2

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/plugins

%add_findreq_skiplist %_datadir/%name/plugins/autotools_templates/resources/*/*.py

PreReq: %name-data = %version-%release
Requires: automake autoconf libtool
Requires: devhelp uncrustify ctags
Requires: libpeas-python3-loader
Requires: git

BuildRequires: /proc gcc-c++ flex mm-common yelp-tools gtk-doc
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: clang-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview3-devel >= %gtksourceview_ver
BuildRequires: libgit2-glib-devel >= %git2_ver libdevhelp-devel >= %devhelp_ver
BuildRequires: libpcre-devel libgjs-devel >= %gjs_ver libwebkit2gtk-devel
BuildRequires: libxml2-devel >= %xml_ver libpeas-devel libvte3-devel
BuildRequires: libjson-glib-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgtksourceview3-gir-devel libgit2-glib-gir-devel libpeas-gir-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: libvala-devel >= %vala_ver vala-tools
%{?_enable_sysprof_plugin:BuildRequires: sysprof-devel >= %sysprof_ver}

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
#NOCONFIGURE=1 ./autogen.sh
%configure --disable-static \
	%{?_disable_sysprof_plugin:--disable-sysprof-plugin} \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%_libexecdir/%name-worker
%dir %_libexecdir/%name
%_libexecdir/%name/ide-list-counters
%dir %_libdir/%name
%_libdir/%name/libide-%api_ver.so
%_libdir/%name/libtemplate-glib-%api_ver.so.*
%_libdir/%name/libegg-private.so.*
%_libdir/%name/librg.so.*
%_libdir/%name/libpanel-gtk.so.*
%_libdir/%name/libsearch.so.*
%_libdir/%name/libgstyle-private.so.*

%exclude %_libdir/%name/*.la
%exclude %_libdir/%name/libegg-private.so
%exclude %_libdir/%name/libpanel-gtk.so
%exclude %_libdir/%name/librg.so
%exclude %_libdir/%name/libsearch.so
%exclude %_libdir/%name/libgstyle-private.so

%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Egg-%api_ver.typelib
%_libdir/%name/girepository-1.0/Gstyle-%api_ver.typelib
%_libdir/%name/girepository-1.0/Ide-%api_ver.typelib
%_libdir/%name/girepository-1.0/Jsonrpc-1.0.typelib
%_libdir/%name/girepository-1.0/Pnl-%api_ver.typelib
%_libdir/%name/girepository-1.0/Template-%api_ver.typelib

%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*.plugin
%_libdir/%name/plugins/__pycache__/
%_libdir/%name/plugins/autotools_templates/
%_libdir/%name/plugins/contributing_plugin/
%_libdir/%name/plugins/fpaste_plugin/
%_libdir/%name/plugins/html_preview_plugin/
%_libdir/%name/plugins/jedi_plugin.py
%_libdir/%name/plugins/jhbuild_plugin.py
%_libdir/%name/plugins/libautotools-plugin.so
%_libdir/%name/plugins/libbuild-tools-plugin.so
%_libdir/%name/plugins/libc-pack-plugin.so
%_libdir/%name/plugins/libclang-plugin.so
%_libdir/%name/plugins/libcolor-picker-plugin.so
%_libdir/%name/plugins/libcommand-bar.so
%_libdir/%name/plugins/libcomment-code-plugin.so
%_libdir/%name/plugins/libcreate-project-plugin.so
%_libdir/%name/plugins/libctags-plugin.so
%_libdir/%name/plugins/libdevhelp-plugin.so
%_libdir/%name/plugins/libfile-search.so
%_libdir/%name/plugins/libgcc-plugin.so
%_libdir/%name/plugins/libgettext-plugin.so
%_libdir/%name/plugins/libgit-plugin.so
%_libdir/%name/plugins/libgnome-code-assistance-plugin.so
%_libdir/%name/plugins/libhtml-completion-plugin.so
%_libdir/%name/plugins/libmingw-plugin.so
%_libdir/%name/plugins/libproject-tree-plugin.so
%_libdir/%name/plugins/libpython-pack-plugin.so
%_libdir/%name/plugins/libquick-highlight-plugin.so
%_libdir/%name/plugins/libsupport-plugin.so
%_libdir/%name/plugins/libsymbol-tree.so
%_libdir/%name/plugins/libsysmon.so
%{?_enable_sysprof_plugin:%_libdir/%name/plugins/libsysprof-plugin.so}
%_libdir/%name/plugins/libterminal.so*
%_libdir/%name/plugins/libvala-pack-plugin.so
%_libdir/%name/plugins/libxml-pack-plugin.so
%_libdir/%name/plugins/python_gi_imports_completion.py
%_libdir/%name/plugins/meson_plugin/
%_libdir/%name/plugins/todo_plugin/
%_libdir/%name/plugins/cargo_plugin.py*
%_libdir/%name/plugins/rust_langserv_plugin.py*

%exclude %_libdir/%name/plugins/*.la

%_includedir/%name-%version/
%_libdir/%name/libtemplate-glib-%api_ver.so
%dir %_libdir/%name/pkgconfig
%_libdir/%name/pkgconfig/libide-%api_ver.pc
%_libdir/%name/pkgconfig/template-glib-%api_ver.pc
%python3_sitelibdir/gi/overrides/Ide.py
%python3_sitelibdir/gi/overrides/__pycache__/
%doc README AUTHORS NEWS

%files data
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%_datadir/gtksourceview-3.0/styles/*.xml
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/appdata/%xdg_name.appdata.xml
#%files -n libide-devel-doc
%{?_enable_gtk_doc:%_datadir/gtk-doc/html/libide/}


%changelog
* Wed Nov 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.20.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

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

