%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name webfont-kit-generator
%define binary_name webfontkitgenerator
%define ver_major 1.1
%define rdn_name com.rafaelmardojai.WebfontKitGenerator

%def_enable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Webfont Kit Generator
License: GPL-3.0-or-later
Group: Development/Other
Url: https://apps.gnome.org/WebfontKitGenerator

%if_disabled snapshot
Source: https://github.com/rafaelmardojai/webfont-kit-generator/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/rafaelmardojai/webfont-kit-generator.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%binary_name

%define bp_ver 0.10
%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: typelib(GtkSource) = 5
Requires: typelib(Soup) = 3.0
#Requires: python3(fontTools) python3(brotli)
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: typelib(Adw) typelib(Soup) = 3.0
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Webfont Kit Generator is a simple utility that allows you to generate
woff, woff2 and the necessary CSS boilerplate from non-web font formats
(otf and ttf).

Webfont Kit Generator also includes a tool to Download fonts from Google
Fonts for self-hosting.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%_name.lang %binary_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_datadir/%binary_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*


%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Dec 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1.1
- explicitly required python3(fontTools), python3(brotli)

* Wed Dec 27 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus


