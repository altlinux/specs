Name: i2c-tools
Version: 4.3
Release: alt2

Summary: I2C tools
License: GPLv2+
Group: System/Kernel and hardware
Url: https://i2c.wiki.kernel.org/index.php/I2C_Tools

Conflicts: lm_sensors < 3
Provides: eepromer = %version-%release
Obsoletes: eepromer
Provides: i2c-tools-perl = %version-%release
Obsoletes: i2c-tools-perl

Source: %name-%version-%release.tar
# Source-url: https://www.kernel.org/pub/software/utils/i2c-tools/%name-%version.tar.xz

BuildRequires: python3-devel
BuildRequires: python3(setuptools)

%description
%name package contains a heterogeneous set of I2C tools for Linux:
a bus probing tool, a chip dumper, register-level SMBus access helpers,
EEPROM decoding scripts, and EEPROM programming tools.

%package -n python3-module-i2c-tools
Summary: Python 3 bindings for Linux SMBus access through i2c-dev
Group: Development/Python3
License: GPLv2

%description -n python3-module-i2c-tools
Python 3 bindings for Linux SMBus access through i2c-dev

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

%description -n libi2c-devel
%summary.

%prep
%setup
sed -i 's,distutils\.core,setuptools,' py-smbus/setup.py

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" BUILD_STATIC_LIB=0 EXTRA=eeprog
pushd py-smbus
CFLAGS="$RPM_OPT_FLAGS -I../include" LDFLAGS="$RPM_LD_FLAGS" \
%__python3 setup.py build -b build-py3
popd

%install
%makeinstall_std PREFIX=%prefix BUILD_STATIC_LIB=0 \
  EXTRA=eeprog libdir=%_libdir
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

%files
%doc CHANGES COPYING README
%config(noreplace) %_libdir/modprobe.d/i2c-dev.conf
%config(noreplace) %_sysconfdir/udev/makedev.d/99-i2c-dev.nodes
%_sbindir/i2c*
%_sbindir/eeprog
%_sbindir/i2c-stub*
%_bindir/decode-*
%_man8dir/eeprog.8*
%_man8dir/i2c*.8*
%_man1dir/decode-*.1*
%_man8dir/i2c-stub-from-dump.8*
%_libdir/modules-load.d/%name.conf

%files -n python3-module-i2c-tools
%doc py-smbus/README
%python3_sitelibdir/*

%files -n libi2c
%doc COPYING.LGPL
%_libdir/libi2c.so.0*

%files -n libi2c-devel
%dir %_includedir/i2c
%_includedir/i2c/smbus.h
%_libdir/libi2c.so
%_man3dir/libi2c.3*

%changelog
* Tue Dec 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3-alt2
- dropped obsolete distutils build req

* Thu Sep 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3-alt1
- 4.3 released
- dropped obsolete eepromer subpackage
- merged back perl subpackage (closes: 40890)

* Thu Dec 27 2018 Anton Midyukov <antohami@altlinux.org> 4.0-alt1
- 4.0 released

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Sat Mar 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- initial release
