Summary: MBM GPS control software
Name: mbm-gps-control
Version: 0.1.0
Release: alt2
License: GPLv2
Group: System/Servers
URL: git://mbm.git.sourceforge.net/gitroot/mbm/mbm-gps-control
Source0: %name-%version.tar.bz2
Patch0: mbm-gps-control.altlinux.patch

# Automatically added by buildreq on Tue Nov 05 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server perl-XML-Parser pkg-config
BuildRequires: glibc-devel-static intltool libGConf-devel libdbus-glib-devel libgtk+2-devel ruby ruby-stdlibs

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
%make install DESTDIR=%buildroot localstatedir=%buildroot/var DBUS_SYS_DIR=%buildroot/etc/dbus-1/system.d

%find_lang --output=%name.lang %name

%post

%preun

%files -f %name.lang
%doc AUTHORS ChangeLog* NEWS README*
%_datadir/%name
%_bindir/*
%_desktopdir/*
%_datadir/%name/*

%changelog
* Mon Oct 14 2019 Grigory Milev <week@altlinux.ru> 0.1.0-alt2
- Fix build with latest versions of the gtk+2

* Mon Nov 04 2013 Grigory Milev <week@altlinux.ru> 0.1.0-alt1
- Initial build for ALT Linux
