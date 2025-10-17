%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.desktop.agent-polkit

%define _libexecdir %_prefix/libexec

Name: pantheon-agent-polkit
Version: 8.0.1
Release: alt1

Summary: Pantheon Polkit Agent
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/pantheon-agent-polkit

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(pantheon-wayland-1)

%description
%summary

%prep
%setup

%build
%meson --libexecdir=%_libexecdir
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc COPYING README.md
%_sysconfdir/xdg/autostart/%{appname}.desktop
%dir %_libexecdir/policykit-1-pantheon
%_libexecdir/policykit-1-pantheon/%{appname}
%_desktopdir/%{appname}.desktop
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
