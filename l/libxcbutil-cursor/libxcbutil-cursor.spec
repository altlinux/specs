Name: libxcbutil-cursor
Version: 0.1.3
Release: alt1
Summary: Client and window-manager helper library on top of libxcb
License: MIT
Group: System/Libraries
URL: http://xcb.freedesktop.org
Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar
Source1: m4.tar
Patch: %name-%version-%release.patch

BuildRequires: libxcbutil-devel >= 0.3.8
BuildRequires: xorg-xproto-devel xorg-util-macros libxcbutil-proto libxcb-render-util-devel libxcbutil-image-devel gperf

%description
XCB util-cursor module provides the following libraries:

  - cursor: port of libxcursor

%package devel
Summary: Development and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development and header files for %name

%prep
%setup -a1

%build
%autoreconf
%configure --disable-static --with-cursorpath="~/.icons:/usr/share/icons:/usr/share/pixmaps"
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc README NEWS

%files devel
%_includedir/xcb/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1
- new version

* Fri Oct 30 2015 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- new version

* Sat Dec 21 2013 Terechkov Evgenii <evg@altlinux.org> 0.1.1-alt1
- Initial build for ALT Linux Sisyphus
