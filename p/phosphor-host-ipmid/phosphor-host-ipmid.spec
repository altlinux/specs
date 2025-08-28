%set_verify_elf_method unresolved=relaxed

Name: phosphor-host-ipmid
Version: 1.0.0
Release: alt2.gita809fa5

Summary: dbus-based ipmid for host-endpoint IPMI commands
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-host-ipmid
Vcs: https://github.com/openbmc/phosphor-host-ipmid.git

Source: %name-%version.tar
Patch0: 0001-boost-version-1.86-support.patch
Patch1: 0002-Fix-bug-in-the-name-of-array-of-whitelisted-commands.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: boost-asio-devel
BuildRequires: boost-devel-headers
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: cli11-devel
BuildRequires: gcc-c++
BuildRequires: libpam0-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsdeventplus-devel
BuildRequires: libssl-devel
BuildRequires: libstdplus-devel
BuildRequires: libsystemd-devel
BuildRequires: meson
BuildRequires: pkg-config
BuildRequires: sdbusplus-tools

%description
%summary.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C++
BuildArch: noarch
Requires: libipmid-devel = %EVR
Requires: libsoftoff-dbus-devel = %EVR

%description -n %name-devel
%summary.

%package -n ipmid
Summary: Tool from the %name
Group: Other
Requires: libipmid = %EVR

%description -n ipmid
%summary.

%package -n phosphor-softpoweroff
Summary: Tool from the %name
Group: Other
Requires: libipmid = %EVR
Requires: libsoftoff-dbus = %EVR

%description -n phosphor-softpoweroff
%summary.

%package -n libipmid
Summary: Library from the %name
Group: System/Libraries

%description -n libipmid
%summary.

%package -n libsoftoff-dbus
Summary: Library from the %name
Group: System/Libraries

%description -n libsoftoff-dbus
%summary.

%package -n libipmid-devel
Summary: Development files for the libipmid
Group: Development/C++
Requires: libipmid = %EVR

%description -n libipmid-devel
%summary.

%package -n libsoftoff-dbus-devel
Summary: Development files for the libsoftoff-dbus
Group: Development/C++
Requires: libsoftoff-dbus = %EVR

%description -n libsoftoff-dbus-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files -n ipmid
%_bindir/ipmid

%files -n phosphor-softpoweroff
%_bindir/phosphor-softpoweroff

%files -n %name-devel
%_includedir/user_channel/*.hpp
%_includedir/user_channel/*.cpp
%_includedir/user_channel/meson.build

%files -n libipmid
%_libdir/libchannellayer.so.*
%_libdir/libipmid.so.*
%_libdir/ipmid-providers/libdynamiccmds.so.*
%_libdir/ipmid-providers/libipmi20.so.*
%_libdir/ipmid-providers/libsysintfcmds.so.*
%_libdir/ipmid-providers/libusercmds.so.*
%_libdir/ipmid-providers/libwhitelist.so.*
%_libdir/libuserlayer.so.*

%files -n libsoftoff-dbus
%_libdir/libsoftoff-dbus.so.*

%files -n libipmid-devel
%dir %_includedir/ipmid
%_includedir/ipmid/*.hpp
%_includedir/ipmid/*.h
%dir %_includedir/ipmid-host
%_includedir/ipmid-host/*.hpp
%dir %_includedir/ipmid/message
%_includedir/ipmid/message/*.hpp
%_libdir/libchannellayer.so
%_libdir/libipmid.so
%_libdir/ipmid-providers/libdynamiccmds.so
%_libdir/ipmid-providers/libipmi20.so
%_libdir/ipmid-providers/libsysintfcmds.so
%_libdir/ipmid-providers/libusercmds.so
%_libdir/ipmid-providers/libwhitelist.so
%_libdir/libuserlayer.so
%_pkgconfigdir/libchannellayer.pc
%_pkgconfigdir/libipmid.pc
%_pkgconfigdir/libuserlayer.pc

%files -n libsoftoff-dbus-devel
%_includedir/dbus-sdr/*.hpp
%_includedir/xyz/openbmc_project/Ipmi/Internal/SoftPowerOff/*.hpp
%_libdir/libsoftoff-dbus.so
%_pkgconfigdir/softoff-dbus.pc

%changelog
* Tue Aug 26 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt2.gita809fa5
- Downgraded to commit from revision list.

* Fri Aug 22 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.gitae30d81
- Initial build for Sisyphus.
