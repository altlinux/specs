Name: riscv32-none-elf-gcc
Version: 14.2.0
Release: alt2

Summary: GNU Compiler Collection
License: GPLv3+
Group: Development/C
Url: https://gcc.gnu.org/

Requires: riscv32-none-elf-newlib

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ flex zlib-devel libgmp-devel libmpc-devel autogen
BuildRequires: riscv32-none-elf-binutils >= 2.44
BuildRequires: riscv32-none-elf-newlib
BuildRequires: /usr/bin/python3

Requires: riscv32-none-elf-binutils >= 2.44
%add_python_req_skip libstdcxx gdb

%package c++
Summary: Cross Compiling GNU GCC targeted at aarch64-none-elf
Group: Development/Tools
AutoReq: yes, nopython
Requires: %name = %version-%release

%description
This package contains the GNU Compiler Collection version 14.2.0.
You'll need this package in order to compile C code.
It is also required for all other GCC compilers.

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

%define target riscv32-none-elf
%define _libexecdir /usr/libexec
%brp_strip_none %_libexecdir/%target/*
%brp_strip_none %_libexecdir/gcc/%target/*.[oa]
%add_verify_elf_skiplist %_libexecdir/%target/*
%add_verify_elf_skiplist %_libexecdir/gcc/%target/*

%prep
%setup
contrib/gcc_update --touch


%build
mkdir obj-%target; cd obj-%target

../configure \
            --prefix=%_libexecdir \
            --bindir=%_bindir \
            --libexecdir=%_libexecdir \
            --libdir=%_libexecdir \
            --mandir=%_mandir \
            --infodir=%_infodir \
            --target=%target \
            --with-python-dir=%target/share/gcc-%version/python \
            --with-pkgversion="%version-%release" \
            --with-bugurl="https://bugzilla.altlinux.org/" \
            \
            --disable-decimal-float \
            --disable-libffi \
            --disable-libgomp \
            --disable-libmudflap \
            --disable-libquadmath \
            --disable-libssp \
            --disable-libstdcxx-pch \
            --disable-nls \
            --disable-shared \
            --disable-threads \
            --disable-tls \
            \
            --enable-checking=release \
            --enable-languages=c,c++ \
            --enable-plugins \
            --with-newlib \
            --with-gnu-as \
            --with-gnu-ld \
            --enable-multilib \
            --with-abi=ilp32d \
            --with-arch=rv32gc \
            --with-multilib-generator='rv32i-ilp32--;rv32iac-ilp32--;rv32im-ilp32--;rv32imac-ilp32--;rv32imafc-ilp32--' \
            --with-gmp \
            --with-mpfr \
            --with-mpc \
            --with-headers=yes \
            --with-system-zlib \
            --with-sysroot=%_libexecdir/%target

%make_build \
CFLAGS_FOR_TARGET='-Os -mcmodel=medlow -ffunction-sections -fdata-sections' \
CXXFLAGS_FOR_TARGET='-Os -mcmodel=medlow'

%install
%makeinstall_std -C obj-%target
# we don't want these as we are a cross version
rm -r %buildroot%_infodir
rm -r %buildroot%_man7dir
rm -f %buildroot%_libdir/libcc1* ||:
rm -f %buildroot%_libexecdir/libcc1* ||:
# these directories are often empty
rmdir %buildroot%_libexecdir/%target/share/gcc-* ||:
rmdir %buildroot%_libexecdir/%target/share ||:
# and these aren't usefull for embedded targets
rm -r %buildroot%prefix/lib*/gcc/%target/*/install-tools ||:
rm -r %buildroot%_libexecdir/gcc/%target/*/install-tools ||:
find  %buildroot%_libexecdir/ -type f -name \*.la -delete

%files
%doc COPYING* README
%_bindir/%target-*
%exclude %_bindir/%target-?++
%_libexecdir/gcc/%target
%_man1dir/%target-*.1*
%exclude %_man1dir/%target-?++.1*
%exclude %_libexecdir/gcc/%target/*/cc1plus

%files c++
%_bindir/%target-?++
%_libexecdir/%target
%_man1dir/%target-g++.1*
%_libexecdir/gcc/%target/*/cc1plus

%changelog
* Wed Feb 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.2.0-alt2
- rebuilt with multilib enabled

* Wed Feb 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.2.0-alt1
- initial release
