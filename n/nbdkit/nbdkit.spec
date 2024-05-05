# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=relaxed

Name: nbdkit
Version: 1.39.4
Release: alt1
Summary: NBD server with stable plugin ABI and permissive license
License: BSD-3-Clause
Group: System/Servers
Url: https://gitlab.com/nbdkit/nbdkit
Requires: e2fsprogs

Source: %name-%version.tar
# c++ is only required for stats filter.
# zlib-ng overrides zlib except for gzip filter.
BuildRequires: %_bindir/pod2man
BuildRequires: e2fsprogs
BuildRequires: gcc-c++
BuildRequires: pkgconfig(bash-completion)
BuildRequires: pkgconfig(blkio)
BuildRequires: pkgconfig(com_err)
BuildRequires: pkgconfig(ext2fs)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libnbd)
BuildRequires: pkgconfig(libssh)
BuildRequires: pkgconfig(libtorrent-rasterbar)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(zlib-ng)
BuildRequires: xorriso
%{?!_without_check:%{?!_disable_check:
BuildRequires: /dev/pts
BuildRequires: expect
BuildRequires: iproute2
BuildRequires: jq
BuildRequires: libnbd
BuildRequires: qemu-img
BuildRequires: socat
}}

%description
nbdkit is an NBD server. NBD - Network Block Device - is a protocol for
accessing Block Devices (hard disks and disk-like things) over a Network.

The key features of nbdkit are:

* Multithreaded NBD server written in C with good performance.
* Minimal dependencies for the basic server.
* Liberal license (BSD) allows nbdkit to be linked to proprietary
* libraries or included in proprietary code.
* Well-documented, simple plugin API with a stable ABI guarantee.
* Lets you export "unconventional" block devices easily.
* You can write plugins in C/C++, [...], and shell script.
* Filters can be stacked in front of plugins to transform the output.

%package devel
Summary: Development files for nbdkit plugins and filters
Group: Development/C
Requires: nbdkit = %EVR
AutoReq: nocpp

%description devel
%summary.

%package checkinstall
Summary: CI tests for %name
Group: Development/Other
BuildArch: noarch
Requires(post): %name = %EVR
Requires(post): %_bindir/nbdinfo

%description checkinstall
%summary.

%prep
%setup
# We have mke2fs outside of PATH and it's useful for non-root users even though
# it's in /sbin.
grep -rlZ 'mke2fs -' | xargs -rt0 sed -i 's!mke2fs -!/sbin/&!'

%build
%ifarch %ix86
# Workaround for precision problems.
%add_optflags -ffloat-store
%endif
%autoreconf
# nbdkit tool is usable for non-root user so force install into bin. Also
# installed into bin in Debian, most other distros install to sbin.
%configure \
	--disable-static \
	--sbindir=%_bindir \
	--with-bash-completions \
	--with-extra='%release%{?disttag::%disttag}' \
	--with-manpages \
	%nil
%make_build

%install
%makeinstall_std
# brp-cleanup does not reach these .la files.
find %buildroot%_libdir -name '*.la' -delete

%check
./nbdkit --version | grep -P '^%name \Q%version\E '
./nbdkit --dump-config
# Upstream tests.
%make_build check || {
	find -name test-suite.log -exec cat {} +
	exit 2
}

%post checkinstall
set -ex
nbdkit -U - memory 1G --run 'nbdinfo "$uri"'

%files
%doc LICENSE README.md
%_bindir/nbdkit
%_libdir/nbdkit
%exclude %_libdir/nbdkit/plugins/nbdkit-example*
%exclude %_libdir/nbdkit/plugins/nbdkit-cc-*
%_datadir/bash-completion/completions/nbdkit
%_man1dir/nbdkit*.1*
%exclude %_man1dir/nbdkit-release-notes-*.1*
%exclude %_man1dir/nbdkit-example*.1*
%_man3dir/nbdkit-sh-plugin*.3*

%files devel
%doc BENCHMARKING OTHER_PLUGINS SECURITY plugins/example*/example*.c
%_libdir/nbdkit/plugins/nbdkit-example*
%_libdir/nbdkit/plugins/nbdkit-cc-*
%_pkgconfigdir/nbdkit.pc
%_includedir/nbd*
%_man1dir/nbdkit-release-notes-*.1*
%_man1dir/nbdkit-example*.1*
%_man3dir/nbdkit*.3*
%exclude %_man3dir/nbdkit-sh-plugin*.3*

%files checkinstall

%changelog
* Fri May 03 2024 Vitaly Chikunov <vt@altlinux.org> 1.39.4-alt1
- Update to v1.39.4 (2024-04-20).

* Thu Mar 07 2024 Vitaly Chikunov <vt@altlinux.org> 1.37.10-alt1
- Update to v1.37.10 (2024-03-04).

* Sat Jan 20 2024 Vitaly Chikunov <vt@altlinux.org> 1.37.5-alt1
- Update to v1.37.5 (2024-01-16).

* Sun Dec 31 2023 Vitaly Chikunov <vt@altlinux.org> 1.37.4-alt1
- Update to v1.37.4 (2023-12-19).

* Mon Dec 04 2023 Vitaly Chikunov <vt@altlinux.org> 1.37.3-alt1
- Update to v1.37.3 (2023-11-26).

* Wed Nov 08 2023 Vitaly Chikunov <vt@altlinux.org> 1.37.2-alt1
- Update to v1.37.2 (2023-11-07).

* Thu Oct 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.37.1-alt1
- Update to v1.37.1 (2023-10-23).

* Tue Sep 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.35.13-alt1
- Update to v1.35.13 (2023-09-11).

* Wed Aug 23 2023 Vitaly Chikunov <vt@altlinux.org> 1.35.10-alt1
- First import v1.35.10 (2023-08-12).
