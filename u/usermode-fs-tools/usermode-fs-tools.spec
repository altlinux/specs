Name: usermode-fs-tools
Version: 1.3
Release: alt1

Summary: User-mode filesystems utilities
License: GPL-3
Group: File tools

Source: %name-%version.tar
Url: https://www.altlinux.org/Usermode-fs-tools
Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: usermode-extfs-tools = %version-%release
Requires: usermode-vfat-tools  = %version-%release
Requires: usermode-image-tools = %version-%release
Requires: usermode-isofs-tools = %version-%release

%description
This package contains common build parts and requirements.

%package -n usermode-extfs-tools
Summary: User-mode ext2/3/4 filesystems utilities
Group: File tools
BuildArch: noarch

Requires: coreutils
Requires: e2fsprogs
Requires: fakeroot
Requires: gawk
Requires: getopt
Requires: grep
Requires: lsblk
Requires: sed

%description -n usermode-extfs-tools
This package contains ext2/3/4 filesystems utilities.

%package -n usermode-vfat-tools
Summary: User-mode vfat filesystem utilities
Group: File tools
BuildArch: noarch

Requires: coreutils
Requires: dosfstools
Requires: getopt
Requires: mtools

%description -n usermode-vfat-tools
This package contains vfat filesystem utilities.

%package -n usermode-image-tools
Summary: User-mode boot loader and disk image utilities
Group: File tools

Requires: coreutils
Requires: fdisk
Requires: getopt
Requires: grep
Requires: sed
Requires: sfdisk
Requires: util-linux

%ifarch x86_64
Requires: alt-uefi-certs
Requires: pesign
Requires: shim-signed
%endif
%ifarch x86_64 aarch64
Requires: grub-efi
%endif
%ifarch %ix86 x86_64
Requires: grub-pc
%endif
%ifarch ppc64le
Requires: grub-ieee1275
%endif

%description -n usermode-image-tools
This package contains user-mode boot loader and disk image utilities.

%package -n usermode-isofs-tools
Summary: User-mode ISO-9660 image repack utilities
Group: File tools
BuildArch: noarch

Requires: coreutils
Requires: cpio
Requires: gawk
Requires: getopt
Requires: p7zip
Requires: rpm
Requires: rsync
Requires: sed
Requires: service
Requires: usermode-extfs-tools = %version-%release
Requires: usermode-vfat-tools  = %version-%release
Requires: usermode-image-tools = %version-%release

%description -n usermode-isofs-tools
This package contains user-mode ISO-9660 image repack utilities.

%prep
%setup

%install
mkdir -pm755 %{buildroot}%_bindir
for tool in *.sh; do
	cat $tool |sed -E 's,\{VERSION\},%version,g' \
			> "%{buildroot}%_bindir/${tool%%%%.*}"
	chmod -- 0755 "%{buildroot}%_bindir/${tool%%%%.*}"
done

%files
%doc README

%files -n usermode-extfs-tools
%_bindir/dev2extfs
%_bindir/dir2extfs
%_bindir/extfs2dir
%_bindir/extfsinfo

%files -n usermode-vfat-tools
%_bindir/dir2vfat
%_bindir/vfat2dir

%files -n usermode-image-tools
%_bindir/grub2dirs
%_bindir/img2parts
%_bindir/parts2img

%files -n usermode-isofs-tools
%_bindir/iso2stick

%changelog
* Fri Jan 28 2022 Leonid Krivoshein <klark@altlinux.org> 1.3-alt1
- dir2extfs.sh: add an option to exclude paths, thx glebfm@.
- grub2dirs, parts2img: boot from single ESP now allowed.

* Sun Jun 13 2021 Leonid Krivoshein <klark@altlinux.org> 1.2-alt1
- iso2stick: added support of the new m-p ISO layouting.
- iso2stick: added --keep-boot/--keep-grub options.

* Thu Jun 10 2021 Nikita Ermakov <arei@altlinux.org> 1.1-alt2
- dev2extfs: Handle the case when a node ends on '/'.

* Mon Nov 16 2020 Leonid Krivoshein <klark@altlinux.org> 1.1-alt1
- New sub-package 'usermode-isofs-tools': iso2stick utility added.
- dir2extfs, dir2vfat, parts2img: more user-friendly sizes input.
- grub2dirs: deprecated option '--root' renamed to '--uuid'.
- grub2dirs: '--foreign' feature added.
- img2parts: bug fix for layout with single partition.

* Thu Oct 15 2020 Leonid Krivoshein <klark@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

