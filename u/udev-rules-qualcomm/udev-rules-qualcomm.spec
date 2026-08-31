%define _unpackaged_files_terminate_build 1

Name: udev-rules-qualcomm
Version: 1
Release: alt1
Summary: Udev rules for Qualcomm devices
License: MIT
Group: System/Kernel and hardware

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%install
install -pDm0644 72-qualcomm.rules %buildroot%_udevrulesdir/72-qualcomm.rules

%files
%_udevrulesdir/72-qualcomm.rules

%changelog
* Sat Aug 29 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT.
