%define _name gssdp
%define ver_major 1.2
%define api_ver 1.2

%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_disable sniffer
%def_enable check

Name: lib%_name%ver_major
Version: %ver_major.2
Release: alt1

Summary: Resource discovery and announcement over SSDP
Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires(pre): meson rpm-build-gir
BuildRequires: gtk-doc libsoup-devel >= 2.26.1 libgio-devel >= 2.54
BuildRequires: vala-tools rpm-build-vala libvala-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libsoup-gir-devel}
%{?_enable_sniffer:BuildRequires: libgtk+3-devel >= 3.12}

%description
GSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.

%package devel
Summary: Development files for gSSDP library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files for development with gSSDP.

%package devel-doc
Summary: Development documentation for gSSDP
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
gSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.

This package provides development documentation for gSSDP.

%package gir
Summary: GObject introspection data for the  library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the  library

%package gir-devel
Summary: GObject introspection devel data for the  library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GSSDP library

%package -n %_name%ver_major-tools
Summary: Graphical SSDP sniffer
Group: Networking/Other
Requires: %name = %version-%release

%description -n %_name%ver_major-tools
A Device Sniffer tool based on GSSDP framework.

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_disable_sniffer:-Dsniffer=false}
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_libdir/lib%_name-%api_ver.so.*
%doc AUTHORS README NEWS ChangeLog

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name
%endif

%if_enabled introspection
%files gir
%_typelibdir/GSSDP-%api_ver.typelib

%files gir-devel
%_girdir/GSSDP-%api_ver.gir
%endif

%if_enabled sniffer
%files -n %_name%ver_major-tools
%_bindir/%_name-device-sniffer
%endif


%changelog
* Thu Jan 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Jan 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3 (ported to Meson build system)
- new gssdp-tools subpackage
- %%check section

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1.1
- NMU: Rebuilt for e2k.

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Oct 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.14.16-alt1
- 0.14.16

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.14.15-alt1
- 0.14.15

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.14.14-alt1
- 0.14.14

* Wed Jan 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.14.13-alt1
- 0.14.13

* Wed Dec 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.12.1-alt1
- 0.14.12.1

* Wed Nov 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.12-alt1
- 0.14.12

* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.11-alt1
- 0.4.11

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.10-alt1
- 0.14.10

* Sat Jul 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.9-alt1
- 0.14.9

* Mon May 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.8-alt1
- 0.14.8

* Mon Feb 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.7-alt1
- 0.14.7

* Thu Oct 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.6-alt1
- 0.14.6

* Tue Sep 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.5-alt1
- 0.14.5

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.4-alt1
- 0.14.4

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.13.2-alt1
- 0.13.2
- update BR:
- add --without-gtk to configure

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.2.1-alt1
- 0.12.2.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt2
- used %%autoreconf to fix RPATH problem

* Fri Dec 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Tue May 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sun Nov 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt2
- rebuild for update dependencies

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2
- introspection support

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
 0.7.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- first build for Sisyphus

