Name:    RVVM
Version: 0.6
Release: alt1

Summary: The RISC-V Virtual Machine
License: GPL-3.0
Group:   Emulators
URL:     https://github.com/LekKit/RVVM/wiki
Vcs:     https://github.com/LekKit/RVVM.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)


%description
RVVM is a virtual machine / emulator for RISC-V guests, which
emphasizes on performance, security, lean code and portability.
It already runs a lot of guest operating systems, including
Linux, Haiku, FreeBSD, OpenBSD, etc. It also aims to run RISC-V
applications on a foreign-arch host without full OS guest &
isolation (Userland emulation).

RVVM features include:
- fully spec-compliant rv64imafdcb instruction set;
- Zkr/Zicbom/Zicboz/Sstc extensions;
- tracing JIT with x86_64, ARM64, RISC-V backends (faster than QEMU TCG);
- working OpenSBI & U-Boot, Linux, FreeBSD, OpenBSD, Haiku guests:
- framebuffer display, HID mouse & keyboard, UART terminal;
- NVMe storage drives, TRIM support (Deallocate space on host)
- fast multi-threaded IO;
- networking userland stack (Works on any host OS);
- VFIO PCIe passthrough (For GPUs, etc).


%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebuginfo \
    %nil
%cmake_build

%install
install -Dm755 %_cmake__builddir/rvvm  %buildroot%_bindir/rvvm

%files
%doc README.md
%_bindir/*

%changelog
* Mon Sep 22 2025 Ivan A. Melnikov <iv@altlinux.org> 0.6-alt1
- initial build
