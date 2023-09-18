
Summary: Cloud image management utilities
Name: cloud-utils
Version: 0.33
Release: alt1
License: GPLv3
Group: System/Configuration/Boot and Init
Url: https://launchpad.net/cloud-utils

# vcs git: https://git.launchpad.net/cloud-utils
Source: %name-%version.tar

BuildArch: noarch

Requires: %name-growpart
Requires: %name-cloud-localds
Requires: %name-write-mime-multipart
Requires: %name-ec2metadata
Requires: %name-resize-part-image
Requires: %name-mount-image-callback
BuildRequires(pre): rpm-build-python3

%description
This package provides a useful set of utilities for managing cloud images.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.

%package growpart
Summary: Script for growing a partition
Group: System/Configuration/Boot and Init

Requires: gawk
Requires: gdisk
Requires: sfdisk
Requires: util-linux

%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%package cloud-localds
Summary: A script for creating a nocloud configuration disk for cloud-init
Group: System/Configuration/Boot and Init

Requires: tar
Requires: dosfstools
Requires: mtools
Requires: genisoimage
Requires: qemu-img
Requires: /usr/bin/qemu-img

%description cloud-localds
This package provides the cloud-localds script, which creates a disk-image
with user-data and/or meta-data for cloud-init.

%package write-mime-multipart
Summary: A utilty for creating mime-multipart files
Group: System/Configuration/Boot and Init

%description write-mime-multipart
This package provides the write-mime-multipart script, which creates
mime multipart files that can be consumed by cloud-init as user-data.

%package ec2metadata
Summary: A script to query and display EC2 AMI instance metadata
Group: System/Configuration/Boot and Init

%description ec2metadata
This package provides the ec2metadata script, which can be used to query and
display EC2 instance metadata rekated to an AMI instance.

%package resize-part-image
Summary: A script for resizing cloud images
Group: System/Configuration/Boot and Init

Requires: file
Requires: gzip
Requires: e2fsprogs
Requires: gawk
Requires: tar

%description resize-part-image
This package provides the resize-part-image script, which can be used to
resize a partition image and the contained filesystem to a new size.

%package mount-image-callback
Summary: A script to run commands over cloud image contents
Group: System/Configuration/Boot and Init

Requires: gawk
Requires: util-linux
Requires: qemu-img
Requires: /usr/bin/qemu-img

%description mount-image-callback
This package provides the mount-image-callback script, which mounts a cloud
image to a temporary mountpoint and runs a specified command on the contents.

%package vcs-run
Summary: Script to run commands over a VCS repository contents
Group: System/Configuration/Boot and Init

Requires: breezy
Requires: git-core
Requires: mercurial
Requires: wget

%description vcs-run
This package provides the vcs-run script, which fetches a code repository
into a temporary directory and runs a user-specified command in it.

%prep
%setup

%build

%install
%makeinstall_std

# Exclude Ubuntu-specific tools
rm -f %buildroot%_bindir/*ubuntu*

%files
%doc README.md ChangeLog

%files growpart
%doc README.md ChangeLog
%_bindir/growpart
%_man1dir/growpart.*

%files cloud-localds
%doc README.md ChangeLog
%_bindir/cloud-localds
%_man1dir/cloud-localds.*

%files write-mime-multipart
%doc README.md ChangeLog
%_bindir/write-mime-multipart
%_man1dir/write-mime-multipart.*

%files ec2metadata
%doc README.md ChangeLog
%_bindir/ec2metadata

%files resize-part-image
%doc README.md ChangeLog
%_bindir/resize-part-image
%_man1dir/resize-part-image.*

%files mount-image-callback
%doc README.md ChangeLog
%_bindir/mount-image-callback

%files vcs-run
%doc README.md ChangeLog
%_bindir/vcs-run

%changelog
* Mon Sep 18 2023 Alexander Stepchenko <geochip@altlinux.org> 0.33-alt1
- 0.32 -> 0.33
- Separate scripts into their own packages and don't require vcs-run

* Mon Aug 02 2021 Andrey Cherepanov <cas@altlinux.org> 0.32-alt1.1
- Remove deprecated euca2ools from build requirements.

* Tue May 25 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.32-alt1
- 0.32
- FTBFS: rpm-build-python3

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 0.31-alt1
- 0.31

* Thu Sep 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.30-alt1
- 0.30

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.29-alt1.20161024
- bzr snapshot 20161024

* Thu Dec 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.27-alt1.20151203
- Initial build upstream snapshot

