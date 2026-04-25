%define _unpackaged_files_terminate_build 1

%define service_id org.altlinux.APM

Name: apm
Version: 0.5.0
Release: alt1

Summary: Atomic Package Manager 
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
URL: https://altlinux.space/alt-atomic/apm
VCS: https://altlinux.space/alt-atomic/apm.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

# From v0.1.3 distrobox in optional requires
# Requires: distrobox

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-golang
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libapt-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: /proc

%description
APM is a universal application for managing both system packages
and packages from distrobox. It consolidates all functions into
a single API, provides interaction via a DBUS service, and offers
optional support for atomic images based on ALT Linux.

%prep
%setup -a1
%autopatch -p1

# Fix go vendoring build
for file in $(find -name "*\[generated\]*"); do
  mv -v "$file" "${file//\[generated\]/}"
done

%build
%meson -Dprofile=prod
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_localstatedir/%name
%_cachedir/%name
%_sysconfdir/%name
%_tmpfilesdir/%name.conf
%_bindir/%name
%_sysconfdir/dbus-1/system.d/%service_id.conf
%_unitdir/%name.service
%_datadir/dbus-1/services/%service_id.User.service
%_datadir/dbus-1/system-services/%service_id.service
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_datadir/polkit-1/actions/%service_id.policy
%_sysconfdir/apt/apt.conf.d/99-apm-update.conf
%_datadir/apt/scripts/update-apm.lua
%_datadir/%name/grpconf.d
%doc README.en.md
%doc README.md
%doc README.ru.md

%changelog
* Sat Apr 25 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5.0-alt1
- New version: 0.5.0.
- Added altfiles module for nss-altfiles support: split/merge /etc/passwd and
  /etc/group, patch nsswitch.conf, sync groups from YAML configs.
- Added lint module: analyze and auto-generate tmpfiles.d/sysusers.d configs,
  detect unexpected files in /run and /tmp.
- Added CLI commands: `apm system image lint`, `fix-nss`, `sync-groups`.
- Fixed LC_ALL=C env for distrobox commands (Alt/Arch/Ubuntu providers)
  to ensure consistent output parsing.
- Added APT config overrides support via `--option` / `Options` field.
- Auto-update package database if empty before install operations.
- Fixed format-type CLI flag name (was format_type).
- Added grpconf.d config directory installation.

* Sat Mar 14 2026 Vladimir Romanov <rirusha@altlinux.org> 0.4.0-alt1
- New version 0.4.0.
- Added HTTP API server (Swagger UI, WebSocker, auth via token).
- Added installing local RPM files support and resolving conflicts.
- New AppStream module for applications metainfo.
- Improved package list filtering (OR logic, protection against SQL injection)
- Added new options:
  - --format-type - show text --format via tree ot plain;
  - --output - output only specified fields;
  - --verbose - enable verbose logging to stdout;
  - --option - override APT options.
- Replaced pogreb storage with  SQLite.
- Fixed issues, improved processing of APT transactions and locks.
- Added integration tests (RPM, thread safety).

* Mon Jan 26 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3.3-alt1
- v0.3.3

* Sun Jan 18 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3.1-alt1
- v0.3.1

* Mon Dec 22 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.6-alt1
- v0.2.6

* Wed Dec 03 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.4-alt1
- v0.2.4

* Mon Dec 01 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.3-alt1
- v0.2.3

* Wed Nov 26 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.2-alt1
- v0.2.2

* Wed Nov 12 2025 Vladimir Romanov <rirusha@altlinux.org> 0.1.11-alt1
- v0.1.11

* Tue Nov 11 2025 Vladimir Romanov <rirusha@altlinux.org> 0.1.10-alt1
- v0.1.10

* Tue Sep 23 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.6-alt1
- v0.1.6

* Thu Aug 21 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.5-alt1
- v0.1.5

* Mon Jun 02 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.1-alt1
- Initial build.
