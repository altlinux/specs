%define _unpackaged_files_terminate_build 1

%def_with check

Name: xepub
Version: 1.0.1
Release: alt1

Summary: EPUB reader for the Linux desktop
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/xepub

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/gtk4-update-icon-cache

%filter_from_requires /python3(window)/d

%description
EPUB reader for the Linux desktop.

Xepub is a secure, comfortable, paginated EPUB reader.

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
%doc README.md SECURITY.md
%_bindir/xepub
%_desktopdir/xepub.desktop
%_datadir/glib-2.0/schemas/org.x.xepub.gschema.xml
%_iconsdir/hicolor/scalable/apps/xepub.svg
%dir %_datadir/xepub
%_datadir/xepub/epub.py
%_datadir/xepub/main.py
%_datadir/xepub/paginator.py
%_datadir/xepub/preferences.py
%_datadir/xepub/state.py
%_datadir/xepub/window.py
%_datadir/xepub/window.ui

%changelog
* Sat Sep 12 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
