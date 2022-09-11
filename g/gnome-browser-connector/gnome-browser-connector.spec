%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 42
%define xdg_name org.gnome.BrowserConnector
%define pypi_name gnome_browser_connector

Name: gnome-browser-connector
Version: %ver_major.1
Release: alt1

Summary: GNOME Shell browser connector
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeShellIntegration

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Obsoletes: chrome-gnome-shell < %version
Provides: chrome-gnome-shell =  %EVR

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: desktop-file-utils
BuildRequires: python3-devel python3-module-pygobject3

%description
OS-native connector counterpart for GNOME Shell browser extension.

%prep
%setup
sed -i "s|py\.get_install_dir()|py.get_path('platlib')|" meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %buildroot%_desktopdir/%xdg_name.desktop

%files
%_sysconfdir/chromium/
%_sysconfdir/opt/chrome/
%_bindir/%name
%_bindir/%name-host
%_libdir/mozilla/native-messaging-hosts/
%python3_sitelibdir/%pypi_name/
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%xdg_name.png
%doc NEWS README*

%changelog
* Sun Sep 11 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- first build for Sisyphus

