%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.shortcut-overlay

Name: elementary-shortcut-overlay
Version: 8.1.0
Release: alt1

Summary: A native, OS-wide shortcut overlay
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/shortcut-overlay

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(pantheon-wayland-1)

%description
Native OS-wide shortcut overlay to be launched by Gala

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- Initial build for Sisyphus
