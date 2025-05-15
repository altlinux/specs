%define _unpackaged_files_terminate_build 1

Name: system-backup
Version: 0.1.4
Release: alt1

Summary: Script for local system backup
Group: Archiving/Backup
License: GPLv3+

Url: http://www.altlinux.org/Rescue/Recovery
Source: %name-%version.tar
BuildArch: noarch

Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: bash
Requires: coreutils
Requires: kmod
Requires: pigz
Requires: pv
Requires: sfdisk
Requires: tar
Requires: util-linux
AutoReq: noshell, noshebang

%description
Script for creation full backup of the installed ALT Linux.
This backup solution restricted by local mounted storages.

%prep
%setup

%install
mkdir -pm755 %buildroot%_bindir
install -pm755 %name %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Fri May 16 2025 Leonid Krivoshein <klark@altlinux.org> 0.1.4-alt1
- Bug fixes, requirements added, minor improvements.

* Thu Jul 28 2022 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt3
- Requires: pv.

* Fri Jun 21 2019 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt2
- Exclude backup storage directory for all backups.
- Change primary digest algo: MD5->SHA256.

* Fri Jun 21 2019 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt1
- Automatic exclude backup storage directory for self-system backup.
- Determinate filesystem on whole disk drive added.
- Ignore empty /etc/fstab records.
- Cleanup and exclude from backup /mnt/target directory.

* Wed Jun 12 2019 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.

