%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.greeter

Name: elementary-greeter
Version: 8.1.2
Release: alt1.git.e307af1

Summary: Login and Lock Screen greeter for elementary OS and Pantheon, using LightDM
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/greeter


Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(liblightdm-gobject-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(gdk-wayland-3.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: libmutter-devel
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

%files -f %appname.lang
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/lightdm/%{appname}.conf
%_bindir/%{appname}-compositor
%_sbindir/%appname
%_sbindir/%{appname}-session-manager
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}*.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}*.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/lightdm/lightdm.conf.d/40-%{appname}.conf
%_datadir/xgreeters/%{appname}.desktop
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/%{appname}.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/%{appname}.mo

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.2-alt1.git.e307af1
- Initial build for Sisyphus
