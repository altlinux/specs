%define _libexecdir %_prefix/libexec
%add_python_req_skip synceconnector

Name: synce-connector
Version: 0.15.2
Release: alt1.1
Summary: Connection framework and dccm-implementation
Group: Communications
Packager: Mobile Development Team <mobile@packages.altlinux.org>
License: GPLv2
Url: http://www.synce.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: synce-serial
Obsoletes: synce-serial < 0.12
Provides: synce-dccm
Obsoletes: synce-dccm < 0.12
Obsoletes: synce-vdccm < 0.11
Provides: synce-hal
Obsoletes: synce-hal < 0.15.1

BuildPreReq: libsynce-devel >= 0.10.0
BuildPreReq: libgnet-devel
BuildPreReq: libdbus-glib-devel >= 0.60 libdbus-devel >= 0.60
BuildPreReq: libudev-devel libgudev-devel
BuildRequires: gcc-c++

%description
Synce-connector is a connection framework and dccm-implementation.
for Windows Mobile devices that integrates with HAL or udev.

%package bluez
Summary: Synce-connector for bluetooth connections
Group: Communications
Requires: %name = %version-%release

%description bluez
Synce-connector is a connection framework and dccm-implementation.
for Windows Mobile devices that integrates with HAL or udev.
This package for support a connection over bluetooth.

%prep
%setup -q
%patch -p1

%build
./autogen.sh
# ACLOCAL="aclocal -I m4" %autoreconf
%configure \
	--enable-udev \
	--enable-bluetooth-support \
	--with-hal-addon-dir=%_libexecdir
%make_build

%install
%make DESTDIR=%buildroot install
install -D etc/synce-connector.conf %buildroot%_sysconfdir/synce-connector.conf

%files
%doc AUTHORS ChangeLog COPYING README TODO
%config(noreplace) %_sysconfdir/synce-connector.conf
%config %_sysconfdir/dbus-1/system.d/*
%_datadir/dbus-1/system-services/org.synce.dccm.service
/lib/udev/rules.d/*
/lib/udev/synce-udev-*
%_bindir/*
%_libexecdir/*
%_datadir/%name

%files bluez
%config(noreplace) %_sysconfdir/ppp/ip-up.d/synce-udev-bt-ipup
%config(noreplace) %_sysconfdir/ppp/peers/synce-bt-peer

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.2-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- initial version based on synce-hal spec
