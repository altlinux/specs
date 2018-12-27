Name: i2c-tools
Version: 4.0
Release: alt1

Summary: I2C tools
License: GPLv2+
Group: System/Kernel and hardware
Url: https://i2c.wiki.kernel.org/index.php/I2C_Tools

Conflicts: lm_sensors < 3

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version-%release.tar
# Source-url: https://www.kernel.org/pub/software/utils/i2c-tools/%name-%version.tar.xz

# Upstream patch
Patch0:         0001-i2c-tools-i2cbusses-Avoid-buffer-overflows-in-sysfs-.patch
# Upstream patch
Patch1:         0002-tools-i2cbusses-Check-the-return-value-of-snprintf.patch
# Upstream patch
Patch2:         0003-py-smbus-Fix-FSF-address-in-smbusmodule.c.patch
# Upstream patch fixing license headers of libi2c
Patch3:         0001-libi2c-Mention-the-correct-license-in-source-files.patch

BuildRequires: python3-devel

Requires: libi2c = %EVR

%description
%name package contains a heterogeneous set of I2C tools for Linux:
a bus probing tool, a chip dumper, register-level SMBus access helpers,
EEPROM decoding scripts, and EEPROM programming tools.

%package eepromer
Summary: Programs for reading / writing i2c / smbus eeproms
# %_sbindir/eeprom is Public Domain, the rest is GPLv2+
License: GPLv2+ and Public Domain
Group: System/Kernel and hardware
Requires: libi2c%{?_isa} = %version-%release
# For the device nodes
Requires: %name = %EVR

%description eepromer
Programs for reading / writing i2c / smbus eeproms. Notice that writing the
eeproms in your system is very dangerous and is likely to render your system
unusable. Do not install, let alone use this, unless you really, _really_ know
what you are doing.

%package -n python3-module-i2c-tools
Summary: Python 3 bindings for Linux SMBus access through i2c-dev
Group: Development/Python3
License: GPLv2
Requires: libi2c = %EVR

%description -n python3-module-i2c-tools
Python 3 bindings for Linux SMBus access through i2c-dev

%package perl
Summary: i2c tools written in Perl
License: GPLv2+
Group: Development/Python3
Requires: libi2c = %EVR

%description perl
A collection of tools written in perl for use with i2c devices.

%package -n libi2c
Summary: I2C/SMBus bus access library
License: LGPLv2+
Group: System/Kernel and hardware

%description -n libi2c
libi2c offers a way for applications to interact with the devices
connected to the I2C or SMBus buses of the system.

%package -n libi2c-devel
Summary: Development files for the I2C library
License: LGPLv2+
Group: Development/C
Requires: libi2c = %EVR

%description -n libi2c-devel
%summary.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" BUILD_STATIC_LIB=0 EXTRA=eeprog
pushd eepromer
make CFLAGS="$RPM_OPT_FLAGS -I../include" LDFLAGS="$RPM_LD_FLAGS"
popd
pushd py-smbus
CFLAGS="$RPM_OPT_FLAGS -I../include" LDFLAGS="$RPM_LD_FLAGS" \
%__python3 setup.py build -b build-py3
popd

%install
%makeinstall_std prefix=%prefix BUILD_STATIC_LIB=0 \
  EXTRA=eeprog libdir=%_libdir
install -m 755 eepromer/{eepromer,eeprom} \
%buildroot%_sbindir
install -m 644 eepromer/{eepromer,eeprom}.8 \
%buildroot%_man8dir
pushd py-smbus
%__python3 setup.py build -b build-py3 install --skip-build --root=%buildroot
popd

# cleanup
rm -f %buildroot%_bindir/decode-edid.pl
# Remove unpleasant DDC tools.  KMS already exposes the EDID block in sysfs,
# and edid-decode is a more complete tool than decode-edid.
rm -f %buildroot%_bindir/{ddcmon,decode-edid}

# for i2c-dev ondemand loading through kmod
mkdir -p %buildroot%_libdir/modprobe.d
echo "alias char-major-89-* i2c-dev" > \
%buildroot%_libdir/modprobe.d/i2c-dev.conf
# for /dev/i2c-# creation (which are needed for kmod i2c-dev autoloading)
mkdir -p %buildroot%_sysconfdir/udev/makedev.d
for (( i = 0 ; i < 8 ; i++ )) do
  echo "i2c-$i" >> %buildroot%_sysconfdir/udev/makedev.d/99-i2c-dev.nodes
done

# auto-load i2c-dev after reboot
mkdir -p %buildroot%_libdir/modules-load.d
echo 'i2c-dev' > %buildroot%_libdir/modules-load.d/%name.conf

%post
# load i2c-dev after the first install
if [ "$1" = 1 ] ; then
/sbin/modprobe i2c-dev
fi
exit 0

%files
%doc CHANGES COPYING README
%config(noreplace) %_libdir/modprobe.d/i2c-dev.conf
%config(noreplace) %_sysconfdir/udev/makedev.d/99-i2c-dev.nodes
%_sbindir/i2c*
%exclude %_sbindir/i2c-stub*
%_man8dir/i2c*.8.*
%exclude %_man8dir/i2c-stub-from-dump.8.*
%_libdir/modules-load.d/%name.conf

%files eepromer
%doc eepromer/README*
%doc eeprog/README.eeprog
%_sbindir/eepro*
%_man8dir/eepro*.8.*

%files -n python3-module-i2c-tools
%doc py-smbus/README
%python3_sitelibdir/*

%files perl
%doc eeprom/README
%_bindir/decode-*
%_sbindir/i2c-stub*
%_man1dir/decode-*.1.*
%_man8dir/i2c-stub-from-dump.8.*

%files -n libi2c
%doc COPYING.LGPL
%_libdir/libi2c.so.0*

%files -n libi2c-devel
%dir %_includedir/i2c
%_includedir/i2c/smbus.h
%_libdir/libi2c.so

%changelog
* Thu Dec 27 2018 Anton Midyukov <antohami@altlinux.org> 4.0-alt1
- 4.0 released

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Sat Mar 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- initial release
