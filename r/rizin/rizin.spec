%define _unpackaged_files_terminate_build 1

Name: rizin
Version: 0.7.4
Release: alt1

Summary: UNIX-like reverse engineering framework and command-line tool-set
License: LGPL-3.0-or-later
Group: Development/Other
Url: https://rizin.re
VCS: https://github.com/rizinorg/rizin

# Source-url: https://github.com/rizinorg/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Patch1: alt-use-sys-blake3.patch
Patch2: alt-fix-segm-fault.patch

BuildRequires(pre): meson
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(capstone)
BuildRequires: pkgconfig(tree-sitter)
BuildRequires: pkgconfig(libblake3)
BuildRequires: libmspack-devel
BuildRequires: libzstd-devel

Requires: %name-common = %EVR

%description
Rizin is a free and open-source Reverse Engineering framework,
providing a complete binary analysis experience with features like
Disassembler, Hexadecimal editor, Emulation, Binary inspection,
Debugger, and more.

Rizin is a fork of radare2 with a focus on usability, working features
and code cleanliness.

%package devel
Summary: Development files for the rizin package
Group: Development/Tools
Requires: %name = %EVR
Requires: libssl-devel
Requires: libmagic-devel

%description devel
Development files for the rizin package. See rizin package for more
information.

%package common
Summary: Arch-independent SDB files for the rizin package
Group: Development/Tools
BuildArch: noarch
Requires: %name = %EVR

%description common
Arch-independent SDB files used by rizin package. See rizin package for
more information

%prep
%setup -a1
%__cp -rf dependencies/* subprojects
%patch1 -p1
%patch2 -p1

%build
%meson \
    -Duse_sys_capstone=enabled \
    -Duse_sys_libzip=enabled \
    -Duse_sys_zlib=enabled \
    -Duse_sys_lz4=enabled \
    -Duse_sys_libzstd=enabled \
    -Duse_sys_xxhash=enabled \
    -Duse_sys_openssl=enabled \
    -Duse_sys_libmspack=enabled \
    -Duse_sys_pcre2=enabled \
    -Duse_sys_tree_sitter=enabled \
    -Duse_sys_lzma=enabled \
    -Duse_sys_blake3=enabled \
    -Denable_tests=false \
    -Denable_rz_test=false
%meson_build

%install
%meson_install

%files
%doc COPYING COPYING.LESSER DEVELOPERS.md README.md SECURITY.md BUILDING.md
%_bindir/r*
%_libdir/librz_*.so.*
%_man1dir/%name.1.*
%_man1dir/rz*.1.*
%_man7dir/rz-esil.7.*

%files devel
%_includedir/librz
%_libdir/librz*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/**/*.cmake
%dir %_libdir/cmake
%dir %_libdir/cmake/**

%files common
%_datadir/%name/asm
%_datadir/%name/cons
%_datadir/%name/flag
%_datadir/%name/format
%_datadir/%name/fortunes
%_datadir/%name/hud
%_datadir/%name/magic
%_datadir/%name/opcodes
%_datadir/%name/reg
%_datadir/%name/syscall
%_datadir/%name/types
%dir %_datadir/%name

%changelog
* Fri Feb 14 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 0.7.4-alt1
- 0.7.4-alt1
- fixed the package description (closes: 52734)
- fixed sigmentation fault (closes: 52725)
- fixed warnings when using "rizin" with "-nqcpm" parameters (closes: 52733)

* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.7.2-alt1
- Initial build for ALT Linux
