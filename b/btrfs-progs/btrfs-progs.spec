%define _unpackaged_files_terminate_build 1

%ifarch x86_64 aarch64
%def_with check
%else
%def_without check
%endif

Name: btrfs-progs
Version: 6.1.2
Release: alt1

Summary: Utilities for managing the Btrfs filesystem
License: GPLv2
Group: System/Kernel and hardware
Url: http://btrfs.wiki.kernel.org/
VCS: git://git.kernel.org/pub/scm/linux/kernel/git/kdave/btrfs-progs.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: libacl-devel
BuildRequires: libe2fs-devel
BuildRequires: libuuid-devel
BuildRequires: zlib-devel
BuildRequires: libblkid-devel
BuildRequires: libattr-devel
BuildRequires: liblzo2-devel
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: libzstd-devel
BuildRequires: libudev-devel
BuildRequires: libselinux-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%if_with check
BuildRequires: /proc /dev/kvm
BuildRequires: /sbin/dmsetup
BuildRequires: /usr/bin/getfacl
BuildRequires: /sbin/udevadm
BuildRequires: rpm-build-vm
BuildRequires: libaio-devel
BuildRequires: liburing-devel
%endif

%description
Btrfs (B-tree FS or usually pronounced "Butter FS") is a copy-on-write
file system for Linux. It was created as a response to the ZFS filesystem,
in order to replace the ext3 file system while removing a number of its
limitations, particularly with respect to file size, total file system size
and filesystem check duration; it is also expected to implement modern
filesystem features not supported by ext3, like writable snapshots,
snapshots of snapshots, builtin RAID support, and subvolumes. In addition,
Btrfs claims a "focus on fault tolerance, repair and easy administration".

This package contains utilities for managing the Btrfs filesystem

%package -n libbtrfs-devel
Summary:	btrfs filesystem-specific libraries and headers
Group:		Development/C
Requires:	libbtrfs = %version-%release
Provides:	%name-devel

%description -n libbtrfs-devel
btrfs-progs-devel contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

You should install btrfs-progs-devel if you want to develop
btrfs filesystem-specific programs.


%package -n libbtrfs
Summary:	btrfs filesystem-specific libraries and headers
Group:		System/Kernel and hardware

%description -n libbtrfs
btrfs-progs-devel contains shared libraries needed to
btrfs filesystem-specific programs.


%prep
%setup -q
%patch0 -p1

%build
autoreconf -fisv -I m4
automake --add-missing ||:
%configure --disable-python \
	   --disable-static \
	   --with-pkgconfigdir=%_pkgconfigdir \
	   #
%make_build

%install
%makeinstall_std bindir=/sbin libdir=/%_lib incdir=/%_includedir/
mkdir -p %buildroot%_libdir %buildroot%_bindir
LIBNAME=`basename \`ls $RPM_BUILD_ROOT/%{_lib}/libbtrfs.so.*.*\``
ln -s ../../%_lib/$LIBNAME %buildroot%_libdir/libbtrfs.so 
LIBUTILNAME=`basename \`ls $RPM_BUILD_ROOT/%{_lib}/libbtrfsutil.so.*.*\``
ln -s ../../%_lib/$LIBUTILNAME %buildroot%_libdir/libbtrfsutil.so
ln -s ../../sbin/btrfs %buildroot%_bindir/btrfs
rm -f %buildroot/%{_lib}/libbtrfs.so
rm -f %buildroot/%{_lib}/libbtrfsutil.so

%check
# failed: setfattr -n user.foo -v bar1 /usr/src/RPM/BUILD/btrfs-progs-5.16/tests/mnt/acls/acls.1
rm -rf tests/convert-tests/001-ext2-basic
rm -rf tests/convert-tests/002-ext3-basic
rm -rf tests/convert-tests/003-ext4-basic
rm -rf tests/convert-tests/005-delete-all-rollback

rm -rf tests/convert-tests/*-reiserfs-*

# mknod is not allowed in virtual environment
rm -rf tests/mkfs-tests/009-special-files-for-rootdir
# don't run all fuzzing tests
rm -rf tests/fuzz-tests/0*

# Needs 'null_blk' kernel module
rm -rf tests/mkfs-tests/025-zoned-parallel

rm -rf "$HOME/new_tmp"
mkdir "$HOME/new_tmp"
TMPDIR="$HOME/new_tmp"
vm-run --sbin --udevd --kvm=cond make V=1 TEST_LOG=dump test-mkfs

%files
/sbin/*
%_bindir/btrfs
%_bindir/*
%_udevrulesdir/*.rules
%_man8dir/*
%_man5dir/*

%files -n libbtrfs
/%_lib/*.so.*

%files -n libbtrfs-devel
%_libdir/*.so
%_pkgconfigdir/libbtrfsutil.pc
%_includedir/*

%changelog
* Sat Jan 07 2023 Egor Ignatov <egori@altlinux.org> 6.1.2-alt1
- new version 6.1.2

* Fri Dec 30 2022 Egor Ignatov <egori@altlinux.org> 6.1-alt1
- new version 6.1

* Wed Nov 30 2022 Egor Ignatov <egori@altlinux.org> 6.0.2-alt1
- new version 6.0.2

* Mon Nov 07 2022 Egor Ignatov <egori@altlinux.org> 6.0.1-alt1
- new version 6.0.1

* Tue Sep 13 2022 Egor Ignatov <egori@altlinux.org> 5.19.1-alt1
- new version 5.19.1

* Thu Sep 01 2022 Egor Ignatov <egori@altlinux.org> 5.19-alt1
- new version 5.19

* Tue Jun 21 2022 Egor Ignatov <egori@altlinux.org> 5.18.1-alt2
- fix tests

* Mon Jun 20 2022 Anton Farygin <rider@altlinux.ru> 5.18.1-alt1
- 5.18 -> 5.18.1

* Mon May 30 2022 Anton Farygin <rider@altlinux.ru> 5.18-alt1
- 5.16.2 -> 5.18

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 5.16.2-alt1
- 5.16.1 -> 5.16.2

* Thu Feb 10 2022 Anton Farygin <rider@altlinux.ru> 5.16.1-alt1
- 5.16 -> 5.16.1

* Mon Jan 17 2022 Anton Farygin <rider@altlinux.ru> 5.16-alt1
- 5.15.1 -> 5.16
- enabled tests

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 5.15.1-alt1
- 5.15 -> 5.15.1

* Sat Nov 06 2021 Anton Farygin <rider@altlinux.ru> 5.15-alt1
- 5.14.2 -> 5.15

* Sun Oct 17 2021 Anton Farygin <rider@altlinux.ru> 5.14.2-alt3
- fixed typo in libbtrfsutil.so symlink (closes: #41143)

* Sun Oct 17 2021 Anton Farygin <rider@altlinux.ru> 5.14.2-alt2
- added libbtrfsutil.so to the devel package (closes: #41137)

* Sat Oct 16 2021 Anton Farygin <rider@altlinux.ru> 5.14.2-alt1
- 5.14.2

* Fri Sep 24 2021 Anton Farygin <rider@altlinux.ru> 5.14.1-alt1
- 5.14.1

* Tue Sep 14 2021 Anton Farygin <rider@altlinux.ru> 5.14-alt1
- 5.14

* Mon Aug 02 2021 Anton Farygin <rider@altlinux.ru> 5.13.1-alt1
- 5.13.1

* Mon Jul 26 2021 Anton Farygin <rider@altlinux.ru> 5.13-alt1
- 5.13

* Mon May 17 2021 Anton Farygin <rider@altlinux.ru> 5.12.1-alt1
- 5.12.1

* Thu Mar 25 2021 Anton Farygin <rider@altlinux.org> 5.11.1-alt1
- 5.11.1

* Tue Mar 09 2021 Anton Farygin <rider@altlinux.org> 5.11-alt1
- 5.11

* Mon Mar 01 2021 Anton Farygin <rider@altlinux.org> 5.10.1-alt1
- 5.10.1

* Fri Jan 22 2021 Anton Farygin <rider@altlinux.org> 5.10-alt1
- 5.10

* Mon Nov 02 2020 Anton Farygin <rider@altlinux.ru> 5.9-alt1
- 5.9

* Fri Jul 10 2020 Anton Farygin <rider@altlinux.ru> 5.7-alt1
- 5.7

* Wed May 20 2020 Anton Farygin <rider@altlinux.ru> 5.6.1-alt1
- 5.6.1

* Mon Apr 20 2020 Anton Farygin <rider@altlinux.ru> 5.6-alt1
- 5.6

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 5.4.1-alt1
- 5.4.1

* Tue Dec 10 2019 Anton Farygin <rider@altlinux.ru> 5.4-alt1
- 5.4

* Wed Nov 20 2019 Anton Farygin <rider@altlinux.ru> 5.3.1-alt1
- 5.3.1

* Sun Sep 08 2019 Anton Farygin <rider@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Tue Jun 18 2019 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Tue May 28 2019 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- 5.1

* Tue Mar 12 2019 Anton Farygin <rider@altlinux.ru> 4.20.2-alt1
- 4.20.2

* Fri Jan 25 2019 Anton Farygin <rider@altlinux.ru> 4.20.1-alt1
- 4.20.1

* Mon Dec 10 2018 Anton Farygin <rider@altlinux.ru> 4.19.1-alt1
- 4.19.1

* Mon Nov 26 2018 Anton Farygin <rider@altlinux.ru> 4.19-alt2
- added symlink %_bindir/btrfs to /sbin/btrfs (closes: #35641)
- added udev rules for frendly names in /dev/mapper (closes: #35646)

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 4.19-alt1
- 4.19

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 4.17.1-alt1
- 4.17.1

* Tue Jun 26 2018 Anton Farygin <rider@altlinux.ru> 4.17-alt1
- 4.17

* Tue May 22 2018 Anton Farygin <rider@altlinux.ru> 4.16.1-alt1
- 4.16.1

* Wed Apr 11 2018 Anton Farygin <rider@altlinux.ru> 4.16-alt2
- Fix up headers location (closes: #34792)

* Tue Apr 10 2018 Anton Farygin <rider@altlinux.ru> 4.16-alt1
- 4.16
- new feature - python bindings was temporary disabled (for sisyphus migration to python 3.6)
 
* Thu Feb 22 2018 Anton Farygin <rider@altlinux.ru> 4.15.1-alt1
- new version

* Wed Jan 10 2018 Anton Farygin <rider@altlinux.ru> 4.14.1-alt1
- new version

* Sun Dec 10 2017 Anton Farygin <rider@altlinux.ru> 4.14-alt1
- new version

* Mon Oct 23 2017 Anton Farygin <rider@altlinux.ru> 4.13.3-alt1
- new version

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 4.13.2-alt1
- new version

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 4.13.1-alt1
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 4.13-alt1
- new version

* Fri Aug 04 2017 Anton Farygin <rider@altlinux.ru> 4.12-alt1
- new version

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 4.11.1-alt1
- new version

* Wed May 24 2017 Anton Farygin <rider@altlinux.ru> 4.11-alt1
- new version

* Tue May 09 2017 Anton Farygin <rider@altlinux.ru> 4.10.2-alt1
- new version

* Mon Mar 27 2017 Anton Farygin <rider@altlinux.ru> 4.10.1-alt1
- new version

* Mon Mar 13 2017 Anton Farygin <rider@altlinux.ru> 4.10-alt1
- new version

* Sat Feb 04 2017 Anton Farygin <rider@altlinux.ru> 4.9.1-alt1
- new version

* Mon Dec 26 2016 Anton Farygin <rider@altlinux.ru> 4.9-alt1
- new version

* Wed Dec 14 2016 Anton Farygin <rider@altlinux.ru> 4.8.5-alt1
- new version

* Tue Nov 29 2016 Anton Farygin <rider@altlinux.ru> 4.8.4-alt1
- new version (closes: #32818)

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 4.8.3-alt1
- new version

* Mon Oct 17 2016 Anton Farygin <rider@altlinux.ru> 4.8.1-alt1
- new version

* Sun Oct 02 2016 Anton Farygin <rider@altlinux.ru> 4.7.3-alt1
- new version

* Tue Sep 13 2016 Anton Farygin <rider@altlinux.ru> 4.7.2-alt1
- new version

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 4.7.1-alt1
- new version

* Wed Jun 29 2016 Anton Farygin <rider@altlinux.ru> 4.6.1-alt1
- new version

* Mon Jun 20 2016 Anton Farygin <rider@altlinux.ru> 4.6-alt1
- new version

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 4.5.3-alt1
- new version

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 4.4.2-alt1
- new version

* Wed Apr 06 2016 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- new version

* Mon Nov 23 2015 Anton Farygin <rider@altlinux.ru> 4.3.1-alt1
- new version

* Sat Oct 17 2015 Anton Farygin <rider@altlinux.ru> 4.2.2-alt1
- new version

* Thu Jun 25 2015 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- new version

* Mon May 25 2015 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1
- new version

* Wed May 20 2015 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- new version

* Tue Mar 31 2015 Anton Farygin <rider@altlinux.ru> 3.19.1-alt1
- new version

* Sun Mar 15 2015 Anton Farygin <rider@altlinux.ru> 3.19-alt1
- new version

* Fri Jan 30 2015 Anton Farygin <rider@altlinux.ru> 3.18.2-alt1
- new version

* Mon Jan 19 2015 Anton Farygin <rider@altlinux.ru> 3.18.1-alt1
- new version

* Fri Jan 16 2015 Anton Farygin <rider@altlinux.ru> 3.18-alt1
- new version

* Tue Nov 18 2014 Anton Farygin <rider@altlinux.ru> 3.17.1-alt1
- new version

* Mon Oct 06 2014 Anton Farygin <rider@altlinux.ru> 3.16.2-alt1
- new version

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 3.16-alt1
- new version

* Thu Jun 05 2014 Anton Farygin <rider@altlinux.ru> 3.14.2-alt1
- new version

* Mon Apr 21 2014 Anton Farygin <rider@altlinux.ru> 3.14.1-alt1
- new version

* Fri Apr 18 2014 Anton Farygin <rider@altlinux.ru> 3.14-alt1
- new version

* Wed Mar 26 2014 Anton Farygin <rider@altlinux.ru> 3.12-alt2
- fixed build on ARM

* Tue Mar 25 2014 Anton Farygin <rider@altlinux.ru> 3.12-alt1
- new version

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt3.1
- Fixed build

* Sun Feb 20 2011 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt3
- v0.19-35-g1b444cd
- Relocate binaries to /sbin

* Tue Nov 24 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt2
- v0.19-4-gab8fb4c
- Fix BuildRequires

* Sun Sep 06 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt1
- v0.19-1-g4f89b6e

* Thu Jan 29 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.18-alt1
- 0.18

* Wed Jan 21 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt2
- Fixed typo in package name
- Fixed URL

* Tue Jan 13 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt1
- Initial build for ALT Linux
