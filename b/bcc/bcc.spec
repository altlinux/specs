# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

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
Version:	0.15.0
Release:	alt1
Summary:	BPF Compiler Collection (BCC)
Group:		Development/Debuggers
License:	Apache-2.0
URL:		https://github.com/iovisor/bcc
Vcs:		https://github.com/iovisor/bcc.git
# Also libbpf https://github.com/libbpf/libbpf
# Which is a mirror of bpf-next linux tree's tools/lib/bpf
# directory plus its supporting header files.
# It's bundled with bcc in src/cc/libbpf

Source:		%name-%version.tar
Source1:	libbpf.tar

ExclusiveArch:	x86_64 aarch64 ppc64le

# Note: clang-10.0 have tests failed:
#  # /usr/src/tmp/bcc-buildroot/usr/share/bcc/tools/cpudist 1 1
#  Traceback (most recent call last):
#    File "/usr/src/tmp/bcc-buildroot/usr/share/bcc/tools/cpudist", line 15, in <module>
#      from bcc import BPF
#    File "/usr/src/tmp/bcc-buildroot/usr/lib64/python3/site-packages/bcc/__init__.py", line 26, in <module>
#      from .libbcc import lib, bcc_symbol, bcc_symbol_option, bcc_stacktrace_build_id, _SYM_CB_TYPE
#    File "/usr/src/tmp/bcc-buildroot/usr/lib64/python3/site-packages/bcc/libbcc.py", line 17, in <module>
#      lib = ct.CDLL("libbcc.so.0", use_errno=True)
#    File "/usr/lib64/python3.8/ctypes/__init__.py", line 373, in __init__
#      self._handle = _dlopen(self._name, mode)
#  OSError: /usr/src/tmp/bcc-buildroot/usr/lib64/libbcc.so.0: undefined symbol: _ZN4llvm19RTDyldMemoryManager16registerEHFramesEPhmm

%define clang_version 9.0

BuildRequires(pre): python3-module-setuptools
BuildRequires(pre): rpm-macros-cmake
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
Requires:	libbcc = %version-%release
AutoReq:	nocpp
%description -n libbcc-devel
Includes and pkg-config for developing BCC programs

%package -n python3-module-bcc
Summary:	Python bindings for BPF Compiler Collection (BCC)
Group:		Development/Python
Requires:	libbcc = %version-%release
%description -n python3-module-bcc
Python bindings for BPF Compiler Collection (BCC)

%package -n bcc-lua
Summary:	Standalone tool to run BCC tracers written in Lua
Group:		Development/Other
Requires:	libbcc = %version-%release
%description -n bcc-lua
Standalone tool to run BCC tracers written in Lua

%package -n bcc-tools
Summary:	Command line tools for BPF Compiler Collection (BCC)
Group:		Development/Debuggers
Requires:	python3-module-bcc = %version-%release
%description -n bcc-tools
Command line tools for BPF Compiler Collection (BCC)

%if_with luajit
%global lua_include `pkg-config --variable=includedir luajit`
%global lua_libs `pkg-config --variable=libdir luajit`/lib`pkg-config --variable=libname luajit`.so
%global lua_config -DLUAJIT_INCLUDE_DIR=%lua_include -DLUAJIT_LIBRARIES=%lua_libs
%endif

%prep
%setup -q
mkdir src/cc/libbpf
tar -xf %SOURCE1 -C src/cc/libbpf

%build
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
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DREVISION_LAST=%version \
	-DREVISION=%version \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DUSINGISYSTEM:BOOL=no \
	-DPYTHON_CMD=python3 \
	%{?lua_config}
%cmake_build

%install
%set_verify_elf_method relaxed
pathfix.py -pni %__python3 tools

%cmake_install install/strip DESTDIR=%buildroot

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

%check
# Simple smoke test, only if KVM is enabled
# (Will fail on ppc64le w/o KVM).
if [ -w /dev/kvm ]; then
	LD_LIBRARY_PATH=%buildroot%_libdir \
	PYTHONPATH=%buildroot%python3_sitelibdir \
	vm-run %buildroot%_datadir/bcc/tools/cpudist 1 1
fi

%files -n libbcc
%doc LICENSE.txt
%_libdir/lib*

%files -n libbcc-devel
%doc FAQ.txt LINKS.md README.md
%_libdir/pkgconfig/*.pc
%_includedir/bcc/

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

%changelog
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

