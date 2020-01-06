%def_disable snapshot

%define ver_major 1.4
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable docs
%def_enable introspection
%def_enable vala
%def_enable check
%def_enable installed_tests

Name: gcab
Version: %ver_major
Release: alt1

Summary: M$ Cabinet archive library and tool
Group: File tools
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/msitools

#VCS: git://git.gnome.org/gcab
%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: lib%name = %version-%release

BuildRequires(pre): meson
BuildRequires: git gtk-doc libgio-devel >= 2.62
BuildRequires: gobject-introspection-devel zlib-devel
BuildRequires: vala-tools

%description
gcab is a tool to manipulate Cabinet archive.

%package -n lib%name
Summary: Library to manipulate Cabinet archives
Group: System/Libraries

%description -n lib%name
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n lib%name-devel
Summary: Development files for gcab library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, needed to develop applications with the gcab library.

%package -n lib%name-devel-doc
Summary: Development documentation for gcab library
Group: Development/Documentation
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

This package contains development documentation for gcab library.

%package -n lib%name-gir
Summary: GObject introspection data for the gcab library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the gcab library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the gcab library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the gcab library

%package -n lib%name-tests
Summary: Tests for the GCab library
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-tests
This package provides tests programs that can be used to verify
the functionality of the installed M$ Cabinet archive library.



%prep
%setup

%build
%meson \
	%{?_enable_docs:-Ddocs=true} \
	%{?_disable_introspection:-Dintrospection=false} \
	%{?_disable_vala:-Dvapi=false} \
	%{?_enable_installed_tests:-Dinstalled_tests=true}
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %name.lang
%_bindir/%name
%_man1dir/%name.1*
%doc NEWS README*

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/lib%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/lib%name-%api_ver.pc
%if_enabled vala
%_vapidir/lib%name-%api_ver.vapi
%_vapidir/lib%name-%api_ver.deps
%endif

%if_enabled docs
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/GCab-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GCab-%api_ver.gir
%endif

%if_enabled installed_tests
%files -n lib%name-tests
%_libexecdir/installed-tests/lib%name-%api_ver/
%_datadir/installed-tests/lib%name-%api_ver/
%endif

%changelog
* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3
- %%check section, new libgcab-tests subpackage

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Tue Jan 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0 (fixed CVE-2018-5345)

* Thu Mar 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt2
- rebuilt for broken rpm-4.0.4-alt100.89

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Tue Mar 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Sat Mar 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt0.1
- 0.6 snapshot

* Mon Mar 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Sun Feb 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus

