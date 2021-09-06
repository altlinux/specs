# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# Based on https://github.com/iovisor/bcc/blob/master/SPECS/bcc.spec

# Lua jit is not available for some architectures
%ifarch i586 x86_64 aarch64
%def_with luajit
%else
%def_without luajit
%endif

# Update How-to:
#   git merge -s ours v0.0.9
#   gear-update-tag libbpf v0.0.9
#   git commit
#   git merge v0.15.0
#   (merge) git rm src/cc/libbpf
#   (merge) git merge --continue

Name:		bcc
Version:	0.21.0
Release:	alt1
Summary:	BPF Compiler Collection (BCC)
Group:		Development/Debuggers
License:	Apache-2.0
URL:		https://www.iovisor.org/technology/bcc
Vcs:		https://github.com/iovisor/bcc.git
# Also libbpf https://github.com/libbpf/libbpf
# Which is a mirror of bpf-next linux tree's tools/lib/bpf
# directory plus its supporting header files.
# It's bundled with bcc in src/cc/libbpf

Source:		%name-%version.tar
Source1:	libbpf.tar

# bcc does not support 32-bit arches
# See https://github.com/iovisor/bcc/issues/3241
ExclusiveArch:	x86_64 aarch64 ppc64le

%define clang_version 12.0

BuildRequires(pre): python3-module-setuptools
BuildRequires(pre): rpm-macros-cmake
BuildRequires: banner
BuildRequires: bpftool
BuildRequires: cmake
BuildRequires: flex
BuildRequires: libstdc++-devel
BuildRequires: clang%clang_version-devel
BuildRequires: clang%clang_version-devel-static
BuildRequires:  llvm%clang_version-devel
BuildRequires:  llvm%clang_version-devel-static
BuildRequires:   lld%clang_version
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: libelf-devel-static
BuildRequires: zlib-devel
BuildRequires: libncurses-devel
%if_with luajit
BuildRequires: luajit
BuildRequires: libluajit-devel
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
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm kernel-headers-un-def kernel-headers-modules-un-def}}

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

%if_with luajit
%global lua_include `pkg-config --variable=includedir luajit`
%global lua_libs `pkg-config --variable=libdir luajit`/lib`pkg-config --variable=libname luajit`.so
%global lua_config -DLUAJIT_INCLUDE_DIR=%lua_include -DLUAJIT_LIBRARIES=%lua_libs
%endif

%prep
%setup -q
tar -xf %SOURCE1 -C src/cc/libbpf

%build
%define optflags_lto -flto=thin

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
export CC=clang
export CXX=clang++
# ld cannot link libLLVM and libclang in ALT: https://bugzilla.altlinux.org/34801
export LDFLAGS="-fuse-ld=lld -Wl,--as-needed $LDFLAGS -lLLVM -lclang-cpp -lelf"
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DREVISION_LAST=%version \
	-DREVISION=%version \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DUSINGISYSTEM:BOOL=no \
	-DPYTHON_CMD=python3 \
	%{?lua_config}
%cmake_build

%ifarch x86_64
%make_build -C libbpf-tools BPFTOOL=/usr/sbin/bpftool
%endif

%install
%set_verify_elf_method relaxed
pathfix.py -pni %__python3 tools

%cmake_install

# Cannot make noarch package because bcc exists not on all arches
install -d %buildroot/%python3_sitelibdir
rmdir %buildroot/%python3_sitelibdir
mv %buildroot/%python3_sitelibdir_noarch %buildroot/%python3_sitelibdir

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

%ifarch x86_64
cd libbpf-tools
make -p | sed -n /^APPS/s/APPS.=//p | tr ' ' '\n' \
	| xargs -i install -v -Dp {} %buildroot%_sbindir/bpf-{}
%endif

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

%files -n libbcc
%doc LICENSE.txt
%_libdir/lib*.so.*

%files -n libbcc-devel
%doc FAQ.txt LINKS.md README.md
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_includedir/bcc

%files -n libbcc-devel-static
%_libdir/lib*.a

%files -n python3-module-bcc
%python3_sitelibdir/bcc*

%if_with luajit
%files -n bcc-lua
%_bindir/bcc-lua
%endif

%files -n bcc-tools
%_bindir/bps
%_datadir/bcc
%_man8dir/*

%ifarch x86_64
%files -n libbpf-tools
%_sbindir/bpf-*
%endif

%changelog
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

