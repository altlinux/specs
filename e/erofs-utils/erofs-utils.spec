%define _bindir /sbin
%define _name erofs

%def_enable fuse
%def_enable check

Name: %_name-utils
Version: 1.9.2
Release: alt1

Summary: Userspace tools for EROFS
Group: System/Kernel and hardware
License: GPL-2.0-or-later
Url: https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils

Vcs: https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libdeflate)
BuildRequires: pkgconfig(libxxhash)
%{?_enable_fuse:BuildRequires: pkgconfig(fuse3)}

%description
Userspace tools for Enhanced Read-Only File System.

%package -n fuse-%_name
Summary: EROFS fuse3 driver
Group: System/Kernel and hardware
Requires: %name = %EVR
Requires: fuse3

%description -n fuse-%_name
This package provides EROFS driver for FUSE3.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    %{subst_enable fuse}
%nil
%make_build

%install
%makeinstall_std

%check
%make -k check VERBOSE=1

%files
%_sbindir/mount.erofs
%_bindir/dump.erofs
%_bindir/fsck.erofs
%_bindir/mkfs.erofs
%_man1dir/*
%_man8dir/mount.erofs.8*
%{?_enable_fuse:%exclude %_man1dir/erofsfuse.1*}
%doc ChangeLog README*

%{?_enable_fuse:
%files -n fuse-%_name
%_bindir/erofsfuse
%_man1dir/erofsfuse.1*}

%changelog
* Thu Jul 02 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Wed Mar 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Sat Dec 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.10-alt1
- 1.8.10


