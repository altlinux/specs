%define _unpackaged_files_terminate_build 1


Name: alterator-blivet
Version: 1.1.1
Release: alt1

Summary: Alterator module for volume management based on blivet
License: GPLv3
Group: System/Configuration/Other

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-alterator

BuildRequires: alterator guile-devel >= 2.0

Requires: alterator alterator-l10n

Requires: python3-module-blivet
Requires: alterator-python-functions

%description
Alterator module for volume management based on blivet

%prep
%setup

%build
%make_build

%install
%makeinstall
install -Dpm644 blivetstorage/*.py -t %buildroot%python3_sitelibdir/blivetstorage

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_backend3dir/*
%_alterator_libdir/ui/*
%python3_sitelibdir/blivetstorage/*

%changelog
* Sat Mar 21 2026 Sergey Konev <darisishe@altlinux.org> 1.1.1-alt1
- Create ESP RAID1 when btrfs RAID1 is used
- Disable btrfs RAID schemas for BIOS legacy

* Thu Jun 05 2025 Sergey Konev <darisishe@altlinux.org> 1.1.0-alt0.3
- virtualization module: minor i18n fix

* Tue May 06 2025 Sergey Konev <darisishe@altlinux.org> 1.1.0-alt0.2
- virtualization module: create local-btrfs subvolume by default 
  for PVE distro

* Tue Apr 08 2025 Sergey Konev <darisishe@altlinux.org> 1.1.0-alt0.1
- virtualization module: redisigned to provide greater functionality
  Now user can add additional/custom volumes
  Proper BIOS RAIDs and regular Linux RAIDs support
  Fixed crash when zero disks detected
  More fail-proof error handling

* Wed Mar 12 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt0.4
- Proper btrfs compression type handling

* Tue Mar 04 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt0.3
- More user-friendly storage layout and UI approach
  for virtualization module

* Fri Feb 28 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt0.2
- Default chroot path to '/mnt/destination'
  if environment variable is not set

* Tue Feb 04 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt0.1
- Initial package


