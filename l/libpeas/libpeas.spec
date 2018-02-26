%define ver_major 1.4
%define api_ver 1.0
%define gtk_api_ver 3.0

%def_enable js
%def_enable gjs
%def_enable vala
%def_enable gtk_doc

Name: libpeas
Version: %ver_major.1
Release: alt1

Summary: A gobject-based plugins engine
Group: System/Libraries
License: LGPLv2+
Url: ftp://ftp.gnome.org/pub/gnome/sources/%name/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar

BuildRequires: gnome-common intltool gtk-doc libgtk+3-devel gobject-introspection-devel >= 1.31.10 libgtk+3-gir-devel
# for python support
BuildRequires: python-module-pygobject3-devel >= 3.1.1
# for Javascript support
%{?_enable_js:BuildRequires: libseed-devel >= 3.2.0}
%{?_enable_gjs:BuildRequires: libgjs-devel >= 1.31.11}
%{?_enable_vala:BuildRequires: vala-tools >= 0.14}

%description
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

%package python-loader
Summary: Python loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description python-loader
This package provides Python loader for %name

%package js-loader
Summary: Javascript loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description js-loader
This package provides WebKit Javascript loader for %name

%package gjs-loader
Summary: Javascript loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gjs-loader
This package provides MozJS Javascript loader for %name

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package devel-doc
Summary: Development documentation for the %name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

This package contains development documentation for the %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/C
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name

%package demo
Summary: %name demonstration program
Group: Development/C
Requires: %name = %version-%release

%description demo
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

This package contains %name demonstration programs

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable vala} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libdir/%{name}*-%api_ver.so.*
%dir %_libdir/%name-%api_ver/loaders
#%_libdir/%name-%api_ver/loaders/libcloader.so
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS README

%files python-loader
%_libdir/%name-%api_ver/loaders/libpythonloader.so

%if_enabled js
%files js-loader
%_libdir/%name-%api_ver/loaders/libseedloader.so
%endif

%if_enabled gjs
%files gjs-loader
%_libdir/%name-%api_ver/loaders/libgjsloader.so
%endif

%files devel
%_libdir/%{name}*-%api_ver.so
%_includedir/%name-%api_ver/
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%files demo
%_bindir/peas-demo
%_libdir/peas-demo/

%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*

%exclude %_libdir/%name-%api_ver/loaders/*.la


%changelog
* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1 snapshot

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Mon Aug 23 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Tue Jul 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- first build for sisyphus

