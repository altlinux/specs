# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global processor_arch arm
%global target         %processor_arch-none-eabi
%global gcc_ver        10.2.0
%global gcc_short_ver  10.2
%define _libexecdir /usr/libexec
%brp_strip_none %_libexecdir/*

# we need newlib to compile complete gcc, but we need gcc to compile newlib,
# so compile minimal gcc first
%def_without bootstrap

Name: arm-none-eabi-gcc
Version: %gcc_ver
Release: alt6
Summary: GNU GCC for cross-compilation for %target target
Group: Development/Tools

# Most of the sources are licensed under GPLv3+ with these exceptions:
# LGPLv2+ libquadmath/ libjava/libltdl/ gcc/testsuite/objc.dg/gnu-encoding/generate-random
#         libgcc/soft-fp/ libffi/msvcc.sh
# LGPLv3+ gcc/prefix.c
# BSD libgo/go/regexp/testdata/testregex.cz zlib/example.c libffi/
#     libjava/classpath/external/relaxngDatatype/org/relaxng/datatype/helpers/DatatypeLibraryLoader.java
# GPLv2+ libitm/testsuite/libitm.c/memset-1.c libjava/
# Public Domain libjava/classpath/external/sax/org/xml/sax/ext/EntityResolver2.java
#               libjava/classpath/external/sax/org/xml/sax/ext/DeclHandler.java
# BSL zlib/contrib/dotzlib/DotZLib/GZipStream.cs
License: GPLv2+ and GPLv3+ and LGPLv2+ and BSD
Url: http://www.codesourcery.com/sgpp/lite/%processor_arch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

Source1: README.alt
Source2: bootstrapexplain

Patch: gcc-config.patch

#BuildRequires: rpm-build-python
BuildRequires: gcc-c++ flex zlib-devel libgmp-devel libmpc-devel autogen 
BuildRequires: %target-binutils >= 2.21
%if_with bootstrap

%else
BuildRequires: %target-newlib
Requires: %target-newlib
%endif

Requires: %target-binutils >= 2.21
%add_python_req_skip libstdcxx gdb

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %target platform, instead of for the
native %_arch platform.

This package is based on the CodeSourcery, which includes improved
ARM target support compared to the corresponding GNU GCC release.

%package c++
Summary: Cross Compiling GNU GCC targeted at %target
Group: Development/Tools
AutoReq: yes, nopython
Requires: %name = %version-%release

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %target platform, instead of for the native
%_arch platform.

%prep
%setup
%patch -p2

contrib/gcc_update --touch
cp -a %SOURCE1 .

%build
mkdir -p gcc-%target gcc-nano-%target

#### normal version

pushd gcc-%target

CC="gcc ${RPM_OPT_FLAGS}  -fno-stack-protector" \
../configure \
            --prefix=%_libexecdir \
            --bindir=%_bindir \
            --libexecdir=%_libexecdir \
            --libdir=%_libexecdir \
            --mandir=%_mandir \
            --infodir=%_infodir \
            --target=%target \
            --with-pkgversion="%version-%release" \
            --with-bugurl="https://bugzilla.altlinux.org/" \
            --enable-interwork \
            --enable-multilib \
            --with-python-dir=%target/share/gcc-%version/python \
            --with-multilib-list=rmprofile \
            --enable-plugins \
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
%if_with bootstrap
   --enable-languages=c --with-newlib --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --without-headers --with-system-zlib
%else
   --enable-languages=c,c++ --with-newlib --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib --with-sysroot=%_libexecdir/%target
%endif
#  --enable-lto \

%if_with bootstrap
%make_build all-gcc INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%else
%make_build INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%endif
popd

######### nano version build part (only relevant if not bootstrap)
%if_with bootstrap

%else
mkdir -p gcc-nano-%target
pushd gcc-nano-%target

export CFLAGS_FOR_TARGET="$CFLAGS_FOR_TARGET -fno-exceptions -Os "
export CXXFLAGS_FOR_TARGET="$CXXFLAGS_FOR_TARGET -fno-exceptions -Os "

CC="gcc ${RPM_OPT_FLAGS}  -fno-stack-protector " \
../configure \
            --prefix=%_libexecdir \
            --bindir=%_bindir \
            --libexecdir=%_libexecdir \
            --libdir=%_libexecdir \
            --mandir=%_mandir \
            --infodir=%_infodir \
            --target=%target \
            --with-pkgversion="%version-%release" \
            --with-bugurl="https://bugzilla.altlinux.org/" \
            --enable-interwork \
            --enable-multilib \
            --with-python-dir=%target/share/gcc-%version/python \
            --with-multilib-list=rmprofile \
            --enable-plugins \
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
            --enable-languages=c,c++ --with-newlib --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib --with-sysroot=%_libexecdir/%target
#  --enable-lto \
%make_build INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
popd
%endif

%install
pushd gcc-%target
%if_with bootstrap
make install-gcc DESTDIR=%buildroot
install -p -m 0755 -D %SOURCE2 %buildroot%_bindir/%target-g++
install -p -m 0755 -D %SOURCE2 %buildroot%_bindir/%target-c++
%else
%makeinstall_std
%endif
popd

##### nano version (only relevant non-bootstrap)

%if_with bootstrap

%else
# everybody needs to end up built with the One True DESTDIR
# to arrange for that, move the non-nano DESTDIR out of the way
# temporarily, and make an empty one for the nano build to
# populate.  Later we'll pick just the bits from the nano one
# into the non-nano one, and switch the non-nano one to be
# the One True DESTDIR again.
#
# Without this sleight-of-hand we get rpmbuild errors noticing that
# the DESTDIR the nano bits were built with is not the One True
# DESTDIR.

rm -rf %buildroot-non-nano
mv %buildroot %buildroot-non-nano
pushd gcc-nano-%target

%makeinstall_std
popd
pushd %buildroot
for i in libstdc++.a libsupc++.a ; do
    find . -name "$i" | while read line ; do
        R=`echo $line | sed "s/\.a/_nano\.a/g"`
        echo "%buildroot/$line -> %buildroot-non-nano/$R"
        cp $line %buildroot-non-nano/$R
    done
done
popd

# junk the nano DESTDIR now we picked out the bits we needed into
# the non-nano destdir

# put the "non-nano + picked nano bits" destdir back at the
# One True DESTDIR location.  Even though it has bits from two different
# builds, all the bits feel they were installed to DESTDIR
rm -fR %buildroot
mv %buildroot-non-nano %buildroot

%endif
### end of nano version install magic

# we don't want these as we are a cross version
rm -r %buildroot%_infodir
rm -r %buildroot%_man7dir
rm -f %buildroot%_libdir/libcc1* ||:
rm -f %buildroot%_libexecdir/libcc1* ||:
# these directories are often empty
rmdir %buildroot%_libexecdir/%target/share/gcc-%gcc_ver ||:
rmdir %buildroot%_libexecdir/%target/share ||:
# and these aren't usefull for embedded targets
rm -r %buildroot%prefix/lib*/gcc/%target/%gcc_ver/install-tools ||:
rm -r %buildroot%_libexecdir/gcc/%target/%gcc_ver/install-tools ||:
find  %buildroot%_libexecdir/ -type f -name \*.la -delete

mkdir -p %buildroot%_libexecdir/%target/share/gcc-%gcc_ver/
mv %buildroot%_datadir/gcc-%gcc_ver/* %buildroot%_libexecdir/%target/share/gcc-%gcc_ver/ ||:
rm -rf %buildroot%_datadir/gcc-%gcc_ver ||:

#find %buildroot%_libexecdir/%target -name libstdc++\* |sed -re 's,%buildroot,,' > c++.files
#sed -re 's,^,%exclude ,' < c++.files > c.files

#global __os_install_post . ./os_install_post

%check
%if_with bootstrap
exit 0
%endif
pushd gcc-%target
#BuildRequires: autoge may be needed
%make_build check || :
popd

%files
%doc COPYING* README README.alt
%_bindir/%target-*
%exclude %_bindir/%target-?++
%dir %_libexecdir/gcc
%dir %_libexecdir/gcc/%target
%_libexecdir/gcc/%target/%gcc_ver
%_man1dir/%target-*.1*
%if_with bootstrap
%else
%exclude %_man1dir/%target-?++.1*
%exclude %_libexecdir/gcc/%target/%gcc_ver/cc1plus
%endif

%files c++
%_bindir/%target-?++
%_libexecdir/%target
%if_with bootstrap
%else
%_man1dir/%target-g++.1*
%_libexecdir/gcc/%target/%gcc_ver/cc1plus
%endif

%changelog
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
