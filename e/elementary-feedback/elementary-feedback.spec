%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.feedback

%def_with check

Name: elementary-feedback
Version: 8.1.1
Release: alt1

Summary: GitHub Issue Reporter for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/feedback

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: libappstream-devel
BuildRequires: libappstream-gir
BuildRequires: libappstream-compose-gir
BuildRequires: libappstream-glib-gir
BuildRequires: libappstream-glib-gir-devel

%description
Feedback assists users in reporting issues against the correct GitHub repository.

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

%files -f %appname.lang
%doc LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/%{appname}.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/%{appname}.mo

%changelog
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.1-alt1
- Initial build for Sisyphus
