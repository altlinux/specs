%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: desktop-icon-cache-updater
Version: 0.1.0
Release: alt1

Summary: Desktop icon cache updater 
License: GPL-3.0-or-later
Group: Other
URL: http://git.altlinux.org/people/rirusha/packages/desktop-icon-cache-updater
VCS: http://git.altlinux.org/people/rirusha/packages/desktop-icon-cache-updater.git

Source: %name-%version.tar

Requires: /usr/bin/gtk4-update-icon-cache

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(librsvg-2.0)

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libexecdir/%name
%_rpmlibdir/%name.filetrigger
%_iconsdir/hicolor/cache

%changelog
* Wed Jul 15 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.0-alt1
- Initial build.
