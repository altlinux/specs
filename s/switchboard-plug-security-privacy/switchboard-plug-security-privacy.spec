%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.security-privacy

Name: switchboard-plug-security-privacy
Version: 8.0.1
Release: alt1

Summary: Switchboard Security & Privacy Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-security-privacy

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(zeitgeist-2.0)

%description
Manage security and privacy.
Settings plugin for managing the security and privacy of your system.

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
%_libdir/switchboard-3/personal/libsecurity-privacy.so
%_libdir/switchboard-3/personal/security-privacy-plug-helper
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
