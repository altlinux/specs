%def_enable snapshot

%define _name xf86-input-libinput
%define _xconfdir %_sysconfdir/X11/xorg.conf.d

Name: xorg-drv-libinput
Version: 0.14.0
Release: alt2

Summary: Xorg libinput input driver
Group: System/X11
License: MIT/X11
Url: http://www.x.org

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: ftp://ftp.x.org/pub/individual/driver/%_name-%version.tar.bz2
%endif
Patch: xf86-input-libinput-0.14.0-alt-include.patch
# fc
Source1: 99-libinput.conf

%define libinput_ver 1.0

PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Requires: libinput >= %libinput_ver
Requires: xkeyboard-config

BuildRequires(Pre): xorg-sdk >= 1.14
BuildRequires: libinput-devel >= %libinput_ver

%description
This is an X driver based on libinput. It is a thin wrapper around libinput,
so while it does provide all features that libinput supports it does little
beyond.

***WARNING: misconfiguration of an X input driver may leave you without
usable input devices in your X session. Use with caution.***

%package devel
Summary: Xorg libinput input driver development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Xorg libinput input driver development files.

%prep
%setup -n %_name-%version
%patch

%build
%autoreconf
%configure --disable-static \
	--with-xorg-module-dir=%_x11modulesdir
%make_build

%install
%makeinstall_std

install -d %buildroot%_xconfdir
install -p -m 0644 %SOURCE1 %buildroot%_xconfdir/90-libinput.conf

%files
%config(noreplace) %_xconfdir/90-libinput.conf
%_x11modulesdir/input/libinput_drv.so
%_man4dir/libinput.4*
%doc README.* COPYING

%exclude %_x11modulesdir/input/libinput_drv.la

%files devel
%_pkgconfigdir/xorg-libinput.pc
%_includedir/xorg/libinput-properties.h

%changelog
* Sat Sep 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt2
- updated to 0.14.0_6abd3412
- mv {90,99}-libinput.conf to overlap 95-input-keyboard.conf

* Mon Aug 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Sun Aug 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0_9563334

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- first build for Sisyphus

