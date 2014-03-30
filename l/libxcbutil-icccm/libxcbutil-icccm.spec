Name: libxcbutil-icccm
Version: 0.4.1
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
BuildRequires: xorg-xproto-devel xorg-util-macros libxcbutil-proto

Provides: libxcbutil-ewmh = %version-%release

%description
XCB util-wm module provides the following libraries:

  - ewmh: Both client and window-manager helpers for EWMH.
  - icccm: Both client and window-manager helpers for ICCCM.

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
%configure --disable-static
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
* Sun Mar 30 2014 Terechkov Evgenii <evg@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Sep  5 2012 Terechkov Evgenii <evg@altlinux.org> 0.3.9-alt1
- Initial build for ALT Linux Sisyphus
