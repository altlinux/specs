# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xfstests
Version: 1.1.1
Release: alt1
Summary: XFS QA testsuite
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://git.kernel.org/pub/scm/fs/xfs/xfstests-dev.git
Vcs: https://git.kernel.org/pub/scm/fs/xfs/xfstests-dev.git
# Additional https://github.com/tytso/xfstests-bld

# Autoreqs work for too long.
AutoReq: nopython nopython3 noshell noshebang noperl
Requires: acl
Requires: attr
Requires: bash
Requires: bc
Requires: btrfs-progs
Requires: coreutils
Requires: dmsetup
Requires: e2fsprogs
Requires: keyutils
Requires: libcap-utils
Requires: lvm2
Requires: mount
Requires: perl
Requires: quota
Requires: util-linux
Requires: xfsdump
Requires: xfsprogs
Requires: xz

Source: %name-%version.tar
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbtrfs-devel >= 5.14.2-alt3
BuildRequires: libcap-devel
BuildRequires: libgdbm-devel
BuildRequires: libssl-devel
BuildRequires: liburing-devel
BuildRequires: libuuid-devel
BuildRequires: libxfs-devel
BuildRequires: rpm-build-python
BuildRequires: rpm-build-python3

%description
The XFS regression test suite. Also includes some support for
acl, attr, udf, and nfs testing. Contains around 1600+ specific
tests for userspace & kernelspace.

%prep
%setup

%build
%autoreconf
%add_optflags -Wno-unused-result
%configure \
	--disable-static \
	--exec-prefix=%_libexecdir

%make_build V=1

%install
%makeinstall_std V=1

%files
%doc README* LICENSES/* doc/*
%_libexecdir/xfstests

# It's v1.1.1 released at 2012-12-12 - ecdb4d61 ("xfstests: update version and changelog")
# there just no approrpiate upstream tag.
%changelog
* Sun Oct 17 2021 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt1
- First import of v1.1.0-3481-g47a1238b (2021-10-07).
