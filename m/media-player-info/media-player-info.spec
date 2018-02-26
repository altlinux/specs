Name:	 media-player-info
Version: 16
Release: alt1

License: BSD
Group:	 System/Configuration/Networking
Summary: Media player identification files

BuildArch: noarch
Url:	http://people.freedesktop.org/~teuf/media-player-info/
Source: http://people.freedesktop.org/~teuf/media-player-info/%name-%version.tar.gz

BuildRequires: libudev-devel

%description
media-player-info is a repository of data files describing media player
(mostly USB Mass Storage ones) capabilities. These files contain information
about the directory layout to use to add music to these devices, about the
supported file formats, and so on.

The music player capabilities are now described in *.mpi files (which are
ini-like files), together with udev rules to identify these devices.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc ChangeLog COPYING NEWS README
%_datadir/%name
/lib/udev/rules.d/*

%changelog
* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 16-alt1
- new version (ATL#27330)

* Sat Nov 28 2009 Mykola Grechukh <gns@altlinux.ru> 3-alt2
- buildreq fixed

* Wed Nov 25 2009 Mykola Grechukh <gns@altlinux.ru> 3-alt1
- initial build for ALT Linux
