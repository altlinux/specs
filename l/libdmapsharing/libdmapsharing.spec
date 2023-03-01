%def_disable snapshot
%define api_ver 3.0

%def_disable vala

Name: libdmapsharing
Version: 2.9.42
Release: alt1

Summary: A DMAP client and server library
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.flyn.org/projects/libdmapsharing/

%if_disabled snapshot
Source: http://www.flyn.org/projects/libdmapsharing/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-build-gir
BuildRequires: gtk-doc libgdk-pixbuf-devel libsoup-devel >= 2.48
BuildRequires: gst-plugins1.0-devel libavahi-glib-devel zlib-devel
BuildRequires: gobject-introspection-devel libsoup-gir-devel
BuildRequires: libgtk+2-devel libgee0.8-devel
BuildRequires: libcheck-devel
%{?_enable_vala:BuildRequires: vala-tools}

%description
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package devel
Summary: Files needed to develop applications using libdmapsharing
Group: Development/C
Requires: %name = %version-%release

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
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name.

%prep
%setup
%{?_enable_snapshot:touch ChangeLog}

%build
%{?_disable_vala:export ac_cv_path_VALAC=""}
%{?_enable_snapshot:%autoreconf}
%add_optflags %optflags_shared
%configure --disable-static

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name-%api_ver.so.*
%doc AUTHORS ChangeLog README

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.vapi}

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/

%files gir
%_typelibdir/DMAP-%api_ver.typelib

%files gir-devel
%_girdir/DMAP-%api_ver.gir

%changelog
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

