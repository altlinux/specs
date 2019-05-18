# based on https://github.com/iovisor/bcc/blob/master/SPECS/bcc.spec

#lua jit not available for some architectures
%ifarch i586 x86_64 aarch64
%def_with luajit
%else
%def_without luajit
%endif

Name:		bcc
Version:	0.9.0.0.55.ge86e0643
Release:	alt2
Summary:	BPF Compiler Collection (BCC)
Group:		Development/Debuggers
License:	ASL 2.0
URL:		https://github.com/iovisor/bcc
# Also libbpf https://github.com/libbpf/libbpf
# Which is a mirror of bpf-next linux tree's tools/lib/bpf
# directory plus its supporting header files.
# It's bundled with bcc in src/cc/libbpf

Source:		%name-%version.tar
Source1:	libbpf.tar

ExclusiveArch:	x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): python3-module-setuptools
BuildRequires:	bison
BuildRequires:	cmake >= 2.8.7
BuildRequires:	flex
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	clang-devel >= 3.7.0
BuildRequires:	llvm-devel >= 3.7.0
BuildRequires:	lld
BuildRequires:	llvm-devel-static
BuildRequires:	clang-devel-static
BuildRequires:	python3-devel
BuildRequires:	libelf-devel-static
BuildRequires:	zlib-devel
BuildRequires:	libncurses-devel
%if_with luajit
BuildRequires:	luajit
BuildRequires:	libluajit-devel
%endif
BuildRequires:	/proc

%description
BCC is a toolkit for creating efficient kernel tracing and manipulation
programs, and includes several useful tools and examples. It makes use of
extended BPF (Berkeley Packet Filters), formally known as eBPF, a new feature
that was first added to Linux 3.15. Much of what BCC uses requires Linux 4.1
and above.

BCC makes BPF programs easier to write, with kernel instrumentation in C (and
includes a C wrapper around LLVM), and front-ends in Python and lua. It is
suited for many tasks, including performance analysis and network traffic
control.

%if_with luajit
%global lua_include `pkg-config --variable=includedir luajit`
%global lua_libs `pkg-config --variable=libdir luajit`/lib`pkg-config --variable=libname luajit`.so
%global lua_config -DLUAJIT_INCLUDE_DIR=%{lua_include} -DLUAJIT_LIBRARIES=%{lua_libs}
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
# ld can not link libLLVM and libclang in ALT
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
%cmake_install install/strip DESTDIR=%buildroot
install -d %buildroot/%python3_sitelibdir
rmdir %buildroot/%python3_sitelibdir
mv %buildroot/%python3_sitelibdir_noarch %buildroot/%python3_sitelibdir
# mangle shebangs
find %{buildroot}/usr/share/bcc/tools -type f | xargs \
    sed -i -e '1 s|^#!/usr/bin/python$|#!'%__python3'|' \
           -e '1 s|^#!/usr/bin/env python$|#!'%__python3'|'
install -d %buildroot%_man8dir
rmdir %buildroot%_man8dir
mv %buildroot/usr/share/bcc/man/man8 %buildroot%_man8dir
pushd %{buildroot}%{_man8dir}
rename '' bcc- *.gz
popd

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
%_datadir/bcc/tools/
%_man8dir/*

%changelog
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

