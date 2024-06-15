# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=normal

Name:    crash
Version: 8.0.5
Release: alt2
Summary: Linux kernel crash utility
Group:   Development/Debuggers
License: GPL-3.0-only
Url:     https://crash-utility.github.io/
Vcs:     https://github.com/crash-utility/crash
# Docs:  https://crash-utility.github.io/crash_whitepaper.html
# Mailing list: https://www.redhat.com/archives/crash-utility/
# Extensions Url: https://crash-utility.github.io/extensions.html
# Extensions Vcs: https://github.com/crash-utility/crash-extensions.git

# Crash calls a lot of tools.
# Non essential requires: bzip2 file findutils gzip less xz
Requires: binutils

Source0: %name-%version.tar
Source1: gdb-10.2.tar.gz

ExcludeArch: e2k
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: makeinfo
BuildRequires: ncurses-devel
BuildRequires: zlib-devel

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump
creation facilities.

Whitepaper: https://crash-utility.github.io/crash_whitepaper.html

Note: You will need -debuginfo package for the current kernel installed
      for this tool to work!

%package -n kernel-ci-crash-debuginfo
Summary: CI test for %name
Group: Development/Other
Requires(post): crash = %EVR
Requires(post): kernel-image-un-def-debuginfo
Requires(post): rpm-build-vm

%description -n kernel-ci-crash-debuginfo
%summary with a workaround for 'sisyphus_check: check-deps ERROR: package
dependencies violation' for a kernel-image.

%prep
%setup
install -m644 %SOURCE1 .
mv crash-extensions/*.c extensions/
tar xvf crash-extensions/crash-gcore-command-1.6.1.tar.gz -C extensions --strip-components=1
tar xvf crash-extensions/ptdump-1.0.7.tar.gz -C extensions --strip-components=1

%build
%add_optflags $(getconf LFS_CFLAGS)
%make_build RPMPKG=%version-%release CFLAGS="%optflags" CXXFLAGS="%optflags" V=1
# Build what builds. Does not support -j.
%make -ki extensions

%install
%makeinstall_std
install -Dp -m0644 crash.8 %buildroot%_man8dir/crash.8
install -Dp -m0644 defs.h  %buildroot%_includedir/crash/defs.h
mkdir -p %buildroot%_libdir/crash/extensions
install -p -m0644 extensions/*.so %buildroot%_libdir/crash/extensions

%ifnarch armh
# armh: crash: cannot find a live memory device
#       due to no PROC_KCORE support on arm.
%post -n kernel-ci-crash-debuginfo
set -exu
%ifarch %ix86
KVER=$(cd /lib/modules; ls | head -1)
echo -e "6.6\n$KVER" | sort -CV || {
	# WARNING: could not find MAGIC_START!
	# WARNING: cannot read linux_banner string
	echo >&2 "Linux $KVER is too old for %_arch (skipping test)."
	exit 0
}
%endif
vm-run --kvm=only --heredoc <<-EOF1
	crash <<EOF2 |& tee crash.log
	ps
	exit
	EOF2
EOF1
grep 'KERNEL: /usr/lib/debug/.*lib/modules/.*/vmlinux' crash.log
grep 'DUMPFILE: /proc/kcore' crash.log
grep -F '[swapper/0]' crash.log
%endif

%files
%doc README COPYING3
%_bindir/crash
%_includedir/crash
%_man8dir/crash.8*
%_libdir/crash

%files -n kernel-ci-crash-debuginfo

%changelog
* Fri Jun 14 2024 Vitaly Chikunov <vt@altlinux.org> 8.0.5-alt2
- Fix FTBFS in p10.
- spec: Add CI package with a smoke test.

* Thu Apr 25 2024 Vitaly Chikunov <vt@altlinux.org> 8.0.5-alt1
- Update to 8.0.5 (2024-04-23).

* Thu Nov 16 2023 Vitaly Chikunov <vt@altlinux.org> 8.0.4-alt1
- Update to 8.0.4 (2023-11-16).

* Wed Apr 26 2023 Vitaly Chikunov <vt@altlinux.org> 8.0.3-alt1
- Update to 8.0.3 (2023-04-26).

* Sat Nov 19 2022 Vitaly Chikunov <vt@altlinux.org> 8.0.2-alt1
- Update to 8.0.2 (2022-11-16).

* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 8.0.1-alt1
- Update to 8.0.1 (2022-04-26).

* Mon Dec 20 2021 Vitaly Chikunov <vt@altlinux.org> 8.0.0-alt1
- Updated to 8.0.0-4-g6968345893 (2021-12-08) which is based on gdb-10.2
  with DWARF 5 support.
- Fixed lfs=strict build on 32-bit systems.

* Wed May 12 2021 Vitaly Chikunov <vt@altlinux.org> 7.3.0-alt1
- Update to 7.3.0 (2021-04-27).

* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.9-alt2
- Add usage note to %%description.

* Wed Nov 25 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.9-alt1
- Update to 7.2.9 (2020-11-20).

* Sun Jul 12 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt3
- spec: ExcludeArch: e2k

* Wed Jul 08 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt2
- Add crash-extensions 80b218f.

* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt1
- First import of 7.2.8-21-gc4862e1.
