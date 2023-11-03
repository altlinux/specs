Name: mergerfs
Version: 2.33.4
Release: alt1.1

Summary: A FUSE union filesystem

Group: File tools
License: MIT
Url: https://github.com/trapexit/mergerfs

Packager: Evgenii Terechkov <evg@altlinux.org>

# Source-url: https://github.com/trapexit/mergerfs/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libattr-devel libfuse-devel

%description
mergerfs is similar to mhddfs, unionfs, and aufs. Like mhddfs in that it too
uses FUSE. Like aufs in that it provides multiple policies for how to handle
behavior.

%prep
%setup
%ifarch %e2k
sed -i 's/#ifdef O_DSYNC/#if defined(O_DSYNC) \&\& O_DSYNC != O_SYNC/' libfuse/lib/debug.c
%endif
#rm -rf libfuse/
subst "s|chown.*||" libfuse/Makefile
echo >tools/update-version
echo "#pragma once" > src/version.hpp
echo "static const char MERGERFS_VERSION[] = \"%version\";" >> src/version.hpp

%build
%make_build
make man

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot/sbin/
#ln -s ../usr/bin/mount.mergerfs %buildroot/sbin/

%files
%_bindir/mergerfs
%attr(4710,root,fuse) %_bindir/mergerfs-fusermount
/sbin/mount.mergerfs
%_man1dir/*.1*
%doc README.md

%changelog
* Fri Nov 03 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.33.4-alt1.1
- fixed build for Elbrus

* Wed Mar 30 2022 Vitaly Lipatov <lav@altlinux.ru> 2.33.4-alt1
- new version 2.33.4 (with rpmrb script)
- build with internal libfuse again (strict and patched version)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 2.25.1-alt1
- new version 2.25.1 (with rpmrb script)
- build with system libfuse

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
