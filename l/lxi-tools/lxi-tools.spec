%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lxi-tools
Version: 2.8
Release: alt1

Summary: LAN eXtensions for Instrumentation (LXI) software interface
License: BSD-3-Clause
Group: Engineering
Url: https://github.com/lxi-tools/lxi-tools

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(liblxi)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(bash-completion)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)

%description
lxi-tools is collection of open source software tools that enables
control of LXI-compatible instruments such as modern oscilloscopes,
power supplies, spectrum analyzers etc.

%prep
%setup
sed -i "s|Categories=.*|Categories=Development;Electronics;|" data/io.github.lxi-tools.lxi-gui.desktop

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS LICENSE NEWS README.md TODO
%doc examples images
%_bindir/lxi
%_bindir/lxi-gui
%_desktopdir/io.github.lxi-tools.lxi-gui.desktop
%_datadir/bash-completion/completions/lxi
%_datadir/glib-2.0/schemas/io.github.lxi-tools.lxi-gui.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.lxi-tools.lxi-gui.svg
%_iconsdir/hicolor/symbolic/apps/io.github.lxi-tools.lxi-gui-symbolic.svg
%_man1dir/lxi.1.*
%_datadir/metainfo/io.github.lxi-tools.lxi-gui.appdata.xml

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 2.8-alt1
- Initial build for Sisyphus
