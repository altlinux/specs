%def_disable static

Name: lm_sensors3
Version: 3.4.0
Release: alt2

Summary: Hardware Health Monitoring Tools
License: LGPLv2+ and GPLv3+ and GPLv2+ and Verbatim and Public Domain
Group: System/Kernel and hardware
Url: http://www.lm-sensors.org/
Packager: Afanasov Dmitry <ender@altlinux.org> 

Source: %name-%version.tar
Source1: lm_sensors.init
Source2: lm_sensors.service
Source3: lm_sensors.sysconfig
Source4: lm_sensors-modprobe-wrapper
Source5: lm_sensors-modprobe-r-wrapper
Source6: sensord.service
Source7: sensord.sysconfig
Source8: sensord-service-wrapper

Patch1: lm_sensors3-3.4.0-alt-set_limit.patch
Patch2: lm_sensors3-3.1.0-makefile-norpath.patch

Requires: libsensors3 = %version-%release
Provides: lm_sensors
Obsoletes: lm_sensors
Conflicts: lm_sensors < 3.1.0-alt1

Provides: lm_sensors = %version-%release

BuildRequires: flex bison
BuildRequires: librrd-devel >= 1.2.1

BuildPreReq: rpm-macros-make

#define _unpackaged_files_terminate_build 1

%package utils
Summary: Hardware Health Monitoring utils
Group: Monitoring
Requires: %name = %version-%release
Provides: lm_sensors-utils
Obsoletes: lm_sensors-utils
Conflicts: sensorfw

%package -n libsensors3
Summary: Shared library for hardware health monitoring tools
Group: System/Libraries
Provides: libsensors
Obsoletes: libsensors

%package -n libsensors3-devel
Summary: Development environment for hardware health monitoring tools
Group: Development/C
Requires: libsensors3 = %version-%release
Provides: %name-devel = %version
Provides: libsensors-devel
Obsoletes: libsensors-devel
Conflicts: libsensors-devel

%package -n libsensors3-devel-static
Summary: Static library for developing hardware health monitoring tools
Group: Development/C
Requires: libsensors-devel = %version-%release
Provides: libsensors-devel-static
Obsoletes: libsensors-devel-static
Conflicts: libsensors-devel-static

%description
This package contains a collection of user space tools for general SMBus
access and hardware monitoring.  SMBus, also known as System Management Bus,
is a protocol for communicating through a I2C ('I squared C') bus.  Many modern
mainboards have a System Management Bus.  There are a lot of devices which can
be connected to a SMBus; the most notable are modern memory chips with EEPROM
memories and chips for hardware monitoring.

Most modern mainboards incorporate some form of hardware monitoring chips.
These chips read things like chip temperatures, fan rotation speeds and
voltage levels.  There are quite a few different chips which can be used
by mainboard builders for approximately the same results.

%description utils
lm_sensors utils

%description -n libsensors3
This package contains shared library required for user space applications
for general SMBus access and hardware monitoring.  SMBus, also known as
System Management Bus, is a protocol for communicating through a I2C
('I squared C') bus.  Many modern mainboards have a System Management Bus.
There are a lot of devices which can be connected to a SMBus; the most
notable are modern memory chips with EEPROM memories and chips for hardware
monitoring.

%description -n libsensors3-devel
This package contains environment for development of user space applications
for general SMBus access and hardware monitoring.  SMBus, also known as
System Management Bus, is a protocol for communicating through a I2C
('I squared C') bus.  Many modern mainboards have a System Management Bus.
There are a lot of devices which can be connected to a SMBus; the most
notable are modern memory chips with EEPROM memories and chips for hardware
monitoring.

%description -n libsensors3-devel-static
This package contains static library for development of statically linked
user space applications for general SMBus access and hardware monitoring.

%prep
%setup -q
%patch1 -p2
%patch2 -p2

# fixing the sensord-service-wrapper path
cp -p %SOURCE2 lm_sensors.service
cp -p %SOURCE6 sensord.service
sed -i "s|\@WRAPPER_DIR\@|%_libexecdir/%name|" lm_sensors.service
sed -i "s|\@WRAPPER_DIR\@|%_libexecdir/%name|" sensord.service

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%make_build_ext PROG_EXTRA=sensord

%install
%set_verify_elf_method strict

%make DESTDIR=%buildroot \
      PREFIX=/usr \
      MANDIR=%_mandir \
      ETCDIR=%_sysconfdir \
      LIBDIR=%_libdir \
      INCLUDEDIR=%_includedir \
      LIBINCLUDEDIR=%_includedir/sensors \
      PROG_EXTRA=sensord \
      EXLDFLAGS= \
      install

mkdir -p %buildroot%_sysconfdir/sysconfig
install -pm 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/lm_sensors
install -pm 644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/sensord

# service files
install -pD -m755 %SOURCE1 %buildroot%_initrddir/lm_sensors
install -pD -m644 lm_sensors.service %buildroot%_unitdir/lm_sensors.service
install -pD -m644 lm_sensors.service %buildroot%_unitdir/sensord.service
install -pD -m644 prog/init/fancontrol.service %buildroot%_unitdir/fancontrol.service

# customized modprobe calls
mkdir -p %buildroot%_libexecdir/%name
install -pm 755 %SOURCE4 %buildroot%_libexecdir/%name/lm_sensors-modprobe-wrapper
install -pm 755 %SOURCE5 %buildroot%_libexecdir/%name/lm_sensors-modprobe-r-wrapper

# sensord service wrapper
install -pm 755 %SOURCE8 %buildroot%_libexecdir/%name/sensord-service-wrapper

install -pD -m755 prog/init/sensord.init %buildroot%_datadir/%name/sensord.init
install -pD -m755 prog/init/fancontrol.init %buildroot%_datadir/%name/fancontrol.init

install -pD -m755 prog/init/sysconfig-lm_sensors-convert %buildroot%_datadir/%name/sysconfig-lm_sensors-convert

mkdir -p %buildroot%_datadir/%name
cp -ar prog/tellerstats %buildroot%_datadir/%name

%post
%post_service lm_sensors

%preun
%preun_service lm_sensors

%triggerun -- lm_sensors < 3
if [ $1 -eq 1 ] && [ $2 -eq 0 ] && [ -f /etc/sysconfig/lm_sensors ]; then
    echo "Try to convert /etc/sysconfig/lm_sensors to new format."
    cp /etc/sysconfig/lm_sensors /etc/sysconfig/lm_sensors.old
    if %_datadir/%name/sysconfig-lm_sensors-convert; then
        echo "Convertion OK"
    else
        echo "Convertion FAILED. Run sensors-detect."
    fi
fi
if [ $1 -eq 0 ] && [ $2 -eq 1 ] && [ -f /etc/sysconfig/lm_sensors.old ]; then
    echo "Restore saved /etc/sysconfig/lm_sensors for v2"
    mv /etc/sysconfig/lm_sensors.old /etc/sysconfig/lm_sensors
fi

%files
%doc doc/ README CHANGES COPYING COPYING.LGPL
%config(noreplace) %_sysconfdir/sensors3.conf
%dir %_sysconfdir/sensors.d
%config(noreplace) %_sysconfdir/sysconfig/lm_sensors
%config %_initdir/lm_sensors
%_unitdir/lm_sensors.service
%_bindir/sensors
%_bindir/sensors-conf-convert
%_sbindir/sensors-detect
%_man1dir/sensors.1*
%_man5dir/sensors.conf.5*
%_man5dir/sensors3.conf.5*
%_man8dir/sensors-detect.8*
%dir %_datadir/%name
%_datadir/%name/sysconfig-lm_sensors-convert
%dir %_libexecdir/%name
%_libexecdir/%name/lm_sensors-modprobe*wrapper

%files utils
%_sbindir/sensord
%_unitdir/sensord.service
%_sbindir/fancontrol
%_unitdir/fancontrol.service
%ifnarch %arm e2k
%_sbindir/isadump
%_sbindir/isaset
%endif
%_sbindir/pwmconfig
%_datadir/%name
%_man8dir/fancontrol.*
%ifnarch %arm e2k
%_man8dir/isadump.*
%_man8dir/isaset.*
%endif
%_man8dir/pwmconfig.*
%_man8dir/sensors-conf-convert.8.*
%_man8dir/sensord.*
%exclude %_datadir/%name/sysconfig-lm_sensors-convert
%_libexecdir/%name/sensord-service-wrapper
%config(noreplace) %{_sysconfdir}/sysconfig/sensord

%files -n libsensors3
%_libdir/*.so.*
%exclude %_libdir/*.a

%files -n libsensors3-devel
%doc doc/libsensors-API.txt doc/svn doc/developers
%_libdir/*.so
%_includedir/sensors
%_man3dir/*

%if_enabled static
%files -n libsensors3-devel-static
%_libdir/*.a
%endif #static

%changelog
* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- E2K: don't expect isadump(8) and isaset(8), like on %%arm

* Sat Jul 30 2016 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt1
- new version 3.4.0 (Closes: 30090)
- update license
- added provides and obsoletes lm_sensors (Closes: 28974)
- added conflict with sensorfw (both contain the file /usr/sbin/sensord)
- added lsb-header in lm_sensors.init

* Thu Aug 07 2014 Denis Smirnov <mithraen@altlinux.ru> 3.3.2-alt3
- add systemd unit (#30221)
- add fancontrol.service (#30186)

* Thu Feb 28 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.2-alt2
- rebuilt with LFS

* Fri Mar 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 3.3.2-alt1
- new version

* Thu Sep 22 2011 Sergey Y. Afonin <asy@altlinux.ru> 3.3.1-alt1
- new version

* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 3.3.0-alt1
- new version

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt2.1.2
- Rebuilt for debuginfo

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 3.1.2-alt2.1.1
- rebuild (with the help of girar-nmu utility)

* Thu May 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1.2-alt2.1
- isa* turned off on ARM

* Mon Apr 26 2010 Afanasov Dmitry <ender@altlinux.org> 3.1.2-alt2
- rebuild with new rrd

* Thu Feb 04 2010 Anton Farygin <rider@altlinux.ru> 3.1.2-alt1
- removed kernel requires (closes #22888)
- updated to release 3.1.2
- fixed build (remove rpath entry from /usr/bin/sensors)

* Wed Jul 08 2009 Afanasov Dmitry <ender@altlinux.org> 3.1.1-alt1
- 3.1.1 release

* Sat Jun 27 2009 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt4
- place headers into /usr/include/sensors (closes: #20595)

* Sun May 31 2009 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt3
- right fix: versioning conflict

* Sun May 31 2009 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt2
- remove Provides: lm_sensors.

* Mon Apr 13 2009 Afanasov Dmitry <ender@altlinux.org> 3.1.0-alt1
- Initial build (spec based upon lm_sensors-2.10)

