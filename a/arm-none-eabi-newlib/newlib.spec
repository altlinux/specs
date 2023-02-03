Name: arm-none-eabi-newlib
Version: 4.3.0
Release: alt1

Summary: C library intended for use on embedded systems
License: BSD and MIT and LGPLv2+ and ISC
Group: Development/Tools
Url: https://sourceware.org/newlib/

Source:  %name-%version-%release.tar

BuildArch: noarch
BuildRequires: arm-none-eabi-binutils arm-none-eabi-gcc
BuildRequires: makeinfo

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%define target arm-none-eabi
%define _libexecdir /usr/libexec

%prep
%setup

%build
mkdir obj; pushd obj
export CFLAGS="-g -O2 -ffunction-sections -fdata-sections"
../configure \
    --prefix=%_libexecdir \
    --libdir=%_libexecdir \
    --mandir=%_mandir \
    --target=%target \
    --disable-nls \
    --disable-newlib-supplied-syscalls \
    --enable-newlib-io-long-long \
    --enable-newlib-io-c99-formats \
    --enable-newlib-mb \
    --enable-newlib-reent-check-verify \
    --enable-newlib-register-fini \
    --enable-newlib-retargetable-locking

%make_build
popd

mkdir nano; pushd nano
export CFLAGS="-g -Os -ffunction-sections -fdata-sections"
../configure \
    --prefix=%_libexecdir \
    --libdir=%_libexecdir \
    --mandir=%_mandir \
    --target=%target \
    --disable-nls \
    --disable-newlib-fseek-optimization \
    --disable-newlib-fvwrite-in-streamio \
    --disable-newlib-unbuf-stream-opt \
    --disable-newlib-wide-orient \
    --disable-newlib-supplied-syscalls \
    --enable-lite-exit \
    --enable-newlib-global-atexit \
    --enable-newlib-nano-formatted-io \
    --enable-newlib-nano-malloc \
    --enable-newlib-reent-check-verify \
    --enable-newlib-reent-small \
    --enable-newlib-retargetable-locking

%make_build
popd

%install
%makeinstall_std -C obj

NANO_ROOT=%buildroot/nano
make install DESTDIR=$NANO_ROOT -C nano
for i in $(find $NANO_ROOT -regex ".*/lib\(c\|g\|rdimon\)\.a"); do
    file=$(basename $i | sed "s|\.a|_nano\.a|")
    target_path=$(dirname $i | sed "s|$NANO_ROOT||")
    mv $i "%buildroot$target_path/$file"
done
rm -rf $NANO_ROOT

# we don't want these as we are a cross version
rm -rf %buildroot%_infodir

%add_verify_elf_skiplist %_libexecdir/%target/lib/*
%brp_strip_none %_libexecdir/%target/lib/*

%files
%doc COPYING*
%dir %_libexecdir/%target
%dir %_libexecdir/%target/include/
%_libexecdir/%target/include/*
%dir %_libexecdir/%target/lib
%_libexecdir/%target/lib/*

%changelog
* Fri Feb 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Fri Aug 27 2021 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt2
- brp_strip_none %_libexecdir/%target/lib/*

* Sat Feb 06 2021 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1
- New version 3.3.0

* Tue Apr 09 2019 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- New version 3.1.0

* Wed Apr 18 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- New version 3.0.0

* Fri Jun 30 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Sisyphus.
