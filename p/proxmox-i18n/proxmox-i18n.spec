%define _unpackaged_files_terminate_build 1

Name: proxmox-i18n
Summary: Internationalization support for Proxmox
Version: 2.11.1
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

%changelog
* Wed Mar 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.11.1-alt1
- 2.11-1
- New Russian translation

* Tue Oct 04 2022 Alexey Shabalin <shaba@altlinux.org> 2.7.2-alt1
- 2.7-2

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7.1-alt1
- 2.7-1

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 2.6-alt1
- initial build as separate package.

