%define ver_major 3.2
%def_enable gtk_doc
%define webkit_api_ver 3.0
%define _name seed-gtk3

Name: seed
Version: %ver_major.0
Release: alt1

Summary: GObject JavaScriptCore bridge
License: LGPLv3+/GPLv3+
Group: Development/Other
Url: http://live.gnome.org/Seed

# git archive --format=tar --prefix=%name-%version/ --output=%name-%version.tar HEAD
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Provides: %_bindir/%name

Requires: lib%name = %version-%release

BuildRequires: libffi-devel
BuildRequires: gobject-introspection-devel >= 0.10.2
BuildRequires: gnome-js-common
BuildRequires: libcairo-devel
BuildRequires: libgtk+3-devel
BuildRequires: libjavascriptcoregtk3-devel >= 1.5.90
BuildRequires: libreadline-devel
BuildRequires: libsqlite3-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libmpfr-devel
BuildRequires: libxml2-devel
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: gnome-common

# for tests
# BuildRequires: libgtk+3-gir

%description
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

%package -n lib%name
Group: System/Libraries
Summary: GObject JavaScriptCore bridge - shared library
Provides: lib%_name = %version-%release

%description -n lib%name
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

%package -n lib%name-devel
Summary: Development files for GObject JavaScriptCore bridge 
Group: Development/C
Provides: lib%_name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

This package provides development headers and libraries for Seed

%package -n lib%name-devel-doc
Summary: Development documentation for GObject JavaScriptCore bridge 
Group: Development/C
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

This package provides development documentation for Seed

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q
# install documentation in proper location
find doc -name "Makefile*" -print0|xargs -r0 subst 's@\$(datadir)/doc/seed@%pkgdocdir@' --

# since 2.29.91 m4 directory not used
subst '/ACLOCAL_AMFLAGS = -I m4/d' Makefile.am

rm -f seed.pc

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-webkit=%webkit_api_ver

%make_build

%install
%make DESTDIR=%buildroot install

#%check
#%make check

%files
%_bindir/%name
%_datadir/%_name
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%files -n lib%name
%_libdir/lib%_name.so.*
%dir %_libdir/%_name
%_libdir/%_name/libseed_cairo.so
%_libdir/%_name/libseed_canvas.so
%_libdir/%_name/libseed_dbusnative.so
%_libdir/%_name/libseed_DynamicObject.so
%_libdir/%_name/libseed_example.so
%_libdir/%_name/libseed_ffi.so
%_libdir/%_name/libseed_gettext.so
%_libdir/%_name/libseed_gtkbuilder.so
%_libdir/%_name/libseed_libxml.so
%_libdir/%_name/libseed_mpfr.so
%_libdir/%_name/libseed_multiprocessing.so
%_libdir/%_name/libseed_os.so
%_libdir/%_name/libseed_readline.so
%_libdir/%_name/libseed_sandbox.so
%_libdir/%_name/libseed_sqlite.so
%exclude %_libdir/%_name/*.la

%files -n lib%name-devel
%_libdir/lib%_name.so
%_includedir/%_name
%_libdir/pkgconfig/%name.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name

%changelog
* Thu Sep 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Sep 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1 git snapshot

* Sat Apr 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.90-alt1
- 2.91.90

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91.1-alt1
- build of current snapshot

* Wed Sep 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.5-alt1
- 2.31.5

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.1-alt2
- rebuild against libffi.so.5

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.1-alt1
- 2.31.1

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91.1-alt1
- 2.29.91.1

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Fri Jan 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5.2-alt1
- 2.29.5.2
- properly linked modules

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5.1-alt1
- 2.29.5.1

* Wed Dec 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- first build for sisyphus

