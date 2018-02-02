Name: mergerfs
Version: 2.23.1
Release: alt1

Summary: A FUSE union filesystem

Group: File tools
License: MIT
Url: https://github.com/trapexit/mergerfs

Packager: Evgenii Terechkov <evg@altlinux.org>

# Source-url: https://github.com/trapexit/mergerfs/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libattr-devel libfuse-devel pandoc

%description
mergerfs is similar to mhddfs, unionfs, and aufs. Like mhddfs in that it too
uses FUSE. Like aufs in that it provides multiple policies for how to handle
behavior.

%prep
%setup

%build
%make_build
make man

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot/sbin/
ln -s ../usr/bin/mount.mergerfs %buildroot/sbin/

%files
%_bindir/mergerfs
%_bindir/mount.mergerfs
/sbin/mount.mergerfs
%_man1dir/*.1*
%doc README.md

%changelog
* Fri Feb 02 2018 Vitaly Lipatov <lav@altlinux.ru> 2.23.1-alt1
- move to classic build from tarball
- new version (2.23.1) with rpmgs script

* Wed Oct 21 2015 Terechkov Evgenii <evg@altlinux.org> 2.7.0-alt1
- 2.7.0
- fsck subpackage (dont require python for main package)

* Mon Sep  7 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sat Sep  5 2015 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Aug 22 2015 Terechkov Evgenii <evg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Linux Sisyphus
