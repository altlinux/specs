Name: android-tools
Version: 5.1.1
Release: alt1

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

Patch0: add-bq-vendor-id.patch
Patch1: remove-selinux-android.patch
Patch2: use-capability.patch
Patch3: use-local-socket.patch
Patch4: ppc64el-ftbfs.patch
Patch5: remove-fs-config-android.patch
Patch6: fix-implicit-pointer-conversion.patch
Patch7: preserve-ownership.patch
Patch8: mkbootimg-Add-dt-parameter-to-specify-DT-image.patch
Patch9: remove-bionic-android.patch
Patch10: define-shell-command.patch
Patch11: fix-implicit-declaration-function.patch
Patch12: adb_libssl_11.diff
Patch13: adb_libssl_bc.diff

BuildRequires: libselinux-devel libssl-devel zlib-devel libpcre-devel

%description
This package contains following utilities:

Android Debug Bridge (adb) -- it is a versatile tool, which lets you manage
the state of an emulator instance or Android-powered device.

Fastboot -- is a diagnostic protocol primarily used to update the flash
filesystem of Android devices over USB.

Mkbootimg -- creates Android boot images that includes kernel image and ramdisk,
in a special format which can be used with fastboot.

%prep
%setup
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p1
#%patch11 -p1
# for openssl 1.1:
#%patch12 -p1
#%patch13 -p1

# use system libselinux
sed -i -e 's/\(LIBS.*\) libselinux.a \(.*\)/\1 -lselinux \2/' debian/makefiles/fastboot.mk
sed -i -e 's/\(fastboot: .*\) libselinux.a \(.*\)/\1 \2/' debian/makefiles/fastboot.mk

%build
# keep this tricks or move from debian makefiles to more adequate ones
mkdir out
for i in adb fastboot mkbootimg; do
    android_arch="linux-x86" CFLAGS='%optflags' make -f debian/makefiles/$i.mk
    cp $i out
    android_arch="linux-x86" CFLAGS='%optflags' make -f debian/makefiles/$i.mk clean
done

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
for i in adb fastboot mkbootimg; do
    install -pm0755 out/$i %buildroot%_bindir
done
for i in adb fastboot; do
    install -pm0644 debian/$i.1 %buildroot%_man1dir
done
for i in adb fastboot; do
    install -pm0644 debian/bash_completion.d/$i %buildroot%_sysconfdir
done

%files
%_bindir/adb
%_bindir/fastboot
%_bindir/mkbootimg
%_man1dir/adb.1*
%_man1dir/fastboot.1*

%changelog
* Wed Mar 15 2017 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt1
- updated to Debian 5.1.1_r38 release

* Tue Jun 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.2-alt1
- 4.2.2 released

* Mon Mar 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.1-alt1
- initial
