%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.desktop

Name: switchboard-plug-pantheon-shell
Version: 8.3.0
Release: alt1

Summary: Switchboard Desktop Plug
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/elementary/settings-desktop

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(gexiv2)

%description
Change desktop settings.
Settings plugin for controlling Pantheon Shell.

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
%doc COPYING README.md
%_libdir/switchboard-3/personal/libdesktop.so
%_datadir/metainfo/io.elementary.settings.desktop.metainfo.xml

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 8.3.0-alt1
- New version 8.3.0.

* Tue Nov 18 2025 Nikolay Strelkov <snk@altlinux.org> 8.2.1-alt1
- New version 8.2.1.

* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus
