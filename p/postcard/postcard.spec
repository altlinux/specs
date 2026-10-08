%define _unpackaged_files_terminate_build 1
%define app_id in.gxanshu.postcard
%def_with check

Name: postcard
Version: 1.13.0
Release: alt1

Summary: A modern email client for GNOME
License: GPL-3.0
Group: Networking/Mail

URL: https://postcard.gxanshu.in
VCS: https://github.com/gxanshu/postcard

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: gettext-tools

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
Postcard is an email client written in Python using GTK4 and libadwaita.
It supports IMAP/SMTP accounts, HTML messages rendered by WebKitGTK,
a local SQLite cache and password storage through Secret Service.
GNOME Online Accounts integration is available when that service is installed.

%prep
%setup

%build
%meson -Dpython.purelibdir=%_datadir/%name
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test
glib-compile-schemas --strict --dry-run data
desktop-file-validate %buildroot%_desktopdir/%app_id.desktop
PYTHONPATH=src python3 -m pytest -q

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_datadir/%name
%_desktopdir/%app_id.desktop
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%app_id.png
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Tue Oct 06 2026 Vladislav Eliseev <general@altlinux.org> 1.13.0-alt1
- Initial build for ALT.
