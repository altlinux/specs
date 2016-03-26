%define api_ver 1.0

Name: libgusb
Version: 0.2.9
Release: alt1

Summary: GLib wrapper around libusb1
Group: System/Libraries
License: LGPLv2+
Url: https://gitorious.org/gusb/
Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz

BuildRequires: libgio-devel >= 2.38 libusb-devel >= 1.0.19
BuildRequires: gobject-introspection-devel vala-tools gtk-doc

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

%package gir
Summary: GObject introspection data for GUsb
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GUsb library.

%package gir-devel
Summary: GObject introspection devel data for GUsb
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GUsb library.

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
        --disable-dependency-tracking \
        --enable-tests

%make_build

%install
%makeinstall_std

%check
# failed to init libusb in hasher
#%%make check

%files
%_libdir/libgusb.so.*
%doc README AUTHORS NEWS

%files devel
%_bindir/gusbcmd
%_includedir/gusb-1/
%_libdir/libgusb.so
%_libdir/pkgconfig/gusb.pc
%_vapidir/gusb.vapi

%files gir
%_typelibdir/GUsb-%api_ver.typelib

%files gir-devel
%_girdir/GUsb-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/gusb/

%changelog
* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Sat Dec 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Thu Jul 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Mon Jun 01 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Thu Nov 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Sun Nov 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Sun Jan 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4
- new -gir{,-devel} subpackages
- added Vala bindings to -devel subpackage

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
