
Summary: Cloud image management utilities
Name: cloud-utils
Version: 0.27
Release: alt1.20151203
License: GPLv3
Group: System/Configuration/Boot and Init
Url: https://launchpad.net/cloud-utils/trunk/0.27/+download/cloud-utils-0.27.tar.gz


Source0: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildArch: noarch

Requires: cloud-utils-growpart
Requires: gawk
Requires: e2fsprogs
Requires: euca2ools
Requires: file
Requires: qemu-img
Requires: util-linux

%description
This package provides a useful set of utilities for managing cloud images.

The euca2ools package (a dependency of cloud-utils) provides an Amazon EC2 API
compatible set of utilities for bundling kernels, ramdisks, and root
filesystems, and uploading them to either EC2 or UEC.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.

%package growpart
Summary: Script for growing a partition
Group: System/Configuration/Boot and Init

Requires: gawk
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk
Requires: sfdisk
Requires: util-linux

%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%prep
%setup
%patch1 -p1

%build

%install
%makeinstall_std

# Exclude Ubuntu-specific tools
rm -f %buildroot%_bindir/*ubuntu*

%files
%doc ChangeLog
%_bindir/*
%_man1dir/*
%exclude %_bindir/growpart
%exclude %_man1dir/growpart.*

%files growpart
%doc ChangeLog
%_bindir/growpart
%_man1dir/growpart.*

%changelog
* Thu Dec 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.27-alt1.20151203
- Initial build upstream snapshot

