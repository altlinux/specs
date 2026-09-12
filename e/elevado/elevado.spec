%define _unpackaged_files_terminate_build 1
%define full_name com.feaneron.Elevado

Name: elevado
Version: 2025.1
Release: alt1

Summary: Accessibility inspector

License: GPL-3.0-or-later
Group: Accessibility
Url: https://gitlab.gnome.org/feaneron/elevado
VCS: https://gitlab.gnome.org/feaneron/elevado.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires(pre): rpm-macros-rust
BuildRequires: libadwaita-devel
BuildRequires: libgtk4-devel
BuildRequires: meson
BuildRequires: rpm-build-ninja
BuildRequires(pre): rpm-build-rust
BuildRequires: rpm-build-cmake

%description
Elevado allows browsing through the accessibility objects that apps set for
themselves. The primary goal is to make it easier to spot where apps fall apart
in terms of accessibility.

%prep
%setup -a0 -a1
%rust_prep

%build
%meson
%meson_build 

%install
%meson_install

%check
%meson_test

%files
%_bindir/%name
%_datadir/applications/%full_name.desktop
%dir %_datadir/%name
%_datadir/%name/%name.gresource
%_datadir/icons/hicolor/scalable/apps/%full_name.svg
%_datadir/icons/hicolor/symbolic/apps/%full_name-symbolic.svg
%_datadir/metainfo/%full_name.metainfo.xml

%changelog
* Thu Sep 10 2026 Artem Semenov <savoptik@altlinux.org> 2025.1-alt1
- Initial build for sisyphus.
