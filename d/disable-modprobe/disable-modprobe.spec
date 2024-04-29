# SPDX-License-Identifier: CC0
%define _unpackaged_files_terminate_build 1

Name: disable-modprobe
Summary: Disable auto-loading of kernel modules after system is running
Version: 1
Release: alt1
License: CC0
Group: System/Kernel and hardware
BuildArch: noarch

Source: %name-%version.tar

%description
Disable auto-loading of kernel modules (via modprobe) after system is
booted in multi-user mode.

! Please ensure that you comprehend the potential consequences, verify the
operability of the system, and use it at your own risk !

%prep
%setup

%install
install -Dpm644 disable-modprobe.service -t %buildroot%_unitdir
install -Dp disable-modprobe.init -T %buildroot%_initdir/disable-modprobe

%check
sh -n %buildroot%_initdir/disable-modprobe

# Intentionally does not invoke post/preun hooks.

%files
%_initdir/disable-modprobe
%_unitdir/disable-modprobe.service

%changelog
* Mon Apr 15 2024 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
