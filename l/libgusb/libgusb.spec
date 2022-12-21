%define api_ver 1.0

%def_enable tests
%def_enable docs
%def_enable introspection
%def_enable vala
# gusb-self-test failed in hasher
# libgusb:ERROR:../gusb/gusb-self-test.c:83:gusb_context_func: assertion failed (array->len > 0): (0 > 0)
%def_disable check

Name: libgusb
Version: 0.4.3
Release: alt1

Summary: GLib wrapper around libusb1
Group: System/Libraries
License: LGPL-2.1+
Url: https://gitorious.org/gusb/

Vcs: https://github.com/hughsie/libgusb.git
#Source: https://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz
Source: https://github.com/hughsie/libgusb/archive/%version/%name-%version.tar.gz

Requires: usbids

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson libgio-devel >= 2.44 libusb-devel >= 1.0.22
BuildRequires: libjson-glib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libjson-glib-gir-devel}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_vala:
BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_tests:BuildRequires: libumockdev-devel usbids}

%description
GUsb is a GObject wrapper for libusb that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package devel
Summary: Libraries and headers for %name
Group: Development/C
Requires: %name = %EVR

%description devel
GLib headers and libraries for the GUsb library.

%package gir
Summary: GObject introspection data for GUsb
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the GUsb library.

%package gir-devel
Summary: GObject introspection devel data for GUsb
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

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
%meson \
	-Dusb_ids=%_datadir/misc/usb.ids \
        %{?_disable_docs:-Ddocs=false} \
        %{?_disable_tests:-Dtests=false} \
	%{?_disable_introspection:-Dintrospection=false} \
        %{?_disable_vala:-Dvapi=false}
%meson_build

%install
%meson_install

%check
%__meson_test -v --print-errorlogs

%files
%_libdir/%name.so.*
%doc README* AUTHORS NEWS

%files devel
%_bindir/gusbcmd
%_includedir/gusb-1/
%_libdir/%name.so
%_pkgconfigdir/gusb.pc
%{?_enable_vala:%_vapidir/gusb.*}

%if_enabled introspection
%files gir
%_typelibdir/GUsb-%api_ver.typelib

%files gir-devel
%_girdir/GUsb-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/%name/
%endif

%changelog
* Wed Dec 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Wed Oct 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sun Oct 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Sep 13 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Wed Dec 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Thu Oct 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Wed May 26 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Fri Jul 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sat Feb 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Tue Jan 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1
- updated License tag

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.11-alt1
- 0.2.11

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10

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
