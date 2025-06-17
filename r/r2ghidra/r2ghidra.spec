%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: r2ghidra
Version: 5.9.8
Release: alt1
Summary: Ghidra decompiler integration for radare2
License: LGPL-3.0-only
Group: Development/Tools
Url: https://www.radare.org/n/

VCS: https://github.com/radareorg/r2ghidra.git
Source0: %name-%version.tar
Source1: %name-%version-ghidra-native.tar
Patch0: r2ghidra-5.9.8-alt-fix-build-return.patch
Patch1: r2ghidra-5.9.8-alt-not-require-git.patch
Patch2: r2ghidra-5.9.8-alt-use-system-pugixml.patch

BuildRequires: gcc-c++
BuildRequires: libpugixml-devel
BuildRequires: radare2-devel
BuildRequires: zlib-devel

%description
This is an integration of the Ghidra decompiler for radare2.  It is solely
based on the decompiler part of Ghidra, which is written entirely in C++, so
Ghidra itself is not required at all and the plugin can be built
self-contained.

%prep
%setup -a1
%autopatch -p1
%make -C ghidra-native patch
sed '/^.*path = .*r2ghidra_sleigh"/ s/lib/%_lib/' -i src/SleighAsm.cpp

%build
%ifarch %ix86
%add_optflags -D_FILE_OFFSET_BITS=64
%endif
%configure
%make_build

%install
%makeinstall_std

%files
%dir %_libdir/radare2/%version/r2ghidra_sleigh
%_bindir/sleighc
%_libdir/radare2/%version/core_ghidra.so
%_libdir/radare2/%version/r2ghidra_sleigh/*

%changelog
* Tue Jun 17 2025 Constantin Sunzow <protvin@altlinux.org> 5.9.8-alt1
- Initial build.
