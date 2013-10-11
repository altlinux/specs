%define ver_major 1.9
%define _libexecdir %_prefix/libexec

Name: cinnamon-bluetooth
Version: %ver_major.0
Release: alt3

Summary: The Cinnamon Bluetooth Subsystem
License: GPLv2/LGPLv2
Group: System/Libraries
Url: https://github.com/linuxmint/cinnamon-bluetooth

Requires: bluez obex-data-server obexd rfkill libgnome-bluetooth-gir
Requires: %name-translations

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gnome-common intltool yelp-tools itstool
BuildRequires: libgio-devel libgtk+3-devel libnotify-devel libXi-devel libdbus-glib-devel glib2-devel
BuildRequires: cinnamon-control-center-devel 
BuildRequires: libgnome-bluetooth-devel

%description
The Cinnamon Bluetooth Subsystem

%package -n %name-panel
Summary: The Cinnamon Bluetooth panel for cinnamon-control-center
Group: System/Libraries
Requires: cinnamon-control-center
Requires: %name = %version-%release

%description -n %name-panel
The Cinnamon Bluetooth panel for cinnamon-control-center

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot -name "*.la" -delete

%files
%doc AUTHORS README 
%_desktopdir/*.desktop
%_datadir/%name
%_datadir/cinnamon/applets/*

%files -n %name-panel
%_libdir/cinnamon-control-center-1/panels/libbluetooth.so

%changelog
* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt3
- remove ObexFTP file browsing

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- add dependence on translations

* Fri Aug 30 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- Initial build
