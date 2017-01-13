%define rname util-renderutil

Name: libxcb-render-util
Version: 0.3.9
Release: alt2.1

Group: System/Libraries
URL: http://xcb.freedesktop.org
Summary: Convenience functions for the Render extension
License: MIT

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Dec 10 2012 (-bi)
# optimized out: elfutils pkg-config python-base
#BuildRequires: doxygen glibc-devel-static libxcb-devel
BuildRequires: glibc-devel libxcb-devel
BuildRequires: libxcbutil-devel >= 0.3.8
BuildRequires: xorg-xproto-devel xorg-util-macros

%description
XCB util-renderutil module provides the following library:

  - renderutil: Convenience functions for the Render extension.

%package devel
Summary: Development and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development and header files for %name

%prep
%setup -n %rname-%version
install -m0644 altlinux/*.m4 m4/

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc README NEWS

%files devel
%_includedir/xcb/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jan 13 2017 Michael Shigorin <mike@altlinux.org> 0.3.9-alt2.1
- BOOTSTRAP: drop unused BR: doxygen

* Thu Oct 29 2015 Sergey V Turchin <zerg@altlinux.org> 0.3.9-alt2
- update to 0.3.9 release

* Mon Dec 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.9-alt1
- initial build
