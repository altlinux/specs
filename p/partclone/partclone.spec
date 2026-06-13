%define _unpackaged_files_terminate_build 1

# This need to be repaired:
# configure: checking for JFS Library files ... ...
# checking for ujfs_get_superblk in -ljfs -luuid... no
# configure: error: *** jfs depend library (libjfs) not found
%def_disable jfs

# raiserfs no longer supported by the Linux Kernel
%def_disable reiserfs

# raiser4 no longer supported by the Linux Kernel
%def_disable reiser4

%def_enable xfs
%def_enable fuse
%def_enable apfs
%def_enable exfat
%def_enable checkfs

Name: partclone
Version: 0.3.47
Release: alt3

Summary: File System Clone Utilities
License: GPLv2+
Group: Archiving/Backup

Url: https://partclone.org/
Vcs: https://github.com/Thomas-Tsai/partclone.git
# Upstream: http://sf.net/projects/partclone/files/
Source: https://github.com/Thomas-Tsai/partclone/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: partclone-0.3.47-build.patch

BuildRequires: libblkid-devel
BuildRequires: libe2fs-devel
BuildRequires: libnilfs-devel
BuildRequires: libncursesw-devel
BuildRequires: libntfs-3g-devel
BuildRequires: libuuid-devel
BuildRequires: libssl-devel
BuildRequires: libxxhash-devel
BuildRequires: libisal-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl

%if_enabled xfs
BuildRequires: libxfs-devel
BuildRequires: libuserspace-rcu-devel
%endif

%if_enabled jfs
BuildRequires: jfsutils
%endif

%if_enabled fuse
BuildRequires: libfuse3-devel
%endif

%if_enabled reiserfs
BuildRequires: libprogsreiserfs-devel
%endif

%if_enabled reiser4
BuildRequires: libreiser4-devel
%endif

# Checkfs requires
%if_enabled checkfs
BuildRequires: e2fsprogs
BuildRequires: btrfs-progs
BuildRequires: dosfstools
BuildRequires: f2fs-tools
BuildRequires: hfsprogs
BuildRequires: ntfs-3g

%if_enabled xfs
BuildRequires: xfsprogs
%endif

%if_enabled exfat
BuildRequires: exfatprogs
%endif

%if_enabled reiserfs
BuildRequires: progsreiserfs
%endif

%if_enabled reiser4
BuildRequires: reiser4progs
%endif
%endif

# TODO: build with ufs (need libufs2), jfs (need fixed build of jfsutils)

%description
A set of file system clone utilities, including ext2/3/4,%{?_enable_xfs: xfs,}%{?_enable_jfs: jfs,} nilfs,
minix, f2fs,%{?_enable_reiserfs: reiserfs,}%{?_enable_reiser4: reiser4,}%{?_enable_apfs: apfs,}%{?_enable_exfat: exfat,} btrfs, ntfs, fat and hfs+ file systems.

%prep
%setup
%autopatch -p1
echo '#define git_version "%version"' > src/version.h

%build
%autoreconf
sed -i -E 's/\r$//g' IMAGE_FORMATS.md
# NB: Due to buggy configure checks --disable-somefeature options does not
# switch off configure requirement for correspondent devel packages and
# configure will fail as if --enable-somefeature was in effect.
%configure \
	%{?_enable_checkfs: --enable-fs-test} \
	--enable-btrfs \
	--enable-extfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--enable-f2fs \
	--disable-ufs \
	--disable-vmfs \
	--enable-minix \
	--enable-nilfs2 \
	%{subst_enable fuse} \
	%{subst_enable reiserfs} \
	%{subst_enable reiser4} \
	%{subst_enable exfat} \
	%{subst_enable apfs} \
	%{subst_enable xfs} \
	%{subst_enable jfs} \
	--enable-ncursesw
%make_build CC="gcc"

%install
%makeinstall_std
%find_lang %name
mv -f %buildroot%_datadir/bash-completion/completions/%name{-completion,}

%check
%if_enabled checkfs
cd tests && make check
%endif

%files -f %name.lang
%_sbindir/*
%_man8dir/*
%_datadir/bash-completion/completions/%name
%doc AUTHORS CONTRIBUTORS ChangeLog README.md IMAGE_FORMATS.md SECURITY_TESTING.md

%changelog
* Sat Jun 13 2026 Anton Midyukov <antohami@altlinux.org> 0.3.47-alt3
- NMU: fix build requirements to fix FTBFS.

* Sun Apr 26 2026 Leonid Krivoshein <klark@altlinux.org> 0.3.47-alt2
- switch to upstream git sources
- packaging documentation

* Sun Apr 26 2026 Leonid Krivoshein <klark@altlinux.org> 0.3.47-alt1
- 0.3.47 (closes: #58849)

* Sun Sep 14 2025 Leonid Krivoshein <klark@altlinux.org> 0.3.32-alt2
- Rebuilt with new reiser4 libraries.

* Sun Dec 08 2024 Leonid Krivoshein <klark@altlinux.org> 0.3.32-alt1
- 0.3.32, enable exfat, fix errors and warnings

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
