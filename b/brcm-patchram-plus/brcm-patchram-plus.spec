Name: brcm-patchram-plus
Version: 1.1.20161117
Release: alt1

Summary: Tool to patch Broadcom Bluetooth chips.
License: Apache-2.0
Group: System/Base
URL: https://gitlab.com/firefly-linux/external/rkwifibt/
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Source: %name-%version.tar
BuildRequires: gcc

%description
This program downloads a patchram files in the HCD format
to Broadcom Bluetooth based silicon and combo chips
and other utility functions.

%prep
%setup

%build
gcc -o brcm_patchram_plus brcm_patchram_plus.c

%install
%__install -Dp -m0755 brcm_patchram_plus %buildroot%_bindir/brcm_patchram_plus

%files
%_bindir/brcm_patchram_plus

%changelog
* Tue Mar 18 2025 Nazarov Denis <nenderus@altlinux.org> 1.1.20161117-alt1
- Update to 1.1 20161117
- Build without systemd service

* Fri Mar 27 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.1.1-alt1
- Initial build
