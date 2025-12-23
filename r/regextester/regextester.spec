%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.artemanufrij.regextester

Name: regextester
Version: 1.1.1
Release: alt1

Summary: simple regex tester
License: GPL-3.0-or-later
Group: Text tools
Url: https://github.com/artemanufrij/regextester

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

Requires: elementary-icon-theme

%description
A simple app for testing regular expressions, written
especially for elementary OS.

%prep
%setup
sed -i "s|Categories=.*|Categories=Development;GNOME;GTK;WebDevelopment;Debugger;|" data/com.github.artemanufrij.regextester.desktop.in
sed -i "s|data/icons/64/|%_iconsdir/hicolor/64x64/apps/|" README.md

%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc debian/copyright README.md screenshots
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.appdata.xml
%dir %_datadir/%appname
%dir %_datadir/%appname/icons
%_datadir/%appname/icons/regex-match-first.svg
%_datadir/%appname/icons/regex-match-second.svg

%changelog
* Mon Dec 22 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
