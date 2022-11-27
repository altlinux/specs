# requires pandoc
%def_enable docs

Name: android-tools
Version: 10.0.0
Release: alt5.r36

Summary: Android Debug CLI tools
License: APL
Group: Development/Tools

Url: http://developer.android.com/guide/developing/tools/
# For sources use the following repositories:
#  https://android.googlesource.com/platform/system/core
#  https://android.googlesource.com/platform/system/extras
# fetching sources example:
# ANDROID_TAG="android-5.1.1_r38" debian/create-snapshot

Source: %name-%version-%release.tar

# Debian core patches
Patch0: move-log-file-to-proper-dir.patch
Patch1: Added-missing-headers.patch
Patch3: libusb-header-path.patch
Patch4: stdatomic.patch
Patch5: Nonnull.patch
Patch7: Vector-cast.patch
Patch8: use-Python-3-for-mkbootimg.patch
Patch11: throw-exception-on-unknown-os.patch
Patch12: simg_dump-python3.patch
Patch13: fix-attribute-issue-with-gcc.patch
Patch14: workaround-error-expected-primary-expression-before-.-token.patch
Patch15: fix-gettid-exception-declaration.patch
Patch16: fix-build-on-non-x86.patch
#Patch17: add-missing-headers.patch
Patch18: hard-code-build-number.patch

# Debian libunwind patches
Patch30: user_pt_regs.patch
Patch31: legacy_built-in_sync_functions.patch
Patch32: 20150704-CVE-2015-3239_dwarf_i.h.patch

# patch from OpenMandriva
Patch100: libcrypto_utils-openssl-1.1.patch
Patch101: adb-system-openssl.patch

# misc patches
Patch150: adb-usb_linux-fix-usb_handle.patch

# ALT patches
Patch200: alt-libbacktrace-fix-GetErrorString-return.patch
Patch201: alt-make-ext4fs-fix-fs_config-include.patch
Patch202: alt-libunwind-fix-ppc64le-build.patch
Patch203: alt-libadb-fix-attribute-usage.patch
Patch204: alt-liblp-fix-cstring-header.patch
Patch205: alt-libunwindstack-dirty-ppc64-compile-fix.patch
Patch206: alt-libunwindstack-dwarfmemory-include-cstddef.patch

Requires: udev-android

BuildRequires: gcc-c++
BuildRequires: liblzma-devel
BuildRequires: libssl-devel zlib-devel libselinux-devel
BuildRequires: libusb-devel libgtest-devel libsafe-iop-devel
%if_enabled docs
BuildRequires: pandoc
%endif
BuildRequires: rpm-build-python3

%description
This package contains following utilities:

Android Debug Bridge (adb) -- it is a versatile command line tool, which lets
you communicate with an emulator instance or connected Android-powered device.

Fastboot -- is a command line tool for flashing an Android device, boot an
Android device to fastboot mode, etc.

Mkbootimg -- creates Android boot images that includes kernel image and ramdisk,
in a special format which can be used with fastboot.

Command line tools to create sparse images for usage with Android devices.
Includes sim2img, img2simg, simg2simg and append2simg tools.

%prep
%setup
pushd system/core
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
#%patch17 -p1
%patch18 -p1
popd

pushd system/external/libunwind
%patch30 -p1
%patch31 -p1
%patch32 -p1
popd

pushd system/core
%patch100 -p3
%patch101 -p3

%patch200 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
popd

pushd system/core/adb
%patch150 -p1
popd

pushd system/extras
#%patch201 -p3
popd

pushd system/external/libunwind
%patch202 -p4
popd

%build

%add_optflags %optflags_shared

%define makefilesdir %_builddir/%name-%version/debian/makefiles
%define outbindir %_builddir/%name-%version/out_bin
%define outlibdir %_builddir/%name-%version/out_lib
%define outmandir %_builddir/%name-%version/out_man

%define aprefix %_libdir/android

case %_arch in
    "aarch64")
        CPU="arm64"
        ;;
    "armh")
        CPU="arm"
        ;;
    "i586")
        CPU="x86"
        ;;
    "x86_64")
        CPU="x86_64"
        ;;
    "ppc64le")
        CPU="ppc64"
        ;;
    "mipsel")
        CPU="mips"
        ;;
    *)
        false
        ;;
esac

CFLAGS+=" %optflags -DNDEBUG -UDEBUG -Wno-unknown-pragmas -Wno-attributes"
CFLAGS+=" -I%_builddir/%name-%version/debian/include"
CPPFLAGS+=" %optflags -DNDEBUG -UDEBUG -Wno-unknown-pragmas -Wno-attributes"
CPPFLAGS+=" -I%_builddir/%name-%version/debian/include"
CPPFLAGS+=" $(getconf LFS_CFLAGS)"
LDFLAGS+=" -Wl,-R%aprefix/lib -L%outlibdir"
DEB_VERSION=%version
export CFLAGS CPPFLAGS LDFLAGS DEB_VERSION CPU

mkdir -p %outbindir
mkdir -p %outlibdir
mkdir -p %outmandir

# dirty workaround to link against 7z library (needed for libunwind)
ln -s %_libdir/p7zip/7z.so %outlibdir/lib7z.so

# building libunwind
pushd system/external/libunwind
OUT_DIR=%outlibdir make -f %makefilesdir/libunwind.mk
popd

# order is important
core_components_libs=" \
		    liblog \
		    libbase \
		    libcutils \
		    libcrypto_utils \
		    libadb \
 		    libbacktrace \
		    libutils \
		    libziparchive \
		    libsparse"
core_simg_tools=" \
		    simg2img \
		    simg2simg \
		    img2simg \
		    append2simg"

core_tools="adb fastboot"

extras_components_libs=" \
		    libext4_utils"

# building core libraries at first
pushd system/core
for i in $core_components_libs; do
    make -f %makefilesdir/$i.mk
    cp -a $i.so* %outlibdir
done
popd

# now building extra libraries
pushd system/extras
for i in $extras_components_libs; do
    OUT_DIR=%outlibdir make -f %makefilesdir/$i.mk
done
popd

# building core tools
pushd system/core
for i in $core_tools; do
    make -f %makefilesdir/$i.mk
    cp -a $i/$i %outbindir
done

# simg stuff requires special handling as it is libsparse-based
for i in $core_simg_tools; do
    make -f %makefilesdir/$i.mk
    cp -a libsparse/$i %outbindir
done
popd

# we do not need symlink to 7z library anymore
rm -f %outlibdir/lib7z.so

# do not forget about mkbootimg
cp system/core/mkbootimg/mkbootimg.py %outbindir/mkbootimg
cp system/core/mkbootimg/unpack_bootimg.py %outbindir/unpack_bootimg

%if_enabled docs
# building man pages
for i in $core_tools; do
    pandoc -s -o %outmandir/$i.1 debian/$i.1.md
done
%endif

%install

core_tools="adb fastboot"

mkdir -p %buildroot%_bindir %buildroot%aprefix/bin %buildroot%aprefix/lib %buildroot%_man1dir

for i in $core_tools mkbootimg unpack_bootimg; do
    install -pm0755 %outbindir/$i %buildroot%_bindir/$i
done
for i in append2simg img2simg simg2img simg2simg; do
    install -pm0755 %outbindir/$i %buildroot%aprefix/bin
done

cp -a %outlibdir/* %buildroot%aprefix/lib

for i in $core_tools; do
    install -pm0644 %outmandir/$i.1 %buildroot%_man1dir
done

mkdir -p %buildroot%_sysconfdir/bash_completion.d
for i in $core_tools; do
    install -pm0644 debian/bash_completion.d/$i %buildroot%_sysconfdir/bash_completion.d
done

%files
%_bindir/*
%_man1dir/*
%_sysconfdir/bash_completion.d/*
%aprefix

%changelog
* Sun Nov 27 2022 Pavel Nakonechnyi <zorg@altlinux.org> 10.0.0-alt5.r36
- Fix build failure with new Linux kernel headers
  See https://github.com/torvalds/linux/commit/94dfc73e7cf4a31da66b8843f0b9283ddd6b8381
  https://github.com/nmeum/android-tools/issues/74

* Sat Mar 19 2022 Pavel Nakonechnyi <zorg@altlinux.org> 10.0.0-alt4.r36
- remove p7zip from link dependencies: replacing it with llzma (from Debian)

* Sat Oct 16 2021 Pavel Nakonechnyi <zorg@altlinux.org> 10.0.0-alt3.r36
- fix build on the update toolchain
- backport some Debian buildfiles updates

* Mon May 03 2021 Pavel Nakonechnyi <zorg@altlinux.org> 10.0.0-alt2.r36
- add rpm-build-python3 as a build requirement

* Fri Dec 18 2020 Pavel Nakonechnyi <zorg@altlinux.org> 10.0.0-alt1.r36
- updated to 10.0.0_r36
- debian/create-snapshot updated
- Debian patches refreshed
- Debian makefiles refreshed
- Debian 7z includes updated
- f2fs is not used anymore
- ext4* tools are not used anymore
- documentation and bash completion updated
- minor spec cleanup

* Fri Jun 19 2020 Ivan A. Melnikov <iv@altlinux.org> 8.1.0-alt3.r23
- mipsel support

* Sun Oct 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.1.0-alt2.r23
- udev-android added as a requirement (closes #37284)

* Tue Aug 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.1.0-alt1.r23
- updated to 8.1.0_r23

* Sat Jul 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.1.1-alt4
- Fixed build on ppc64le (tnx to Hans Boehm for stdatomic patch).

* Tue Sep 04 2018 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt3
- rebuilt with OpenSSL 1.1.x

* Tue Aug 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt2
- patches to support OpenSSL 1.1.x are enabled
- fixed bash completions installation

* Wed Mar 15 2017 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt1
- updated to Debian 5.1.1_r38 release

* Tue Jun 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.2-alt1
- 4.2.2 released

* Mon Mar 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.1-alt1
- initial
