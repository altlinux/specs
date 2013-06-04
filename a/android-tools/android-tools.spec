Name: android-tools
Version: 4.2.2
Release: alt1

Summary: Android Debug CLI tools
License: APL
Group: Development/Tools

Source: %name-%version-%release.tar

BuildRequires: libselinux-devel libssl-devel zlib-devel

%description
This package contains following utilities:

Android Debug Bridge (adb) -- it is a versatile tool, which lets you manage
the state of an emulator instance or Android-powered device.

Fastboot is protocol used to update the flash filesystem in Android devices
from a host over USB. It allows flashing of unsigned partition images.

%prep
%setup

%build
make -f ../../debian/makefiles/adb.mk -C core/adb CFLAGS='%optflags'
make -f ../../debian/makefiles/fastboot.mk -C core/fastboot CFLAGS='%optflags'
#make -f ../../debian/makefiles/ext4_utils.mk -C extras/ext4_utils CFLAGS='%optflags'

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -pm0755 core/adb/adb core/fastboot/fastboot %buildroot%_bindir
install -pm0644 debian/adb.1 %buildroot%_man1dir

%files
%_bindir/adb
%_bindir/fastboot
%_man1dir/adb.1*

%changelog
* Tue Jun 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.2-alt1
- 4.2.2 released

* Mon Mar 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.1-alt1
- initial
