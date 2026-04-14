%define _unpackaged_files_terminate_build 1

Name: pd-mapper
Version: 1.1
Release: alt1
Summary: Userspace implementation of Qualcomm protected domain mapper
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://github.com/linux-msm/pd-mapper
VCS: https://github.com/linux-msm/pd-mapper.git
ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires: pkgconfig(liblzma)
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
%_unitdir/%name.service

%changelog
* Tue Apr 14 2026 Vasiliy Doylov <neko@altlinux.org> 1.1-alt1
- Initial package
