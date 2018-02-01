%def_disable snapshot

%define xdg_name org.gnome.Builder
%define ver_major 3.26
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_with sysprof
%def_with flatpak
%def_with docs
%def_without autotools
%def_without autotools_templates

Name: gnome-builder
Version: %ver_major.4
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

%define glib_ver 2.53.2
%define gtk_ver 3.22.1
%define gtksourceview_ver 3.20.0
%define git2_ver 0.25.0
%define devhelp_ver 3.20.0
%define gjs_ver 1.42
%define xml_ver 2.9.0
%define vala_ver 0.37
%define sysprof_ver 3.22.3
%define vte_ver 0.46
%define gtkmm_ver 3.20
%define gspell_ver 1.2.0
%define peas_ver 1.21.0
%define json_glib_ver 1.2.0
%define dazzle_ver 3.26.3

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/plugins

%add_findreq_skiplist %_datadir/%name/plugins/*_templates/resources/*/*.py

PreReq: %name-data = %version-%release
Requires: meson
%{?_with_autotools:Requires: automake autoconf libtool}
Requires: devhelp uncrustify ctags
Requires: libpeas-python3-loader
Requires: git
Requires: indent xmllint

BuildRequires: /proc meson gcc-c++ flex mm-common yelp-tools gtk-doc
BuildRequires: ctags
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: clang4.0-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview3-devel >= %gtksourceview_ver
BuildRequires: libgit2-glib-devel >= %git2_ver libdevhelp-devel >= %devhelp_ver
BuildRequires: libpcre-devel libgjs-devel >= %gjs_ver libwebkit2gtk-devel
BuildRequires: libxml2-devel >= %xml_ver libpeas-devel >= %peas_ver libvte3-devel >= %vte_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgtksourceview3-gir-devel libgit2-glib-gir-devel libpeas-gir-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: libgspell-devel >= %gspell_ver libenchant-devel
BuildRequires: libdazzle-devel >= %dazzle_ver libtemplate-glib-devel libjsonrpc-glib-devel
BuildRequires: libdazzle-gir-devel libtemplate-glib-gir-devel  libjsonrpc-glib-gir-devel
BuildRequires: python-module-sphinx python-module-sphinx_rtd_theme
%{?_with_flatpak:BuildRequires: libflatpak-devel libostree-devel}
%{?_with_sysprof:BuildRequires: sysprof-devel >= %sysprof_ver}
%{?_with_idemm:BuildRequires: libgtkmm3-devel >= %gtkmm_ver}

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
%meson -Denable-static=false \
	%{?_with_sysprof:-Dwith-sysprof=true} \
	%{?_with_docs:-Dwith-docs=true} \
	%{?_without_flatpak:-Dwith-flatpak=false} \
	%{?_with_autotools:-Dwith-autotools=true} \
	%{?_with_autotools_templates:-Dwith-autotools_templates=true}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%_libexecdir/%name-worker
%dir %_libdir/%name
%_libdir/%name/libide-%api_ver.so
%{?_enable_idemm:%_libdir/%name/libidemm-%api_ver.so.*}
%_libdir/%name/libgstyle-private.so.*
%_libdir/%name/libgd.so

%exclude %_libdir/%name/libgstyle-private.so

%{?_enable_idemm:%exclude %_libdir/%name/libidemm-%api_ver.so}

%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Gstyle-%api_ver.typelib
%_libdir/%name/girepository-1.0/Ide-%api_ver.typelib

%dir %_libdir/%name/plugins
%_libdir/%name/plugins/cargo_plugin.py*
%_libdir/%name/plugins/cmake_plugin/
%_libdir/%name/plugins/eslint_plugin/
%_libdir/%name/plugins/find_other_file.py
#%_libdir/%name/plugins/fpaste_plugin/
%_libdir/%name/plugins/html_preview_plugin/
%_libdir/%name/plugins/jedi_plugin.py
%_libdir/%name/plugins/jhbuild_plugin.py
%_libdir/%name/plugins/libautotools-plugin.so
%_libdir/%name/plugins/libbeautifier_plugin.so
%_libdir/%name/plugins/libclang-plugin.so
%_libdir/%name/plugins/libcode-index-plugin.so
%_libdir/%name/plugins/libcolor-picker-plugin.so
%_libdir/%name/plugins/libcommand-bar.so
%_libdir/%name/plugins/libcomment-code-plugin.so
%_libdir/%name/plugins/libc-pack-plugin.so
%_libdir/%name/plugins/libcreate-project-plugin.so
%_libdir/%name/plugins/libctags-plugin.so
%_libdir/%name/plugins/libdevhelp-plugin.so
%_libdir/%name/plugins/libdocumentation-card-plugin.so
%_libdir/%name/plugins/libfile-search.so
%_libdir/%name/plugins/libflatpak-plugin.so
%_libdir/%name/plugins/libgcc-plugin.so
%_libdir/%name/plugins/libgdb-plugin.so
%_libdir/%name/plugins/libgettext-plugin.so
%_libdir/%name/plugins/libgit-plugin.so
%_libdir/%name/plugins/libgnome-code-assistance-plugin.so
%_libdir/%name/plugins/libhistory-plugin.so
%_libdir/%name/plugins/libhtml-completion-plugin.so
%_libdir/%name/plugins/libmingw-plugin.so
%_libdir/%name/plugins/libnotification-plugin.so
%_libdir/%name/plugins/libproject-tree-plugin.so
%_libdir/%name/plugins/libpython-pack-plugin.so
%_libdir/%name/plugins/libquick-highlight-plugin.so
%_libdir/%name/plugins/libretab-plugin.so
%_libdir/%name/plugins/libspellcheck-plugin.so
%_libdir/%name/plugins/libsupport-plugin.so
%_libdir/%name/plugins/libsymbol-tree-plugin.so
%_libdir/%name/plugins/libsysmon.so
%_libdir/%name/plugins/libterminal.so*
%_libdir/%name/plugins/libtodo-plugin.so
%_libdir/%name/plugins/libvala-pack-plugin.so
%_libdir/%name/plugins/libxml-pack-plugin.so
%_libdir/%name/plugins/make_plugin/
%_libdir/%name/plugins/meson_plugin/
%_libdir/%name/plugins/meson_templates/
%_libdir/%name/plugins/mono_plugin*
%_libdir/%name/plugins/npm_plugin.py
%_libdir/%name/plugins/phpize_plugin.py
%_libdir/%name/plugins/*.plugin
%_libdir/%name/plugins/__pycache__/
%_libdir/%name/plugins/python_gi_imports_completion.py
%_libdir/%name/plugins/rust_langserv_plugin.py*
%_libdir/%name/plugins/rustup_plugin/
%_libdir/%name/plugins/valgrind*
%{?_with_autotools_templates:%_libdir/%name/plugins/autotools_templates/}
%{?_with_sysprof:%_libdir/%name/plugins/libsysprof-plugin.so}

%_includedir/%name/
%dir %_libdir/%name/pkgconfig
%_libdir/%name/pkgconfig/libide-%api_ver.pc
%python3_sitelibdir/gi/overrides/Ide.py
%python3_sitelibdir/gi/overrides/__pycache__/
%doc README AUTHORS NEWS

%files data
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml
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
#%{?_with_docs:%_datadir/gtk-doc/html/libide/}
%doc %_defaultdocdir/%name/


%changelog
* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Wed Nov 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- rebuilt against libclang.so.4

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 14 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.22.4-alt1.1
- Rebuilt with llvm 4.0.

* Thu Dec 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

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

