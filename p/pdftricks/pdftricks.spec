%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.muriloventuroso.pdftricks

Name: pdftricks
Version: 0.4.1
Release: alt1

Summary: A simple, efficient application for small manipulations in PDF files using Ghostscript.
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/muriloventuroso/pdftricks

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

Requires: /usr/bin/gs

%description
%summary

Features:

* Compress PDF (multiple resolutions)
* Split PDF (All pages or page ranges)
* Merge PDF
* Convert PDF

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=GTK;Publishing;Office;|' data/com.github.muriloventuroso.pdftricks.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
