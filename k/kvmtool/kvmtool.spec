
Name: kvmtool
Version: 3.18.0
Release: alt5.git.e17d182a
Summary: Linux Native KVM Tool
License: GPLv2+
Group: Emulators
Url: https://git.kernel.org/cgit/linux/kernel/git/will/kvmtool.git/
Source: %name-%version.tar

# suse patches
Patch11: nonexec-stack.patch

# rkt patches
Patch21: do_synchronous_writes.patch
Patch22: p9-chown-files-and-dirs-upon-creation.patch
Patch23: quiet-booting.patch
Patch24: terminal_late_fix.patch


BuildRequires: glibc-devel-static
BuildRequires: libaio-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: libfdt-devel
BuildRequires: libvncserver-devel

%description
kvmtool is a lightweight tool for hosting KVM guests. As a pure virtualization
tool it only supports guests using the same architecture, though it supports
running 32-bit guests on those 64-bit architectures that allow this.

%prep
%setup
%patch11 -p1
%patch21 -p1
%patch22 -p1
#patch23 -p1
%patch24 -p1

%build
%make_build V=1 prefix=%prefix

%install
%makeinstall_std prefix=%prefix

%files
%_bindir/lkvm
%doc README COPYING

%changelog
* Mon Jan 23 2023 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt5.git.e17d182a
- update to upstream master (e17d182ad3f797f01947fc234d95c96c050c534b)

* Mon Mar 29 2021 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt4.git.117d6495
- update to upstream master (117d64953228afa90b52f6e1b4873770643ffdc9)

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt3.git.a0eab49a
- update to upstream master (a0eab49a8876ad29a200ce688d1055b566c69b38)

* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt2.git.fdd26ecb
- update to upstream master (fdd26ecb4bc52ac7e06455d5ea2cf5ebf7d500bc)
- add patch from suse for fix build with gcc8
- build with vncserver support

* Thu Feb 08 2018 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1.git.a508ea
- Initial build


