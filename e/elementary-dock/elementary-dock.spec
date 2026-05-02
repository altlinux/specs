%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.dock

Name: elementary-dock
Version: 8.3.3
Release: alt1

Summary: A quick app launcher and window switcher for Pantheon and elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/dock

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)

%description
%summary

%prep
%setup

%build
CFLAGS="%{optflags} -Wno-error=int-conversion"
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc LICENSE README.md
%_bindir/%appname
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/io.elementary.dock.mo
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/io.elementary.dock.mo

%changelog
* Sat May 02 2026 Nikolay Strelkov <snk@altlinux.org> 8.3.3-alt1
- New version 8.3.3.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 8.3.2-alt1
- New version 8.3.2.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 8.3.1-alt1
- New version 8.3.1.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 8.3.0-alt1
- New version 8.3.0.

* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus
