%define _unpackaged_files_terminate_build 1

Name: msm-firmware-loader
Version: 1.8.0
Release: alt1
Summary: Automatically load firmware from device partitions
License: MIT
Group: System/Kernel and hardware
URL: https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader/
VCS: https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader.git

BuildArch: noarch

Source: %name-%version.tar

%description
This script is responsible for loading firmware blobs from firmware
partitions on qcom devices. It will make a dir in tmp, mount all of the
interesting partitions there and then symlink blobs to a single dir that can
be then provided to the kernel. (At this time only single additional
directory can be provided)
This script attempts to load everything at runtime and be as generic
as possible between the target devices: It should allow a single rootfs
to be used on multiple different devices as long as all the blobs
are present on dedicated partitions.

%prep
%setup

%install
install -Dm 0755 %name.sh %buildroot/%_sbindir/%name.sh
install -Dm 0755 %name-unpack.sh %buildroot/%_sbindir/%name-unpack.sh
install -Dm 0644 %name.service %buildroot/%_unitdir/%name.service
install -Dm 0644 %name-unpack.service %buildroot/%_unitdir/%name-unpack.service

%files
%doc README.md
%_sbindir/%name.sh
%_sbindir/%name-unpack.sh
%_unitdir/%name.service
%_unitdir/%name-unpack.service

%changelog
* Thu Jul 30 2026 Vasiliy Doylov <neko@altlinux.org> 1.8.0-alt1
- Initial package for ALT.
