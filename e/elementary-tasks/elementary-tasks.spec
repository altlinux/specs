%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.tasks

Name: elementary-tasks
Version: 6.3.3
Release: alt1

Summary: Synced tasks and reminders on elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/tasks

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libecal-2.0)
BuildRequires: pkgconfig(champlain-0.12)
BuildRequires: pkgconfig(champlain-gtk-0.12)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: vapi(libedataserver-1.2)
BuildRequires: vapi(granite)

%description
%summary

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
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 6.3.3-alt1
- Initial build for Sisyphus
