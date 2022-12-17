%define _name gupnp
%define ver_major 1.6
%define api_ver 1.6

%def_disable static
%def_enable gtk_doc
%def_enable man
%def_enable introspection
%def_enable vala
# context and acl failed in hasher
%def_disable check

Name: lib%_name%api_ver
Version: %ver_major.3
Release: alt1

Summary: A framework for creating UPnP devices and control points
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.gupnp.org/

Vcs: https://gitlab.gnome.org/GNOME/gupnp.git
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define meson_ver 0.54
%define glib_ver 2.69
%define gssdp_ver 1.6.2
%define soup_api_ver 3.0
%define soup_ver 3.0.6

BuildRequires(pre): rpm-macros-meson >= %meson_ver rpm-build-gir rpm-build-python3
BuildRequires: meson libgio-devel >= %glib_ver libgssdp%api_ver-devel >= %gssdp_ver
BuildRequires: libxml2-devel libsoup%soup_api_ver-devel >= %soup_ver libuuid-devel
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libsoup%soup_api_ver-gir-devel
BuildRequires: libgssdp%api_ver-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc gi-docgen}
%{?_enable_man:BuildRequires: xsltproc docbook-style-xsl}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development files and libraries for gUPnP
Group: Development/C
Requires: %name = %version-%release

%description devel
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

This package provides files for development with gUPnP.

%package devel-doc
Summary: Development documentaion for gUPnP
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

This package provides development documentations for gUPnP.

%package gir
Summary: GObject introspection data for the gUPnP library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the gUPnP library

%package gir-devel
Summary: GObject introspection devel data for the gUPnP library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the gUPnP library


%prep
%setup -n %_name-%version
# fix manpage building
sed -i '/\--nowrite/d' doc/meson.build

%build
%meson \
%{?_enable_gtk_doc:-Dgtk_doc=true} \
%{?_disable_introspection:-Dintrospection=false} \
%{?_disable_vala:-Dvapi=false}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%_name-binding-tool-%api_ver
%_libdir/lib%_name-%api_ver.so.*
%{?_enable_man:%_man1dir/%_name-binding-tool*.1*}
%doc AUTHORS README* NEWS

%files devel
%_pkgconfigdir/%_name-%api_ver.pc
%_libdir/lib%_name-%api_ver.so
%_includedir/%_name-%api_ver/
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/GUPnP-%api_ver.typelib

%files gir-devel
%_girdir/GUPnP-%api_ver.gir
%endif


%changelog
* Sat Dec 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Mon Nov 21 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Sun Aug 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Mon Jul 04 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Fri Jun 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Mon Apr 25 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0 (1.2 -> 1.6 API, ported to Soup-3)

* Thu Jan 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sat Jan 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Mon Dec 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Aug 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Mon Jul 05 2021 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Jun 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.7-alt1
- 1.2.7

* Mon May 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt2
- BR: +rpm-build-python3

* Mon Aug 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Tue Jun 23 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3 (Add mitigations for CVE-2020-12695 (CallStranger),
  Implement UDA 2.0 April 17 2020 Addendum (Partial fix for CVE-2020-12695))

* Thu Jan 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Oct 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20.18-alt1
- 0.20.18

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20.17-alt1
- 0.20.17

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20.16-alt1
- 0.20.16

* Wed Jan 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20.15-alt1
- 0.20.15

* Sun May 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.20.14-alt1
- 0.20.14

* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 0.20.13-alt1
- 0.20.13

* Sun Jun 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.12-alt1
- 0.20.12

* Mon Feb 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.10-alt1
- 0.20.10

* Sat Dec 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.9-alt1
- 0.20.9

* Thu Oct 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.8-alt1
- 0.20.8

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.7-alt1
- 0.20.7

* Tue Sep 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.6-alt1
- 0.20.6

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.5-alt1
- 0.20.5

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.19.3-alt1
- 0.19.3

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.4-alt1
- 0.18.4

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Sat Mar 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Dec 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Tue May 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Nov 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt2
- rebuild for update dependencies

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3
- introspection support

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Tue Nov 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Wed Jun 24 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- new version (closes #20468)

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- new version

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- first build for Sisyphus

