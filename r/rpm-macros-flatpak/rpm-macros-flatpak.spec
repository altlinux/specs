%define _unpackage_files_terminate_build 1

Name:      rpm-macros-flatpak
Version:   0.3
Release:   alt1

Summary:   Macros for building RPMS for flatpaks
License:   GPL-3.0-or-later
Group:     Development/Tools

URL:       https://altlinux.space/alt-hub/rpm-macros-flatpak
VCS:       https://altlinux.space/alt-hub/rpm-macros-flatpak
Source:    flatpak

Requires:  rpm-build >= 4.0.4-alt78

BuildArch: noarch

%description
Flatpak buildroot setup for /app installs.

%install
install -pDm0644 %SOURCE0 %buildroot%_rpmmacrosdir/z-flatpak

%files
%_rpmmacrosdir/z-flatpak

%changelog
* Sun Sep 27 2026 Anton Osipov <radiolamp@altlinux.org> 0.3-alt1
- Refactor: remove global debuginfo, check and ELF verify overrides.

* Fri Apr 17 2026 Anton Osipov <radiolamp@altlinux.org> 0.2-alt1
- Fix(cmake): add systemd unitdir support and refactor macro syntax.

* Thu Dec 25 2025 Anton Osipov <radiolamp@altlinux.org> 0.1-alt1
- Initial version.
