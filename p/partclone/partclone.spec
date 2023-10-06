%def_enable xfs
%def_disable jfs
%def_disable apfs
%ifarch loongarch64 %mips ppc64le
# raiserfs4 does not work with 16k kernel pages
%def_disable reiser4
%else
%def_enable reiser4
%endif
%def_enable checkfs

Name: partclone
Version: 0.3.27
Release: alt1

Summary: File System Clone Utilities
License: GPLv2+
Group: Archiving/Backup

Url: http://partclone.org
# Upstream: git://github.com/Thomas-Tsai/partclone.git
Source: http://download.sourceforge.net/%name/%name-%version.tar
Patch1: partclone-0.3.6-no_fail_mbr.patch
Patch2: partclone-0.3.20-checkfs.patch

# Automatically added by buildreq on Fri Dec 04 2015
# optimized out: libaal-devel libcom_err-devel libncurses-devel libntfs-3g libtinfo-devel pkg-config xz
BuildRequires: libblkid-devel libe2fs-devel libncursesw-devel libntfs-3g-devel libprogsreiserfs-devel libuuid-devel
BuildRequires: libssl-devel
%if_enabled xfs
BuildRequires: libxfs-devel
%endif
%if_enabled jfs
BuildRequires: jfsutils
%endif
%if_enabled reiser4
BuildRequires: libreiser4-devel
%endif

# Checkfs requires
%if_enabled checkfs
BuildRequires: /dev/kvm
BuildRequires: rpm-build-vm
BuildRequires: e2fsprogs btrfs-progs dosfstools reiserfsprogs hfsprogs ntfs-3g
%if_enabled xfs
BuildRequires: xfsprogs
%endif
%if_enabled reiser4
BuildRequires: reiser4progs
%endif
%endif

# TODO: build with ufs (need libufs2), jfs (need fixed build of jfsutils), apfs

%description
A set of file system clone utilities, including ext2/3/4,%{?_enable_xfs: xfs,}%{?_enable_jfs: jfs,}
reiserfs,%{?_enable_reiser4: reiser4,}%{?_enable_apfs: apfs,} btrfs, ntfs, fat and hfs+ file systems.

%prep
%setup
%patch1 -p1
%patch2 -p1
echo '#define git_version "%version"' > src/version.h

%build
%autoreconf
# NB: Due to buggy configure checks --disable-somefeature options does not
# switch off configure requirement for correspondent devel packages and
# configure will fail as if --enable-somefeature was in effect.
%configure \
	%{?_enable_checkfs: --enable-fs-test} \
	--enable-btrfs \
	--enable-extfs \
	--enable-reiserfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--disable-vmfs \
	%{subst_enable reiser4} \
	%{subst_enable apfs} \
	%{subst_enable xfs} \
	%{subst_enable jfs} \
	--enable-ncursesw
%make_build CC="gcc"

%install
%makeinstall_std
%find_lang %name

%check
%if_enabled checkfs
pushd tests
make check || {
	for fname in *.log; do
		if [ "$fname" != "test-suite.log" ]; then
			echo "*** ${fname%%.log} results ***"
			cat -- "$fname"
			echo "******************************"
			echo
		fi
	done
	false
}
popd
%endif

%files -f %name.lang
%_sbindir/*
%_man8dir/*

%changelog
* Thu Oct 05 2023 Ivan A. Melnikov <iv@altlinux.org> 0.3.27-alt1
- 0.3.27

* Wed Aug 30 2023 Ivan A. Melnikov <iv@altlinux.org> 0.3.25-alt1
- 0.3.25
- disable reiserfs4 on loongarch64, %%mips and ppc64le
- enable and fix tests on ppc64le

* Sun Oct 16 2022 Leonid Krivoshein <klark@altlinux.org> 0.3.20-alt0.1.gitgf5082c4
- Updated to upstream version 0.3.20 from github.
- Improved test suite.

* Sun Dec 20 2020 Leonid Krivoshein <klark@altlinux.org> 0.3.17-alt1
- Updated to upstream version 0.3.17 from SourceForge.
- Dropped VMFS support.

* Wed Feb 19 2020 Leonid Krivoshein <klark@altlinux.org> 0.3.12-alt1
- Updated to upstream version 0.3.12 from GitHub.
- Fixed upstream sources for suppress few warnings.
- Enabled checkfs test suite based on modern vm-run feature.

* Wed Jul 31 2019 Michael Shigorin <mike@altlinux.org> 0.3.6-alt0.4.git96f986f
- introduce reiser4 knob (on by default)
- minor spec cleanup

* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.6-alt0.3.git96f986f
- Rebuilt with new reiser4 libraries.

* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.6-alt0.2.git96f986f
- Rebuilt with new reiser4 libraries.

* Tue Sep 12 2017 Leonid Krivoshein <klark@altlinux.org> 0.3.6-alt0.1.git96f986f
- Updated upstream version 0.3.6 from GitHub.
- Moved to Archiving/Backup group.

* Sun Apr 24 2016 Denis Medvedev <nbr@altlinux.org> 0.2.84-alt2
- Rebuild for new ntfs-3g.

* Fri Dec 04 2015 Michael Shigorin <mike@altlinux.org> 0.2.84-alt1
- 0.2.84
- use ntfs-3g instead of libntfs
- reenabled XFS support by default
- added debian watch file
- buildreq

* Fri Dec 04 2015 Michael Shigorin <mike@altlinux.org> 0.2.58-alt3.1
- disabled XFS support by default (FTBFS against libxfs-3.1.11-alt1)

* Sat Aug 31 2013 Led <led@altlinux.ru> 0.2.58-alt3
- rebuild with libreiser4 1.0.8 (libreiser4-1.0.so.8)

* Fri Apr 12 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.58-alt2
- Enable XFS support

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.58-alt1
- 0.2.58

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 0.2.45-alt1
- 0.2.45

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 0.2.43-alt1
- 0.2.43

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.2.24-alt1
- 0.2.24

* Sat Apr 23 2011 Victor Forsiuk <force@altlinux.org> 0.2.23-alt1
- 0.2.23

* Fri Apr 22 2011 Victor Forsiuk <force@altlinux.org> 0.2.22-alt1
- 0.2.22
- Fixed build due to e2fsprogs-v1.41.12-107-gefe0b40 API change.
  Thanks to ldv@ for patch.

* Wed Jan 26 2011 Victor Forsiuk <force@altlinux.org> 0.2.17-alt1
- 0.2.17

* Fri Dec 17 2010 Victor Forsiuk <force@altlinux.org> 0.2.16-alt1
- 0.2.16

* Fri Jun 19 2009 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt2
- Built without xfs due to API change.

* Thu Jun 18 2009 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt1
- Built for ALT Linux.
