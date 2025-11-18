%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.mouse-touchpad

Name: switchboard-plug-mouse-touchpad
Version: 8.0.3
Release: alt1

Summary: Switchboard Mouse & Touchpad Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-mouse-touchpad

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(libxml-2.0)

%description
Mouse/Touchpad plug for Switchboard.
This plug configures mouse and touchpad.

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
%_libdir/switchboard-3/hardware/libmouse-touchpad.so
%_datadir/metainfo/io.elementary.settings.mouse-touchpad.metainfo.xml

%changelog
* Tue Nov 18 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.3-alt1
- New version 8.0.3.

* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus
