%define _unpackaged_files_terminate_build 1

Name: system-backup
Version: 0.1.5
Release: alt2

Summary: Script for local system backup
Group: Archiving/Backup
License: GPLv3+

Url: http://www.altlinux.org/Rescue/Recovery
Source: %name-%version.tar
BuildArch: noarch

Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: bash
Requires: btrfs-progs
Requires: coreutils
Requires: e2fsprogs
Requires: gawk
Requires: jfsutils
Requires: kmod
Requires: pigz
Requires: pv
Requires: sed
Requires: sfdisk
Requires: tar
Requires: util-linux
Requires: xfsprogs
AutoReq: noshell, noshebang

%description
Script for creation full backup of the installed ALT Linux.
This backup solution restricted by local mounted storages.

%prep
%setup

%install
mkdir -p -m 0755 %buildroot%_bindir
install -p -m 0755 %name %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Wed Dec 24 2025 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt2
- Fixed significant regression (ALT #57339).

* Fri Dec 19 2025 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt1
- Added support for installer-feature-swapfile;
- Added basic support for the 'timeshift' layout;
- The backup version changed to 0.2, it includes:
  + SWPFILE (the size and name of the swap file);
  + TMSHIFT (a Timeshift-partitioned device info);
  + root.sub (btrfs subvolume info for @ / ROOT);
  + home.sub (btrfs subvolume info for @home / HOME);
  + root.opts (mount options for the ROOT subvolume);
  + home.opts (mount options for the HOME subvolume);
  + *.jfs, *.xfs, *.btrfs (additional FS information);
  + now the NONVRAM file is not empty when it created;
  + all these objects are optional;
- Also added multiple code and style improvements.

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

