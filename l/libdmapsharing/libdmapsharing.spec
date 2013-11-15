%define api_ver 3.0

Name: libdmapsharing
Version: 2.9.24
Release: alt1

Summary: A DMAP client and server library
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.flyn.org/projects/libdmapsharing/

Source: http://www.flyn.org/projects/libdmapsharing/%name-%version.tar.gz

BuildRequires: gtk-doc libgdk-pixbuf-devel libsoup-devel >= 2.32
BuildRequires: gst-plugins1.0-devel libavahi-glib-devel zlib-devel
# for dpapview and tests if maintainer mode enabled
#BuildRequires: vala-tools libgtk+2-devel libgee0.8-devel libcheck-devel

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

%prep
%setup

%build
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
%_libdir/pkgconfig/%name-%api_ver.pc
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/


%changelog
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

