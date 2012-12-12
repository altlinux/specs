%define _name gssdp

%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: lib%_name
Version: 0.13.2
Release: alt1

Summary: Resource discovery and announcement over SSDP
Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/

Source: http://www.gupnp.org/sources/%_name/%_name-%version.tar.xz

BuildRequires: gtk-doc libsoup-devel >= 2.26.1 glib2-devel >= 2.22 libgio-devel >= 2.22
BuildRequires: vala-tools rpm-build-vala libvala-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel}

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
Group: Development/C
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

%prep
%setup -q -n %_name-%version

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure  --disable-static \
	    --without-gtk \
	    %{?_enable_gtk_doc:--enable-gtk-doc} \
	    %{subst_enable introspection}

%make_build

%install
%make  DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS README NEWS ChangeLog

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_vapidir/*.deps
%_vapidir/*.vapi

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif


%changelog
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

