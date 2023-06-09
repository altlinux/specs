Summary: FUSE implementation for overlayfs.
Name: fuse-overlayfs

Version: 1.10
Release: alt1
License: GPLv3+

Group: System/Kernel and hardware

URL: https://github.com/containers/fuse-overlayfs

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
%setup -n %name-%version

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
* Mon Feb 20 2023 Stepan Paksashvili <paksa@altlinux.org> 1.10-alt1
- 1.10

* Sat Jul 25 2020 Alexey Gladkov <legion@altlinux.ru> 1.1.2.3.800011b-alt1
- First build for ALTLinux.
