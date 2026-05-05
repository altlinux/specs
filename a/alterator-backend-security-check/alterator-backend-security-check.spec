%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.alterator.securitycheck
%define shortname security-check

Name: alterator-backend-%shortname
Version: 1.0.6
Release: alt1
Summary: Security check tool
Group: System/Configuration/Other
License: GPL-3.0-or-later
Url: https://altlinux.space/vladislavpetrukhin/alterator-backend-security-check
Vcs: https://altlinux.space/vladislavpetrukhin/alterator-backend-security-check

Source0: %name-%version.tar

Requires: alterator-interface-%shortname = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(augeas)

%description
System security tool that checks system configuration with some rules.
Built on Augeas and GLib and provides a D-Bus interface for integration with 
Alterator.

%package -n alterator-interface-%{shortname}
Summary: Security Check interface for Alterator
Group: System/Configuration/Other

%description -n alterator-interface-%{shortname}
%summary.

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
%_datadir/dbus-1/system.d/%app_id.conf
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/polkit-1/rules.d/50-%app_id.rules

%files -n alterator-interface-%shortname
%_datadir/dbus-1/interfaces/%app_id.xml
%_datadir/polkit-1/actions/%app_id.policy

%changelog
* Tue May 05 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.6-alt1
- New version 1.0.6.
- Add .mo files (Closes: #58989).
- Separating d-bus interface into another package (Closes: #58990).

* Thu Apr 09 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.5-alt1
- New version 1.0.5.

* Tue Mar 17 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.4-alt1
- New version 1.0.4.

* Wed Mar 04 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.3-alt1
- New version 1.0.3.

* Thu Jan 29 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.2-alt1
- Initial build.
