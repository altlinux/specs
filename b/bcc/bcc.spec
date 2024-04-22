# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%ifarch loongarch64
%def_without check
%else
%def_with check
%endif

# Based on https://github.com/iovisor/bcc/blob/master/SPECS/bcc.spec

# Lua jit is not available for some architectures
%ifarch i586 x86_64 aarch64 loongarch64
%def_with luajit
%else
%def_without luajit
%endif

Name:		bcc
Version: 0.30.0
Release: alt1
Summary:	BPF Compiler Collection (BCC)
Group:		Development/Debuggers
License:	Apache-2.0
Url:		https://github.com/iovisor/bcc

Source:		%name-%version.tar
Source1: libbpf-0.tar
Source2: bpftool-0.tar
Source3: libbpf-1.tar
Source4: blazesym-0.tar

# bcc does not support 32-bit arches
# See https://github.com/iovisor/bcc/issues/3241
ExclusiveArch: x86_64 aarch64 ppc64le loongarch64

BuildRequires(pre): python3-module-setuptools
BuildRequires(pre): rpm-macros-cmake
BuildRequires: banner
BuildRequires: bpftool
BuildRequires: clang-devel
BuildRequires: clang-devel-static
BuildRequires: cmake
BuildRequires: flex
BuildRequires: libdebuginfod-devel
BuildRequires: libelf-devel-static
BuildRequires: liblzma-devel
BuildRequires: libmlir-devel
BuildRequires: libncurses-devel
BuildRequires: libpolly-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
%ifnarch loongarch64
BuildRequires: lld
%endif
BuildRequires: llvm-devel
BuildRequires: llvm-devel-static
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: zlib-devel
%if_with luajit
BuildRequires: libluajit-devel
BuildRequires: luajit
%endif
# Prevent copying into repos with too old pahole.
BuildRequires: dwarves >= 1.16

# Adding `BuildRequires: /proc' improves lld speed:
#    USER     %%CPU  %%MEM  COMMAND
#    builder   1601  4,436  ld.lld
# vs:
#    builder  100,1  0,942  ld.lld
BuildRequires: /proc

# Assuming 'kernel' dependency will bring un-def kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires: kernel-headers-modules-un-def
BuildRequires: kernel-headers-un-def
BuildRequires: rpm-build-vm
}}

%description
BCC is a toolkit for creating efficient kernel tracing and manipulation
programs, and includes several useful tools and examples. It makes use of
extended BPF (Berkeley Packet Filters), formally known as eBPF, a new feature
that was first added to Linux 3.15. Much of what BCC uses requires Linux 4.1
and above.

BCC makes BPF programs easier to write, with kernel instrumentation in C (and
includes a C wrapper around LLVM), and front-ends in Python and Lua. It is
suited for many tasks, including performance analysis and network traffic
control.

%package -n libbcc
Summary:	Shared Library for BPF Compiler Collection (BCC)
Group:		System/Libraries
Requires:	libelf
%description -n libbcc
Shared Library for BPF Compiler Collection (BCC)

%package -n libbcc-devel
Summary:	BPF Compiler Collection (BCC) (devel package)
Group:		Development/C
Requires:	libbcc = %EVR
AutoReq:	nocpp
%description -n libbcc-devel
Includes and pkg-config for developing BCC programs

%package -n libbcc-devel-static
Summary:	BPF Compiler Collection (BCC) (static libs)
Group:		Development/C
Requires:	libbcc-devel = %EVR
AutoReq:	nocpp
%description -n libbcc-devel-static
Static libraries for developing BCC programs

%package -n python3-module-bcc
Summary:	Python bindings for BPF Compiler Collection (BCC)
Group:		Development/Python
Requires:	libbcc = %EVR
%description -n python3-module-bcc
Python bindings for BPF Compiler Collection (BCC)

%package -n bcc-lua
Summary:	Standalone tool to run BCC tracers written in Lua
Group:		Development/Other
Requires:	libbcc = %EVR
%description -n bcc-lua
Standalone tool to run BCC tracers written in Lua

%package -n bcc-tools
Summary:	Command line tools for BPF Compiler Collection (BCC)
Group:		Development/Debuggers
Requires:	python3-module-bcc = %EVR
%description -n bcc-tools
Command line tools for BPF Compiler Collection (BCC)

%package -n libbpf-tools
Summary:	Compile-once run-everywhere (CO-RE) libbpf based tools
Group:		Development/Debuggers
Url:		https://github.com/iovisor/bcc/tree/master/libbpf-tools
# PR: http://www.brendangregg.com/blog/2020-11-04/bpf-co-re-btf-libbpf.html
# PR: https://nakryiko.com/posts/libbpf-bootstrap/
Requires:	python3-module-bcc = %EVR
%description -n libbpf-tools
Compile-once run-everywhere (CO-RE) libbpf based tools.
These tools are experimental! All the tools prefixed with 'bpf-'.
Kernel should be compiled with 'CONFIG_DEBUG_INFO_BTF=y'.

Installing of libbpf is not required due to it being statically
linked (and built in bcc package).

%package checkinstall
Summary: CI test for %name
Group: Development/Other
Requires(post): bcc-tools = %EVR
Requires(post): libbpf-tools = %EVR
Requires(post): rpm-build-vm

%description checkinstall
%summary.

%if_with luajit
%global lua_include `pkg-config --variable=includedir luajit`
%global lua_libs `pkg-config --variable=libdir luajit`/lib`pkg-config --variable=libname luajit`.so
%global lua_config -DLUAJIT_INCLUDE_DIR=%lua_include -DLUAJIT_LIBRARIES=%lua_libs
%endif

%prep
%setup -q
tar xf %SOURCE1 -C libbpf-tools/bpftool
tar xf %SOURCE2 -C libbpf-tools
tar xf %SOURCE3 -C src/cc
tar xf %SOURCE4 -C libbpf-tools

# Poor man's pathfix.py
grep -lrZx -e '#!/usr/bin/env python3\?' -e '#!/usr/bin/python' tools \
	| xargs -0 sed -i '1s,#!.*,#!%__python3,'

%build
%define optflags_lto %nil

%if_without luajit
subst '/add_subdirectory(lua)/d' examples/CMakeLists.txt
%endif
# fix bps install path
subst 's,share/bcc/introspection,bin,' introspection/CMakeLists.txt
# tests are for aarch64, powerpc64, and x86_64 only,
# but we don't run tests anyway (require root)
subst '/add_subdirectory(tests)/d' CMakeLists.txt
# do not build examples to speed things up
subst '/add_subdirectory(examples)/d' CMakeLists.txt

%remove_optflags -frecord-gcc-switches
%add_optflags -fdebug-default-version=4
export CC=clang
export CXX=clang++
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DREVISION_LAST=%version \
	-DREVISION=%version \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DUSINGISYSTEM:BOOL=no \
	-DPYTHON_CMD=python3 \
	-DENABLE_LLVM_SHARED=ON \
	%{?lua_config}
%cmake_build

# LIBBPF_OBJ expects libbpf.a, but...
%make_build -C libbpf-tools BPFTOOL=/usr/sbin/bpftool V=1

%install
%cmake_install

# Cannot make noarch package because bcc exists not on all arches
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot/%python3_sitelibdir
rmdir %buildroot/%python3_sitelibdir
mv %buildroot/%python3_sitelibdir_noarch %buildroot/%python3_sitelibdir
%endif

# Fix man pages
install -d %buildroot%_man8dir
rmdir %buildroot%_man8dir
mv %buildroot/usr/share/bcc/man/man8 %buildroot%_man8dir
pushd %buildroot%_man8dir
rename '' bcc- *.gz
popd
rm -rf %buildroot/usr/share/bcc/man

# Lib with unknown purpose.
rm -rf %buildroot%_bindir/libbcc-loader-static.a

pushd libbpf-tools
make --no-print-directory -qs --eval 'print-%%:; $(info $($*))' print-APPS \
	| xargs -n1 \
	| xargs -i install -v -Dp {} %buildroot%_sbindir/bpf-{}
popd

install -Dp .gear/bcc.sh %buildroot%_sbindir/bcc
install -Dp .gear/bcc.bash_completion %buildroot%_datadir/bash-completion/completions/bcc
ln -rs %buildroot%_datadir/bcc/tools/tplist %buildroot%_bindir
ln -s bcc-tplist.8 %buildroot%_man8dir/tplist.8

%check
banner test
# Simple smoke test, only if KVM is enabled
# (Will fail on ppc64le w/o KVM).
if [ -w /dev/kvm ]; then
	LD_LIBRARY_PATH=%buildroot%_libdir \
	PYTHONPATH=%buildroot%python3_sitelibdir \
	vm-run %buildroot%_datadir/bcc/tools/cpudist 1 1
fi

%post -n libbpf-tools
kver=$(uname -r)
if ! grep -qs CONFIG_DEBUG_INFO_BTF=y /boot/config-$kver; then
	echo >&2 "Your running kernel ($kver) does not have 'CONFIG_DEBUG_INFO_BTF=y'"
	echo >&2 "option enabled, because of this libbpf-tools will not work."
fi

%post checkinstall
set -xeo pipefail
vm-run bcc cpudist 1 1
if grep CONFIG_DEBUG_INFO_BTF=y /boot/config-*; then
	vm-run bpf-cpudist 1 1
fi
rm -f /tmp/vm.* /tmp/initramfs-*.img

%files -n libbcc
%doc LICENSE.txt
%_libdir/lib*.so.*

%files -n libbcc-devel
%doc CODEOWNERS CONTRIBUTING-SCRIPTS.md
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_includedir/bcc

%files -n libbcc-devel-static
%_libdir/lib*.a

%files -n python3-module-bcc
%python3_sitelibdir/bcc*

%if_with luajit
%files -n bcc-lua
%doc src/lua/README.md
%_bindir/bcc-lua
%endif

%files -n bcc-tools
%doc FAQ.txt LINKS.md README.md docs/*
%_bindir/bps
%_bindir/tplist
%_sbindir/bcc
%_datadir/bcc
%_datadir/bash-completion/completions/bcc
%_man8dir/*

%files -n libbpf-tools
%doc libbpf-tools/README.md
%_sbindir/bpf-*

%files checkinstall

%changelog
* Sun Apr 21 2024 Vitaly Chikunov <vt@altlinux.org> 0.30.0-alt1
- Update to v0.30.0 (2024-03-24).

* Mon Mar 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.29.1-alt3
- NMU: spec: adjusted for LoongArch:
  + do NOT use lld (as of llvm 17 lld is incompatible with the GNU ld one).
  + disable tests for now (KVM is not reliable enough yet here).

* Sat Mar 02 2024 Vitaly Chikunov <vt@altlinux.org> 0.29.1-alt2
- Fix FTBFS after removal of pathfix.py on python3 update.

* Thu Jan 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.29.1-alt1
- Update to v0.29.1 (2023-12-08).

* Thu Sep 14 2023 Artyom Bystrov <arbars@altlinux.org> 0.28.0-alt2
- Fix FTBFS

* Sun Aug 27 2023 Vitaly Chikunov <vt@altlinux.org> 0.28.0-alt1
- Update to v0.28.0 (2023-06-28).
- spec: Add checkinstall package with tests.
- spec: Build libbpf-tools on all supported architectures.

* Sun Oct 09 2022 Vitaly Chikunov <vt@altlinux.org> 0.25.0-alt1
- Update to v0.25.0 (2022-08-10).

* Sat Oct 08 2022 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt2
- Revert to use built-in libbpf (submodule).
- Build with libdebuginfod.
- Add bcc tools launcher.

* Sat May 28 2022 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt1
- Update to v0.24.0 (2022-01-14).
- Replace built-in with system libbpf package.
- Disable LTO to fix static libs.

* Sat Nov 13 2021 Vitaly Chikunov <vt@altlinux.org> 0.22.0-alt1
- Update to v0.22.0 (2021-09-15).

* Mon Sep 06 2021 Vitaly Chikunov <vt@altlinux.org> 0.21.0-alt1
- Update to v0.21.0 (2021-07-18).
- spec: Fix build with LTO.

* Sun May 30 2021 Arseny Maslennikov <arseny@altlinux.org> 0.19.0-alt1.1
- NMU: spec: migrate to new cmake macros.

* Tue Apr 27 2021 Vitaly Chikunov <vt@altlinux.org> 0.19.0-alt1
- Update to v0.19.0 (2021-03-19).
- Build using clang/llvm 12.

* Fri Jan 29 2021 Vitaly Chikunov <vt@altlinux.org> 0.18.0-alt2
- spec: Build libbpf-tools (CO-RE eBPF tools) on x86_64.

* Fri Jan 29 2021 Vitaly Chikunov <vt@altlinux.org> 0.18.0-alt1
- Update to bcc v0.18.0 (2021-01-04), libbpf v0.3 (2021-01-02).

* Fri Dec 25 2020 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to v0.17.0 (2020-10-29).

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt3
- Spin off -static package and fix wrongly packaged .a libs.
- Do not package libbcc-loader-static.a.

* Mon Aug 24 2020 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt2
- Update to bcc v0.16.0 (2020-08-22), libbpf v0.1.0 (2020-08-18).
- spec: Fix debuginfo packages.

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt2
- Rebuild on clang10.

* Thu Jul 02 2020 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- Update to bcc 0.15.0, libbpf 0.0.9.

* Wed Apr 29 2020 Vitaly Chikunov <vt@altlinux.org> 0.14.0-alt1
- Update to bcc 0.14.0, libbpf 0.0.8.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.13.0-alt3
- spec: Rework BuildRequires.

* Tue Feb 25 2020 Vitaly Chikunov <vt@altlinux.org> 0.13.0-alt2
- Add ppc64le build.

* Mon Feb 24 2020 Vitaly Chikunov <vt@altlinux.org> 0.13.0-alt1
- Update bcc to 0.13.0 with libbpf 0.0.7.

* Sun Feb 23 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.55.ge86e0643-alt3
- Fix Beekeeper build. Update License tag.

* Sat May 18 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.55.ge86e0643-alt2
- Fix man pages collide with postfix and perf-tools (closes: #36761)

* Fri May 17 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.55.ge86e0643-alt1
- Update to bcc to v0.9.0-55-ge86e0643
- Update libbpf to 5188b0ca

* Wed Jan 09 2019 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt1
- Update to 0.7.0.

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 0.5.0-alt1.458
- First build of bcc for ALT.

* Mon Nov 21 2016 William Cohen <wcohen@redhat.com> - 0.2.0-1
- Revise bcc.spec to address rpmlint issues and build properly in Fedora koji.

* Mon Apr 04 2016 Vicent Marti <vicent@github.com> - 0.1.4-1
- Add bcc-lua package

* Sun Nov 29 2015 Brenden Blanco <bblanco@plumgrid.com> - 0.1.3-1
- Add bcc-tools package

* Mon Oct 12 2015 Brenden Blanco <bblanco@plumgrid.com> - 0.1.2-1
- Add better version numbering into libbcc.so

* Fri Jul 03 2015 Brenden Blanco <bblanco@plumgrid.com> - 0.1.1-2
- Initial RPM Release

