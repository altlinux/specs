
Summary: Cloud image management utilities
Name: cloud-utils
Version: 0.32
Release: alt1.1
License: GPLv3
Group: System/Configuration/Boot and Init
Url: https://launchpad.net/cloud-utils

# vcs git: https://git.launchpad.net/cloud-utils
Source: %name-%version.tar

BuildArch: noarch

Requires: cloud-utils-growpart
Requires: gawk
Requires: e2fsprogs
Requires: file
Requires: util-linux
Requires: qemu-img
Requires: /usr/bin/qemu-img
BuildRequires(pre): rpm-build-python3

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
Requires: gdisk
Requires: sfdisk
Requires: util-linux

%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%prep
%setup

%build

%install
%makeinstall_std

# Exclude Ubuntu-specific tools
rm -f %buildroot%_bindir/*ubuntu*

%files
%doc README.md ChangeLog
%_bindir/*
%_man1dir/*
%exclude %_bindir/growpart
%exclude %_man1dir/growpart.*

%files growpart
%doc ChangeLog
%_bindir/growpart
%_man1dir/growpart.*

%changelog
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

