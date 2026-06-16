%define _unpackaged_files_terminate_build 1

Name: proxmox-i18n
Summary: Internationalization support for Proxmox
Version: 3.7.5
Release: alt1
License: AGPL-3.0+
Group: System/Internationalization
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-i18n.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

BuildRequires: perl(Locale/PO.pm) perl(JSON.pm)

%description
%summary.

%package -n pbs-i18n
Summary: Internationalization support for Proxmox Backup Server
Group: System/Internationalization

%description -n pbs-i18n
%summary.

%package -n pmg-i18n
Summary: Internationalization support for Proxmox Mail Gateway
Group: System/Internationalization

%description -n pmg-i18n
%summary.

%package -n pve-i18n
Summary: Internationalization support for Proxmox VE
Group: System/Internationalization

%description -n pve-i18n
%summary.

%package -n pdm-i18n
Summary: Internationalization support for Proxmox Datacenter Manager
Group: System/Internationalization

%description -n pdm-i18n
%summary.

%package -n pve-yew-mobile-i18n
Summary: Internationalization support for Proxmox Virtual Environment (yew PWA)
Group: System/Internationalization

%description -n pve-yew-mobile-i18n
%summary.

%prep
%setup
%patch -p1

%build
%install
%makeinstall_std

%files -n pbs-i18n
%_datadir/pbs-i18n

%files -n pmg-i18n
%_datadir/pmg-i18n

%files -n pve-i18n
%_datadir/pve-i18n

%files -n pdm-i18n
%_datadir/pdm-i18n

%files -n pve-yew-mobile-i18n
%_datadir/pve-yew-mobile-i18n

%changelog
* Mon Jun 08 2026 Sergey Konev <darisishe@altlinux.org> 3.7.5-alt1
- 3.7.5

* Tue Jan 20 2026 Sergey Konev <darisishe@altlinux.org> 3.6.6-alt1
- 3.6.6

* Sat Sep 27 2025 Sergey Konev <darisishe@altlinux.org> 3.6.0-alt2
- Translations for PVE Mobile Web UI

* Thu Sep 18 2025 Sergey Konev <darisishe@altlinux.org> 3.6.0-alt1
- 3.6.0 (Closes: #56046)
- Translations for PDM

* Fri Apr 18 2025 Sergey Konev <darisishe@altlinux.org> 3.4.2-alt1
- 3.4.2
- update Russian translation

* Tue Jan 21 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.3.3-alt2
- more Russian translation fixes (thnx lepata@) (Closes: #52785)

* Tue Jan 21 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.3.3-alt1
- 3.3.3
- update Russian translation (Closes: #52784)

* Mon Dec 16 2024 Sergey Konev <darisishe@altlinux.org> 3.3.2-alt1
- 3.3.2

* Wed Oct 16 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.4-alt1
- 3.2.4

* Mon Sep 30 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.3-alt1
- 3.2.3
- update Russian translation

* Fri Aug 30 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Feb 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.12.1-alt1
- 2.12-1

* Wed Mar 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.11.1-alt1
- 2.11-1
- New Russian translation

* Tue Oct 04 2022 Alexey Shabalin <shaba@altlinux.org> 2.7.2-alt1
- 2.7-2

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7.1-alt1
- 2.7-1

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 2.6-alt1
- initial build as separate package.

