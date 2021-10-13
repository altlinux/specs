Name: fakechroot
Version: 2.20.1
Release: alt3
Summary: Gives a fake chroot environment
Group: Development/Tools
License: LGPLv2+
Url: https://github.com/dex4er/fakechroot
# Repacked %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch: fakechroot-2.20.1-add-statx-support.patch
Patch1: pull-85-0001-tmpnam.c-fix-heap-overflow.patch
Patch2: pull-85-0002-declare-missing-bufs-remove-ver-from-lstat.patch
Patch3: pull-85-0003-fix-glibc-2.33-compatibility.patch
Patch4: pull-85-0006-wrap-fstatat-and-fstatat64.patch


# Automatically added by buildreq on Wed Aug 31 2016
# optimized out: gnu-config perl perl-podlators python-base python3
BuildRequires: perl-devel python3-base

# ldd.fakechroot
Requires: /usr/bin/objdump

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \
#
%make_build

# For dependency-clean %%doc.
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%install
%makeinstall_std
# Drop libtool files
find %buildroot%_libdir -name '*.la' -delete -print

%check
%make check

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%doc NEWS.md README.md
%doc COPYING LICENSE
%_bindir/%name
%_bindir/env.%name
%_bindir/ldd.%name
%_sbindir/chroot.%name
%_libdir/%name/
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/chroot.env
%config(noreplace) %_sysconfdir/%name/debootstrap.env
%config(noreplace) %_sysconfdir/%name/rinse.env
%_mandir/man1/%name.1*

%changelog
* Wed Oct 13 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt3
- Added glibc 2.33+ support patches from
  https://github.com/dex4er/fakechroot/pull/85 (thanks to Ilya Lipnitskiy), and
  https://github.com/dex4er/fakechroot/pull/86 (thanks to neok-m4700).

* Tue Apr 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt2
- Backported upstream commit adding support of libc wrapper for
  statx(1) syscall.

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.20.1-alt1
- Updated to 2.20.1.

* Fri Aug 18 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.19-alt2
- Added support of LFS-compatible fts functions.

* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.19-alt1
- Updated to 2.19.

* Wed Aug 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.18-alt2
- Initial build.
