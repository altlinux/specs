Name: libxcbutil-keysyms
Version: 0.3.9
Release: alt1
Summary: Standard X key constants and keycodes conversion on top of libxcb
License: MIT
Group: System/Libraries
URL: http://xcb.freedesktop.org
Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar
Source1: m4.tar
Patch: %name-%version-%release.patch

BuildRequires: libxcbutil-devel >= 0.3.8
BuildRequires: xorg-xproto-devel xorg-util-macros

%description
XCB util-keysyms module provides the following library:

  - keysyms: Standard X key constants and conversion to/from keycodes.

%package devel
Summary: Development and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development and header files for %name

%prep
%setup -q -a1

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
* Wed Sep  5 2012 Terechkov Evgenii <evg@altlinux.org> 0.3.9-alt1
- Initial build for ALT Linux Sisyphus
