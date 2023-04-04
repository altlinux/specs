%def_disable snapshot

%define _name libdmapsharing
%define api_ver 4.0

%def_enable vala
# broken coverage tests
%def_disable check

Name: %_name%api_ver
Version: 3.9.12
Release: alt1

Summary: A DMAP client and server library (4.0 API)
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.flyn.org/projects/libdmapsharing/

%if_disabled snapshot
Source: http://www.flyn.org/projects/libdmapsharing/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/GNOME/libdmapsharing.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.66
%define soup_api_ver 3.0
%define gst_ver 1.22

BuildRequires(pre): rpm-build-gir
BuildRequires: gtk-doc libgdk-pixbuf-devel libsoup%soup_api_ver-devel >= 3.0.0
BuildRequires: gst-plugins1.0-devel >= %gst_ver libavahi-glib-devel zlib-devel
BuildRequires: gobject-introspection-devel libsoup%soup_api_ver-gir-devel gst-plugins1.0-gir-devel
BuildRequires: libgtk+3-devel libgee0.8-devel
BuildRequires: libcheck-devel
%{?_enable_vala:BuildRequires: vala-tools}

%description
libdmapsharing implements the DMAP protocols. This includes support for
DAAP, DPAP & DACP.

%package devel
Summary: Files needed to develop applications using libdmapsharing
Group: Development/C
Requires: %name = %EVR

%description devel
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

This package contains development documentation for the %name library.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %name.

%prep
%setup -n %_name-%version
%{?_enable_snapshot:touch ChangeLog}

%build
%{?_enable_snapshot:%autoreconf}
%add_optflags %optflags_shared
%configure --disable-static \
    --disable-coverage
%nil
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%_name-%api_ver.so.*
%doc AUTHORS ChangeLog README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.vapi}

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/

%files gir
%_typelibdir/Dmap-%api_ver.typelib

%files gir-devel
%_girdir/Dmap-%api_ver.gir

%changelog
* Tue Apr 04 2023 Yuri N. Sedunov <aris@altlinux.org> 3.9.12-alt1
- 3.9.12 (3.0 -> 4.0)

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 2.9.42-alt1
- 2.9.42

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.9.39-alt2
- disabled vapi rebuild

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.39-alt1
- 2.9.39

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.38-alt1
- 2.9.38

* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 2.9.37-alt1
- 2.9.37

* Mon Aug 01 2016 Yuri N. Sedunov <aris@altlinux.org> 2.9.36-alt1
- 2.9.36

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.9.34-alt1
- 2.9.34

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.32-alt1
- 2.9.32

* Mon Jun 01 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.31-alt1
- 2.9.31

* Sun Feb 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.30-alt1
- 2.9.30

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 2.9.29-alt1
- 2.9.29
- new -gir{,-devel} subpackages

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 2.9.25-alt1
- 2.9.25

* Fri Nov 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.9.24-alt1
- 2.9.24

* Sun Oct 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.9.23-alt1
- 2.9.23
- spec cleanup
- updated buildrqs
- new -devel-doc subpackage

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.9.18-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.9.18-alt1_2
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.9.18-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt1_1
- initial import by fcimport

