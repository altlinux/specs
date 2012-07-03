Name: libgusb
Version: 0.1.3
Release: alt1

Summary: GLib wrapper around libusb1
Group: System/Libraries
License: LGPLv2+
Url: https://gitorious.org/gusb/
Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz

BuildRequires: libgio-devel >= 2.16.1 libgudev-devel libusb-devel

%description
GUsb is a GObject wrapper for libusb that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package devel
Summary: Libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
GLib headers and libraries for the GUsb library.

%package devel-doc
Summary: Development documentation for GUsb
Group: Development/C
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package provides documentation for developing
applications that use GUsb library.


%prep
%setup

%build
%configure \
        --disable-static \
        --disable-dependency-tracking

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/libgusb.so.*
%doc README AUTHORS NEWS

%files devel
%_includedir/gusb-1/
%_libdir/libgusb.so
%_libdir/pkgconfig/gusb.pc

%files devel-doc
%_datadir/gtk-doc/html/gusb/

%changelog
* Thu Jan 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- adapted for Sisyphus

* Mon Dec 05 2011 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream version
- Add a missing error enum value

* Fri Nov 11 2011 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream version
- Ignore EBUSY when trying to detach a detached kernel driver

* Tue Nov 01 2011 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream version

* Thu Sep 15 2011 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial version for Fedora package review
