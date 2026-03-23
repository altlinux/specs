%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: fuse-overlayfs
Version: 1.16
Release: alt1

Summary: An implementation of overlay+shiftfs in FUSE for rootless containers
License: GPLv2+
Group: System/Kernel and hardware
Url: https://github.com/containers/fuse-overlayfs
Vcs: https://github.com/containers/fuse-overlayfs

Source0: %name-%version.tar

# We always run autogen.sh
BuildRequires: autoconf automake
#BuildRequires: git
BuildRequires: gcc
BuildRequires: libfuse3-devel
Requires: fuse3

%description
%summary.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_modulesloaddir
echo fuse > %buildroot%_modulesloaddir/fuse-overlayfs.conf

%files
%doc COPYING
%_bindir/%name
%_man1dir/*
%_modulesloaddir/fuse-overlayfs.conf

%changelog
* Mon Mar 23 2026 Denis Rastyogin <gerben@altlinux.org> 1.16-alt1
- Updated to 1.16.

* Mon Aug 25 2025 Denis Rastyogin <gerben@altlinux.org> 1.15-alt1
- Updated to 1.15.

* Tue Apr 22 2025 Denis Rastyogin <gerben@altlinux.org> 1.14-alt1
- Updated to 1.14.

* Mon Feb 20 2023 Stepan Paksashvili <paksa@altlinux.org> 1.10-alt1
- 1.10

* Sat Jul 25 2020 Alexey Gladkov <legion@altlinux.ru> 1.1.2.3.800011b-alt1
- First build for ALTLinux.
