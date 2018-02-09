%def_disable snapshot

%define ver_major 1.1
%define api_ver 1.0

%def_enable docs
%def_enable introspection

Name: gcab
Version: %ver_major
Release: alt1

Summary: M$ Cabinet archive library and tool
Group: File tools
License: LGPLv2+
Url: https://wiki.gnome.org/msitools

#VCS: git://git.gnome.org/gcab
%if_disabled snapshot
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: lib%name = %version-%release

BuildRequires: meson git gtk-doc glib2-devel
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


%prep
%setup

%build
%meson \
	%{?_enable_docs:-Ddocs=true} \
	%{?_enable_introspection:-Dintrospection=true}
%meson_build

%install
%meson_install

%find_lang %name

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
%_vapidir/lib%name-%api_ver.vapi
%_vapidir/lib%name-%api_ver.deps

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name/

%files -n lib%name-gir
%_typelibdir/GCab-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GCab-%api_ver.gir

%changelog
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

