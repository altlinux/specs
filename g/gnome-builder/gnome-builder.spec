%def_disable snapshot
%define optflags_lto %nil

%define xdg_name org.gnome.Builder
%define ver_major 42
%define beta %nil
%define _libexecdir %_prefix/libexec
%define api_ver %ver_major.0

%def_with clang
%def_with sysprof
%def_with flatpak
%def_with docs
%def_with help
%def_with autotools
# disabled by default
%def_with vala
# Rust Language Server integration plugin (disabled by default)
%def_without rls
# SDK for Language Server Protocol (LSP)
# https://gitlab.gnome.org/esodan/gvls.git
%def_without gvls

Name: gnome-builder
Version: %ver_major.1
Release: alt1%beta

Summary: Builder - Develop software for GNOME
License: LGPLv2+
Group: Development/GNOME and GTK+
Url: https://wiki.gnome.org/Apps/Builder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif
#https://l10n.gnome.org/media/upload/gnome-builder-master-po-ru-955618_BWaCuRU.po
Source1: %name-ru.po

%set_typelibdir %_libdir/%name/girepository-1.0

%define glib_ver 2.69.1
%define gtk_ver 3.24
%define gtksourceview_api_ver 4
%define gtksourceview_ver 4.6.1
%define git2_ver 0.28.0.1
%define devhelp_ver 3.30.0
%define gjs_ver 1.42
%define xml_ver 2.9.0
%define vala_ver 0.37
%define sysprof_ver 3.34.0
%define vte_ver 0.46
%define gtkmm_ver 3.20
%define gspell_ver 1.8.0
%define peas_ver 1.22.0
%define json_glib_ver 1.2.0
%define dazzle_ver 3.37.0
%define template_glib_ver 3.34.0
%define soup_ver 2.52
%define webkit_ver 2.26
%define portal_ver 0.5
%define gi_docgen_ver 2021.9
%define jsonrpc_ver 3.41.0
%define handy_ver 1.0

%add_python3_path %_libdir/%name/plugins
%add_findreq_skiplist %_datadir/%name/plugins/*_templates/resources/*/*.py

Requires(pre): %name-data = %EVR
# src/libide/gui/ide-application-plugins.c
Requires: typelib(WebKit2) = 4.0
Requires: typelib(Jsonrpc) = 1.0

%{?_with_autotools:Requires: automake autoconf libtool}
#%{?_with_flatpak:Requires: flatpak-builder}
Requires: meson %_bindir/git %_bindir/indent %_bindir/xmllint
Requires: devhelp %_bindir/uncrustify %_bindir/ctags %_bindir/cmark
Requires: libpeas-python3-loader

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: /proc meson gcc-c++ flex mm-common yelp-tools
BuildRequires: %_bindir/ctags %_bindir/tidy %_bindir/uncrustify
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview%gtksourceview_api_ver-devel >= %gtksourceview_ver
BuildRequires: libgit2-glib-devel >= %git2_ver libdevhelp-devel >= %devhelp_ver
BuildRequires: libpcre-devel libgjs-devel >= %gjs_ver libwebkit2gtk-devel >= %webkit_ver
BuildRequires: libxml2-devel >= %xml_ver libpeas-devel >= %peas_ver libvte3-devel >= %vte_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver libpcre2-devel
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libvte3-gir-devel
BuildRequires: libgtksourceview%gtksourceview_api_ver-gir-devel libgit2-glib-gir-devel libpeas-gir-devel
BuildRequires: libjson-glib-gir-devel libsoup-devel >= %soup_ver
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: libgspell-devel >= %gspell_ver libenchant2-devel
BuildRequires: libdazzle-devel >= %dazzle_ver libtemplate-glib-devel >= %template_glib_ver
BuildRequires: libjsonrpc-glib-devel >= %jsonrpc_ver
BuildRequires: libdazzle-gir-devel libtemplate-glib-gir-devel  libjsonrpc-glib-gir-devel
BuildRequires: libgtkmm3-devel >= %gtkmm_ver
BuildRequires: libgladeui2.0-devel cmark-devel
BuildRequires: libportal-gtk3-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
%{?_with_clang:BuildRequires: llvm-devel clang-devel}
%{?_with_docs:BuildRequires: gi-docgen >= %gi_docgen_ver}
%{?_with_help:BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme}
%{?_with_flatpak:BuildRequires: libflatpak-devel libostree-devel libportal-devel >= %portal_ver}
%{?_with_sysprof:BuildRequires: sysprof-devel >= %sysprof_ver}

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

%package clang
Summary: Clang/LLVW dependent part for GNOME Builder
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description clang
This package provides files for Gnome Builder to work with Clang/LLVW.

%prep
%setup -n %name-%version%beta
sed -i 's|\(#\!/usr/bin/env python\)$|\13|' src/plugins/*/*.py
#cp %SOURCE1 po/ru.po

%build
%meson \
	%{?_without_clang:-Dplugin_clang=false} \
	%{?_without_sysprof:-Dplugin_sysprof=false} \
	%{?_with_docs:-Ddocs=true} \
	%{?_with_help:-Dhelp=true} \
	%{?_without_flatpak:-Dplugin_flatpak=false} \
	%{?_with_autotools:-Dplugin_autotools=true} \
	%{?_with_rls:-Dplugin_rls=true} \
	%{?_with_gvls:-Dplugin_gvls=true}
%nil
%meson_build -v

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-git
%_libexecdir/%name-flatpak
%dir %_libdir/%name

%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Ide-%api_ver.typelib

%dir %_libdir/%name/plugins
%_libdir/%name/plugins/__pycache__
%_libdir/%name/plugins/blueprint.plugin
%_libdir/%name/plugins/blueprint_plugin.py
%_libdir/%name/plugins/buildstream.plugin
%_libdir/%name/plugins/buildstream_plugin.py
%_libdir/%name/plugins/cargo.plugin
%_libdir/%name/plugins/cargo_plugin.py
%_libdir/%name/plugins/copyright.plugin
%_libdir/%name/plugins/copyright_plugin.py
%_libdir/%name/plugins/eslint.plugin
%_libdir/%name/plugins/eslint_plugin.py
%_libdir/%name/plugins/find-other-file.plugin
%_libdir/%name/plugins/find_other_file.py
%_libdir/%name/plugins/gjs_symbols.plugin
%_libdir/%name/plugins/gjs_symbols.py
%_libdir/%name/plugins/go-langserv.plugin
%_libdir/%name/plugins/go_langserver_plugin.py
%_libdir/%name/plugins/gradle.plugin
%_libdir/%name/plugins/gradle_plugin.py
%{?_with_gvls:%_libdir/%name/plugins/gvls_plugin.py
%_libdir/%name/plugins/gvls.plugin}
%_libdir/%name/plugins/html-preview.plugin
%_libdir/%name/plugins/html_preview.gresource
%_libdir/%name/plugins/html_preview.py
%_libdir/%name/plugins/intelephense.plugin
%_libdir/%name/plugins/intelephense.py
%_libdir/%name/plugins/jedi-language-server.plugin
%_libdir/%name/plugins/jedi_language_server_plugin.py
%_libdir/%name/plugins/jhbuild.plugin
%_libdir/%name/plugins/jhbuild_plugin.py
%_libdir/%name/plugins/make.plugin
%_libdir/%name/plugins/make_plugin.gresource
%_libdir/%name/plugins/make_plugin.py
%_libdir/%name/plugins/maven.plugin
%_libdir/%name/plugins/maven_plugin.py
%_libdir/%name/plugins/meson-templates.plugin
%_libdir/%name/plugins/meson_templates.gresource
%_libdir/%name/plugins/meson_templates.py
%_libdir/%name/plugins/mono.plugin
%_libdir/%name/plugins/mono_plugin.py
%_libdir/%name/plugins/npm.plugin
%_libdir/%name/plugins/npm_plugin.py
%_libdir/%name/plugins/phpize.plugin
%_libdir/%name/plugins/phpize_plugin.py
%_libdir/%name/plugins/python-gi-imports-completion.plugin
%_libdir/%name/plugins/python_gi_imports_completion.py
%{?_with_rls:%_libdir/%name/plugins/rls.plugin
%_libdir/%name/plugins/rls_plugin.py}
%_libdir/%name/plugins/rstcheck.plugin
%_libdir/%name/plugins/rstcheck_plugin.py
%_libdir/%name/plugins/rubocop.plugin
%_libdir/%name/plugins/rubocop_plugin.py
%_libdir/%name/plugins/stylelint.plugin
%_libdir/%name/plugins/stylelint_plugin.py
%_libdir/%name/plugins/ts-language-server.plugin
%_libdir/%name/plugins/ts_language_server_plugin.py
%{?_with_vala:%_libdir/%name/plugins/vala-pack.plugin
%_libdir/%name/plugins/vala_pack_plugin.py}
%_libdir/%name/plugins/valgrind.plugin
%_libdir/%name/plugins/valgrind_plugin.gresource
%_libdir/%name/plugins/valgrind_plugin.py
%_libdir/%name/plugins/vala_langserv.plugin
%_libdir/%name/plugins/vala_langserv.py
%_libdir/%name/plugins/waf.plugin
%_libdir/%name/plugins/waf_plugin.py
#%{?_with_autotools_templates:%_libdir/%name/plugins/autotools_templates/}
#%{?_with_sysprof:%_libdir/%name/plugins/sysprof-plugin.so}

%_includedir/%name/
%_includedir/%name-%ver_major/
%_pkgconfigdir/%name-%version.pc
%python3_sitelibdir_noarch/gi/overrides/Ide.py
%python3_sitelibdir_noarch/gi/overrides/__pycache__/
%doc README* AUTHORS NEWS

%if_with clang
%files clang
%_libexecdir/%name-clang
%endif

%files data
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.clang.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.copyright.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.stylelint.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.rust-analyzer.gschema.xml
%_datadir/gtksourceview-%gtksourceview_api_ver/styles/*.xml
%_datadir/gtksourceview-%gtksourceview_api_ver/language-specs/blueprint.lang

%_datadir/%name/
%_iconsdir/hicolor/*/*/*.*
%_datadir/metainfo/%xdg_name.appdata.xml

%{?_with_docs:%_datadir/doc/libide/}
%{?_with_help:%_datadir/doc/%name/}

%changelog
* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Tue Apr 12 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1.1
- rebuilt against libclang.so.13

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc1
- 42.rc1

* Thu Jan 27 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt2
- updated to 41.3-14-gc3a428982
- fixed russian translation (ALT #41815)

* Tue Dec 07 2021 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Wed Nov 17 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Thu Sep 23 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Mon Sep 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.2-alt1.2
- disabled LTO

* Thu Jul 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.2-alt1.1
- required "typelib(Jsonrpc) = 1.0" (ALT #40399)

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.2-alt1
- updated to 3.40.2-5-gb7eb24645

* Thu Apr 29 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1
- moved gnome-builder-clang to separate package
  to optimize dependencies (ALT #39925)

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Tue Feb 02 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Oct 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Jun 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Dec 03 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt2
- updated to 3.34.1-6-gf64dc9d30
- backported fixes to build with meson-0.52

* Sat Oct 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Jul 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.4-alt1
- 3.32.4

* Wed Jun 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Jan 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri Jul 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Apr 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.28.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1.1
- rebuilt against libclang.so.6

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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

