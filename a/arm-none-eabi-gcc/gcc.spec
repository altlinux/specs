Name: arm-none-eabi-gcc
Version: 12.2.1
Release: alt1

Summary: GNU Compiler Collection
License: GPLv3+
Group: Development/C
Url: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads

Requires: arm-none-eabi-newlib

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ flex zlib-devel libgmp-devel libmpc-devel autogen
BuildRequires: arm-none-eabi-binutils >= 2.35
BuildRequires: arm-none-eabi-newlib

Requires: arm-none-eabi-binutils >= 2.35
%add_python_req_skip libstdcxx gdb

%package c++
Summary: Cross Compiling GNU GCC targeted at arm-none-eabi
Group: Development/Tools
AutoReq: yes, nopython
Requires: %name = %version-%release

%description
This package contains the GNU Compiler Collection version 12.2.1.
You'll need this package in order to compile C code.
It is also required for all other GCC compilers.

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

%define target         arm-none-eabi
%define _libexecdir /usr/libexec
%brp_strip_none %_libexecdir/*

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
            --with-multilib-list=aprofile,rmprofile \
            --with-gmp \
            --with-mpfr \
            --with-mpc \
            --with-headers=yes \
            --with-system-zlib \
            --with-sysroot=%_libexecdir/%target

%make_build

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
* Thu Feb 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.2.1-alt1
- 12.2.1

* Sat Aug 28 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt6
- brp_strip_none %_libexecdir/*

* Sun Feb 28 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt5
- Fix twice packaged files

* Sat Feb 27 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt4
- Fix unpackaged files (ALT bug 39740)

* Mon Feb 08 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt3
- relocate libstdc++ to c++ subpackage (Thanks Sergey Bolshakov)
- while at it, suppress python autoreqs on *gdb.py (Thanks Sergey Bolshakov)

* Sun Feb 07 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt2
- Rebuild with newlib 3.3.0 (without bootstrap)

* Sat Feb 06 2021 Anton Midyukov <antohami@altlinux.org> 10.2.0-alt1
- New version 10.2.0 (bootstrap build)

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 8.3.1-alt3
- Fix build with gcc10 -fno-common

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 8.3.1-alt2
- build with parallelization (Closes: 36680)

* Sun Mar 03 2019 Anton Midyukov <antohami@altlinux.org> 8.3.1-alt1
- new version 8.3.1

* Sun Feb 10 2019 Anton Midyukov <antohami@altlinux.org> 8.2.1-alt1
- new version 8.2.1

* Thu Sep 20 2018 Anton Midyukov <antohami@altlinux.org> 7.3.1-alt3
- first build for aarch64
- skip requires python(gdb)

* Thu Apr 19 2018 Anton Midyukov <antohami@altlinux.org> 7.3.1-alt2
- Rebuild with newlib 3.0.0 (without bootstrap)

* Mon Apr 16 2018 Anton Midyukov <antohami@altlinux.org> 7.3.1-alt1
- New version 7.3.1 (bootstrap build)

* Sun Jul 02 2017 Anton Midyukov <antohami@altlinux.org> 6.3.0-alt3
- Replace if_without to if_with
- Added requires arm-none-eabi-newlib.

* Sat Jul 01 2017 Anton Midyukov <antohami@altlinux.org> 6.3.0-alt2
- Rebuild with newlib (without bootstrap).

* Fri Jun 30 2017 Anton Midyukov <antohami@altlinux.org> 6.3.0-alt1
- Initial build for ALT Sisyphus.
