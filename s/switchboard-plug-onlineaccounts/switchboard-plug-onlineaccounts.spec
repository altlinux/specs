%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.onlineaccounts

Name: switchboard-plug-onlineaccounts
Version: 8.0.2
Release: alt1

Summary: Switchboard Online Accounts Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-onlineaccounts

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(camel-1.2)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: vapi(libedataserver-1.2)

%description
Online Accounts plug for Switchboard.
This plug allow you to enable online accounts sync.

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
%_libdir/switchboard-3/network/libonlineaccounts.so
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus
