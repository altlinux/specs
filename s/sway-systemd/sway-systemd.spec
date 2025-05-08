%define _unpackaged_files_terminate_build 1

Name: sway-systemd
Version: 0.4.1
Release: alt1

Summary: Systemd integration for Sway session
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/alebastr/sway-systemd

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd

BuildRequires: meson
BuildRequires: pkgconfig(systemd)

Requires: python3(Xlib)
Requires: /usr/bin/dbus-update-activation-environment

BuildArch: noarch

Source: %name-%version.tar

%description
The goal of this project is to provide a minimal set of configuration 
files and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session 
   environment.
 - Define sway-session.target for starting user services.
 - Place GUI applications into a systemd scopes for systemd-oomd 
   compatibility.

%prep
%setup -n %name-%version

%build
%meson \
       -Dautoload-configs=all 
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-session.conf
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-cgroups.conf
%config(noreplace) %{_sysconfdir}/sway/config.d/95-system-keyboard-config.conf
%config(noreplace) %{_sysconfdir}/sway/config.d/95-xdg-desktop-autostart.conf
%dir %_libexecdir/%name
%_libexecdir/%name/assign-cgroups.py
%_libexecdir/%name/locale1-xkb-config
%_libexecdir/%name/session.sh
%_libexecdir/%name/wait-sni-ready
%_userunitdir/sway-session.target
%_userunitdir/sway-session-shutdown.target
%_userunitdir/sway-xdg-autostart.target

%changelog
* Thu May 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
