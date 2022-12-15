Name: bees
Version: 0.8
Release: alt1

Summary: Best-Effort Extent-Same, a btrfs deduplication agent

License: GPL3.0-only
Group: File tools
Url: https://github.com/Zygo/bees

# Source-url: https://github.com/Zygo/bees/archive/v%version.tar.gz
Source: %name-%version.tar

# [ppc64le] fiemap.cc:31:67: error: no matching function for call to 'min(__u64&, long long unsigned int)'
ExcludeArch: ppc64le

BuildRequires: gcc-c++
BuildRequires: libuuid-devel

%description
bees is a block-oriented userspace deduplication agent designed for large btrfs
filesystems. It is an offline dedupe combined with an incremental data scan
capability to minimize time data spends on disk from write to dedupe.

Hilights:

* Space-efficient hash table and matching algorithms - can use as little as 1
  GB hash table per 10 TB unique data (0.1GB/TB)
* Daemon incrementally dedupes new data using btrfs tree search
* Works with btrfs compression - dedupe any combination of compressed and uncompressed files
* Persistent hash table for rapid restart after shutdown
* Whole-filesystem dedupe - including snapshots
* Constant hash table size - no increased RAM usage if data set becomes larger
* Works on live data - no scheduled downtime required
* Automatic self-throttling based on system load

%prep
%setup
subst 's|CCFLAGS =.*|CCFLAGS = -Wall -Wextra %optflags|' makeflags

%build
cat >localconf <<-EOF
	SYSTEMD_SYSTEM_UNIT_DIR=%_unitdir
	LIBEXEC_PREFIX=%_bindir
	LIB_PREFIX=%_libdir
	PREFIX=%prefix
	LIBDIR=%_libdir
	DEFAULT_MAKE_TARGET=all
EOF

%make_build BEES_VERSION=%version TAG="no"

%install
%makeinstall_std BEES_VERSION=%version TAG="no"

%files
%doc COPYING
%doc README.md
%_bindir/bees
%_sbindir/beesd
%_unitdir/beesd@.service
%dir %_sysconfdir/bees
%config(noreplace) %_sysconfdir/bees/beesd.conf.sample

%changelog
* Fri Dec 16 2022 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- new version 0.8 (with rpmrb script)

* Sun Jan 23 2022 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- new version 0.7 (with rpmrb script)

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt0.pre
- build pre 0.6.6 from git 081a6af (see https://github.com/Zygo/bees/issues/187)

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- initial build for ALT Sisyphus

