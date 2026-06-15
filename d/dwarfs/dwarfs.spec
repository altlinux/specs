%def_disable snapshot
%define _name dwarfs
# fuse tests failed in hasher
%def_disable check

Name: %_name
Version: 0.15.3
Release: alt1.1

Summary: A fast high compression read-only file system
License: MIT
Group: System/Kernel and hardware
Url: https://github.com/mhx/dwarfs

Vcs: https://github.com/mhx/dwarfs.git

%if_disabled snapshot
Source: %url/releases/download/v%version/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake ninja-build
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(libcrypto) >= 3.0
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: librange-v3-devel
BuildRequires: parallel-hashmap-devel
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(flac++)
BuildRequires: pkgconfig(fuse3)
BuildRequires: libbrotli-devel
BuildRequires: libutf8cpp-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-context-devel
BuildRequires: boost-asio-devel
BuildRequires: libunwind-devel
%{?_enable_check:BuildRequires: libgtest-devel ctest fuse3}

%description
DwarFS
The Deduplicating Warp-speed Advanced Read-only File System.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
Development files for %name.

%package tools
Summary: DwarFS tools
Group: System/Kernel and hardware

%description tools
This package provides DWarFS tools (dwarfsck, dwarfsextract, mkdwarfs)

%package -n fuse-%name
Summary: DwarFS fuse3 driver
Group: System/Kernel and hardware
Requires: %name-tools = %EVR
Requires: fuse3

%description -n fuse-%name
This package provides DWarFS driver for FUSE3.

%prep
%setup -n %_name-%version

%build
# no way to build shared libraries
# put dwarfs.mount to /usr/bin
# put tools to /sbin
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_LIBDWARFS=ON \
    -DWITH_TOOLS=ON \
    -DWITH_FUSE_DRIVER=ON \
    -DPREFER_SYSTEM_ZSTD=ON \
    -DPREFER_SYSTEM_XXHASH=ON \
    -DPREFER_SYSTEM_LIBFMT=ON \
    -DPREFER_SYSTEM_GTEST=ON \
    -DDISABLE_MOLD=ON \
    -DCMAKE_INSTALL_SBINDIR=/bin \
    -DCMAKE_INSTALL_BINDIR=/sbin \
    %{?_enable_check:-DWITH_TESTS=ON} \
%nil
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

# fix symlink
ln -sf ../../sbin/%_name %buildroot%_bindir/mount.%_name
# https://bugzilla.altlinux.org/59541
ln -sf ../../sbin/%{_name}extract %buildroot%_bindir/%{_name}extract

%check
%ctest

%files tools
/sbin/%{_name}ck
/sbin/%{_name}extract
/sbin/mk%_name
# symlink
%_bindir/%{_name}extract
%_man1dir/*
%_man5dir/%_name-format.5*
%_man7dir/%_name-env.7*
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%doc README* CHANGES*

%files -n fuse-%name
/sbin/%_name
# symlink
%_bindir/mount.%_name
%_desktopdir/%_name-mount-handler.desktop
%_datadir/mime/packages/%_name.xml

#%files devel
%exclude %_includedir/%_name/
%exclude %_libdir/cmake/%_name/

%changelog
* Mon Jun 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.3-alt1.1
- symlinked dwarfsextract to %%_bindir (ALT #59541)

* Wed Apr 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.3-alt1
- 0.15.3

* Tue Mar 31 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Sun Mar 22 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Thu Mar 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.0-alt1
- 0.15.0

* Mon Dec 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- first build for Sisyphus



