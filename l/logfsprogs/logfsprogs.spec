%define _sbindir /sbin
%define fsname logfs
%define Name LogFS
Name: %{fsname}progs
Version: 1.1
Release: alt0.2
Summary: Utilities for the %Name filesystem
License: GPLv2
Group: System/Kernel and hardware
URL: http://github.com/prasad-joshi/%name.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: zlib-devel

%description
%Name is a scalable flash filesystem.
It is aimed to replace JFFS2 for most uses, but focuses more on large devices.
This package contains utilities for the %Name filesystem.


%prep
%setup -q
%patch -p1


%build
export CFLAGS="%optflags"
%make_build


%install
%makeinstall_std BINDIR=%_sbindir
ln -s {mk,%buildroot/sbin/mkfs.}%fsname


%files
%_sbindir/*


%changelog
* Sun Feb 10 2013 Led <led@altlinux.ru> 1.1-alt0.2
- updated from upstream's SCM

* Thu Sep 13 2012 Led <led@altlinux.ru> 1.1-alt0.1
- updated from upstream SCM
- cleaned up spec

* Mon May 31 2010 Led <led@altlinux.ru> 1.1-tmc0.1
- initial build
