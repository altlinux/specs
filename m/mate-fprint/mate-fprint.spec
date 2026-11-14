%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-fprint
Version: 1.0.0
Release: alt1

Summary: Fingerprint enrollment UI for MATE
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-fprint

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: /usr/bin/appstreamcli

Requires: fprintd

%description
A traditional Vala and GTK 3 fingerprint utility for the MATE desktop.
It talks directly to fprintd over D-Bus.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/mate-fprint
%_desktopdir/org.mate.fprint.desktop
%dir %_datadir/mate-fprint
%_datadir/mate-fprint/mate-fprint.css
%_datadir/metainfo/org.mate.fprint.metainfo.xml
%_datadir/pam-configs/mate-fprint

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
