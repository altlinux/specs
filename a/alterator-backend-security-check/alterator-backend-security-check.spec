%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.alterator.securitycheck

Name: alterator-backend-security-check
Version: 1.0.3
Release: alt1
Summary: Security check tool
Group: System/Configuration/Other
License: GPL-3.0-or-later
Url: https://altlinux.space/vladislavpetrukhin/alterator-backend-security-check
Vcs: https://altlinux.space/vladislavpetrukhin/alterator-backend-security-check

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(augeas)

%description
System security tool that checks system configuration with some rules.
Built on Augeas and GLib and provides a D-Bus interface for integration with 
Alterator.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/dbus-1/system-services/%app_id.service
%_datadir/dbus-1/interfaces/%app_id.xml
%_datadir/dbus-1/system.d/%app_id.conf
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Wed Mar 04 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.3-alt1
- New version 1.0.3.

* Thu Jan 29 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.2-alt1
- Initial build.
