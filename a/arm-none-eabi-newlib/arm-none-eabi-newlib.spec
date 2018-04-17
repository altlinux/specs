# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for ARM.
#define _binaries_in_noarch_packages_terminate_build 0

%define target arm-none-eabi
%define pkg_version 3.0.0
%define _libexecdir /usr/libexec
%add_verify_elf_skiplist %_libexecdir/%target/lib/*

Name: arm-none-eabi-newlib
Version: %pkg_version
Release: alt1
Summary: C library intended for use on %target embedded systems
Group: Development/Tools
# For a breakdown of the licensing, see NEWLIB-LICENSING
License: BSD and MIT and LGPLv2+ and ISC
Url: http://sourceware.org/newlib/
Packager: Anton Midyukov <antohami@altlinux.org>

Source:  %name-%version.tar
Source1: README.alt
Source2: NEWLIB-LICENSING
Patch0: ftbfs.patch
Patch1: ftbfs2.patch

BuildRequires: %target-binutils %target-gcc %target-gcc-c++ texinfo
BuildArch: noarch

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
rm -rf build-{newlib,nano}
mkdir build-{newlib,nano}

pushd build-newlib

export CFLAGS="-g -O2 -ffunction-sections -fdata-sections"
../configure \
    --prefix=%_libexecdir \
    --libdir=%_libexecdir \
    --mandir=%_mandir \
    --htmldir=%_docdir/html \
    --pdfdir=%_docdir/pdf \
    --target=%target \
    --enable-interwork \
    --enable-multilib \
    --enable-newlib-io-long-long \
    --disable-nls \
    --disable-libssp \
    --disable-nls \
    --disable-newlib-supplied-syscalls \
    --with-float=soft

%make_build

popd
pushd build-nano
export CFLAGS="-g -Os -ffunction-sections -fdata-sections"
../configure \
    --prefix=%_libexecdir \
    --libdir=%_libexecdir \
    --mandir=%_mandir \
    --target=%target \
    --disable-nls \
    --disable-newlib-supplied-syscalls \
    --enable-newlib-reent-small \
    --disable-newlib-fvwrite-in-streamio \
    --disable-newlib-fseek-optimization \
    --disable-newlib-wide-orient \
    --enable-newlib-nano-malloc \
    --disable-newlib-unbuf-stream-opt \
    --enable-lite-exit \
    --enable-newlib-global-atexit \
    --enable-newlib-nano-formatted-io

%make_build

popd

%install
pushd build-newlib
%makeinstall_std
popd
pushd build-nano
NANO_ROOT=%buildroot/nano
make install DESTDIR=$NANO_ROOT

for i in $(find $NANO_ROOT -regex ".*/lib\(c\|g\|rdimon\)\.a"); do
    file=$(basename $i | sed "s|\.a|_nano\.a|")
    target_path=$(dirname $i | sed "s|$NANO_ROOT||")
    mv $i "%buildroot$target_path/$file"
done
popd

cp %SOURCE1 .
cp %SOURCE2 .

# we don't want these as we are a cross version
rm -rf %buildroot%_infodir

rm -rf $NANO_ROOT

%files
%doc README.alt
%doc NEWLIB-LICENSING COPYING*
%dir %_libexecdir/%target
%dir %_libexecdir/%target/include/
%_libexecdir/%target/include/*
%dir %_libexecdir/%target/lib
%_libexecdir/%target/lib/*

%changelog
* Wed Apr 18 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- New version 3.0.0

* Fri Jun 30 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Sisyphus.
