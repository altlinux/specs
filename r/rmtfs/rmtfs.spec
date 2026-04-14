%define _unpackaged_files_terminate_build 1

Name: rmtfs
Version: 1.2
Release: alt1
Summary: Qualcomm Remote Filesystem Service Implementation
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://github.com/linux-msm/rmtfs
VCS: https://github.com/linux-msm/rmtfs.git
ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(qrtr)

%description
%summary

%prep
%setup

%build
%make_build

%install
%makeinstall_std servicedir=%_unitdir bindir=%_bindir prefix=%_prefix

%files
%_bindir/%name
%_unitdir/*.service

%changelog
* Tue Apr 14 2026 Vasiliy Doylov <neko@altlinux.org> 1.2-alt1
- Initial package
