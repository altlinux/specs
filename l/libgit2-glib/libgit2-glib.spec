%def_disable snapshot
%define ver_major 1.2
%define api_ver 1.0

%def_enable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable python
%def_enable ssh
%def_enable check

Name: libgit2-glib
Version: %ver_major.0
Release: alt1

Summary: Git library for GLib
Group: System/Libraries
License: LGPL-2.1
Url: https://live.gnome.org/Libgit2-glib

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define libgit2_ver 0.25
%define glib_ver 2.44

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel >= %glib_ver libgit2-devel >= %libgit2_ver
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_python:BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel}
%{?_enable_ssh:BuildRequires: libssh2-devel}

%description
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the Libgit2-glib library
Group: System/Libraries
Requires: %name = %EVR

%description gir
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package provides GObject introspection data for the Libgit2-glib library.

%package gir-devel
Summary: GObject introspection devel data for the Libgit2-glib library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package provides GObject introspection devel data for the Libgit2-glib library .

%package devel-doc
Summary: Development documentation for Libgit2-glib
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description devel-doc
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package contains documentation needed for developing Libgit2-glib applications.


%prep
%setup
# fix python install dir
sed -i 's/purelib/platlib/' %name/meson.build

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	%{?_disable_introspection:-Dintrospection=false} \
	%{?_disable_vala:-Dvapi=false} \
	%{?_disable_python:-Dpython=false} \
	%{?_disable_ssh:-Dssh=false}
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name-%api_ver.so.*
%{?_enable_python:%python3_sitelibdir/gi/overrides/*}
%doc AUTHORS COPYING NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%if_enabled vala
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-%api_ver.deps
%_vapidir/ggit-%api_ver.vapi
%_vapidir/ggit-%api_ver.deps
%endif

%if_enabled introspection
%files gir
%_typelibdir/Ggit-%api_ver.typelib

%files gir-devel
%_girdir/Ggit-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Sun Sep 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jul 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Dec 23 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.0.1-alt1
- updated to v1.0.0.1-1-gf745f88

* Fri Oct 30 2020 Yuri N. Sedunov <aris@altlinux.org> 0.99.0.1-alt1
- 0.99.0.1

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.28.0.1-alt1
- 0.28.0.1

* Wed Feb 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.27.8-alt1
- 0.27.8

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.7-alt1
- 0.27.7

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.4-alt1
- 0.26.4

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.2-alt1
- 0.26.2

* Sun Jul 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Wed Sep 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.4-alt1
- 0.24.4

* Thu Aug 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.3-alt1
- 0.24.3

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.10-alt1
- 0.23.10

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.8-alt1
- 0.23.8

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.6-alt1
- 0.23.6

* Fri Aug 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.8-alt1
- 0.22.8

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.6-alt1
- 0.22.6

* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.4-alt1
- 0.22.4

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.2-alt1
- 0.22.2

* Sun Jan 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.24-alt1
- 0.0.24

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.22-alt1
- 0.0.22

* Fri Jul 25 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.20-alt1
- 0.0.20

* Mon Jun 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.18-alt1
- 0.0.18

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.12-alt1
- 0.0.12

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- 0.0.6

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- first build for Sisyphus

