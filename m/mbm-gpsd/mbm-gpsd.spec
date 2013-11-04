Summary: MBM GPS daemon
Name: mbm-gpsd
Version: 0.1.0
Release: alt1
License: GPLv2
Group: System/Servers
URL: git://mbm.git.sourceforge.net/gitroot/mbm/mbm-gpsd
Source0: %name-%version.tar.bz2
Patch0: mbm-gpsd.altlinux.patch

# Automatically added by buildreq on Mon Nov 04 2013
# optimized out: glib2-devel libdbus-devel libdbus-glib perl-XML-Parser pkg-config
BuildRequires: git-core glibc-devel-static gtk-doc intltool libdbus-glib-devel libnl1-devel libudev-devel ruby ruby-stdlibs zlib-devel

BuildRequires: rpm-macros-kde-common-devel libuuid-devel libnss-devel

%description
The  bm_gpsd  daemon  attempts to abstract the GPS functionality of MBM
devices so it behaves as more common GPS devices.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh --prefix=/usr --sysconfdir=/etc --localstatedir=/var --with-distro=altlinux
%make

%install
%makeinstall localstatedir=%buildroot/var DBUS_SYS_DIR=%buildroot/etc/dbus-1/system.d

%post

%preun

%files
%doc AUTHORS ChangeLog* NEWS README*
%dir %_runtimedir/MBM
%_initdir/*
%_sysconfdir/pm/sleep.d/*
%_sysconfdir/udev/rules.d/*
%_sysconfdir/dbus-1/system.d/
%_sysconfdir/mbm-gpsd.conf
%_bindir/*
%_sbindir/*
%_usr/lib/convert-conpro
%_datadir/PolicyKit/policy/*
%_K4dbus_sys_services/*
%_man8dir/*

%changelog
* Mon Nov 04 2013 Grigory Milev <week@altlinux.ru> 0.1.0-alt1
- Initial build for ALT Linux
