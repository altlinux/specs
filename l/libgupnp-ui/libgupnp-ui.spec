%define oname gupnp-ui

Name: lib%oname
Version: 0.1.1
Release: alt2
Summary: GUPnP-UI is a collection of helpers for adding ui to upnp apps 

Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: http://www.gupnp.org/sources/bindings/%name-%version.tar
Patch0: %name-%version-%release.patch

%define gupnp_ver 0.3

BuildRequires: gtk-doc
BuildRequires: libgupnp-devel >= %gupnp_ver
BuildRequires: libgtk+2-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-UI is a collection of helpers for building user interface
application components for gupnp applications.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development package for %name

%package devel-doc
Summary: Development documentaion for gUPnP-UI
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides development documentations for gUPnP-UI.

%prep
%setup -q
%patch0 -p1

%build
gtkdocize
%autoreconf
glib-gettextize --force --copy
%configure --enable-maintainer-mode --disable-static --enable-gtk-doc
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README 
%_libdir/*.so.*

%files devel
%_libdir/*.so
%dir %_includedir/%oname-1.0
%_includedir/%oname-1.0/*
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt2
- rebuild with new libgupnp

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial release
