%define _unpackaged_files_terminate_build 1

Name: sticky-linuxmint
Version: 1.31
Release: alt1

Summary: A sticky notes app for the linux desktop
License: GPL-2.0
Group: Graphical desktop/Other
URL: https://github.com/linuxmint/sticky

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires: meson

Requires: typelib(Gspell)
Requires: xapp-symbolic-icons

BuildArch: noarch

Source: %name-%version.tar

%description
Sticky is a note-taking app for the Linux desktop that simulates
traditional "sticky note" style stationery on your desktop. Some of its
features include basic text formatting (bold, italics, monospaced,
etc.), spell-checking, a tray icon for controlling note visibility,
color notes, manual and automatic backups, and a manager to organize
your notes into groups. Sticky is written in Python, and uses the
GTK3 toolkit.

%prep
%setup -n %name-%version
sed -i "s/__DEB_VERSION__/%{version}/" usr/lib/sticky/sticky.py
sed -i 's|common-licenses/GPL|license/GPL-2.0|' usr/lib/sticky/sticky.py
sed -i 's|^Categories=.*|Categories=Utility;TextTools;|' data/sticky.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %{name}.lang
%doc COPYING README.md
%_bindir/sticky
%dir %_libexecdir/sticky
%_libexecdir/sticky/*
%_desktopdir/*.desktop
%_sysconfdir/xdg/autostart/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.gschema.xml
%dir %_datadir/sticky
%_datadir/sticky/*

%changelog
* Tue May 19 2026 Nikolay Strelkov <snk@altlinux.org> 1.31-alt1
- New version 1.31.

* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 1.30-alt1
- New version 1.30.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.29-alt1
- New version 1.29.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.28-alt1
- New version 1.28.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.27-alt1
- New version 1.27.

* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.26-alt1
- New version 1.26.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.25-alt1
- New version 1.25.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.24-alt2
- Applied repocop fix for freedesktop-categories

* Tue Mar 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.24-alt1
- Initial build for Sisyphus
