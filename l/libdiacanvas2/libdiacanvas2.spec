%define realname diacanvas2
Name: libdiacanvas2
Version: 0.15.4
Release: alt3
Summary: Diagram widget for GTK+ 2.0
Group: System/Libraries
License: LGPL
Packager: Pavel Vainerman <pv@altlinux.ru>
Url: http://diacanvas.sourceforge.net
Source: %{realname}_%{version}.tar.gz
Patch: %name.patch

# Automatically added by buildreq on Sat Apr 07 2012
# optimized out: docbook-dtds docbook-style-xsl fontconfig fontconfig-devel glib2-devel libart_lgpl-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgfortran-devel libgio-devel libgnomecanvas-devel libgnomeprint-devel libgpg-error libgtk+2-devel libpango-devel libstdc++-devel libwayland-client libwayland-server libxml2-devel pkg-config xml-common xsltproc zlib-devel
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static gtk-doc indent libgnomeprintui-devel

%description
A diagram widget for GTK+-2.0 with a Visio look.
Development libs and headers are in %name-devel.

%package docs
Summary: Documentation for developing with %name
Group: Development/C
Requires: %name = %version-%release

%description docs
This package contains the documentation for
developing %name.

%package devel
Summary: DiaCanvas2 development libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries and header files for the support library for DiaCanvas2.

%package demo
Summary: DiaCanvas2 demo
Group: Development/C
Requires: %name = %version-%release

%description demo
Demo for DiaCanvas2.

%package python
Summary: DiaCanvas2 development libraries
Group: Development/C
Requires: %name = %version-%release

%description python
Python interface for DiaCanvas2.

%prep
%setup -q -n %realname-%version
%patch -p0

%build
%configure --enable-python=no --enable-gtk-doc
%make_build

%install
%makeinstall
%find_lang %name

mkdir -p $RPM_BUILD_ROOT%_docdir/gtk-doc
mv -f $RPM_BUILD_ROOT/usr/share/gtk-doc/* $RPM_BUILD_ROOT%_docdir/gtk-doc
#install -d -p -m755 $RPM_BUILD_ROOT%_bindir
#install -p -s -m755 demos/.libs/test-canvas $RPM_BUILD_ROOT%_bindir
(cd demos && make install)

# demos install
#mkdir -p $RPM_BUILD_ROOT%_docdir/%name-%version
#cp demos/.libs/test-canvas $RPM_BUILD_ROOT%_docdir/%name-%version
#cp demos/image.png $RPM_BUILD_ROOT%_docdir/%name-%version

%files
%_libdir/*.so*
%_datadir/locale/*/*

%files docs
%_docdir/gtk-doc/html/%realname

%files devel
%_includedir/*
%_libdir/pkgconfig/dia*

# %files python
# %_libdir/python2.2/site-packages/diacanvasmodule.so

#%files demo
#%_docdir/%name-%version

%changelog
* Sat Apr 07 2012 Pavel Vainerman <pv@altlinux.ru> 0.15.4-alt3
- update requires (again)

* Wed Apr 04 2012 Pavel Vainerman <pv@altlinux.ru> 0.15.4-alt2
- added patch for new glib.h
- update requires

* Sun Feb 20 2011 Pavel Vainerman <pv@altlinux.ru> 0.15.4-alt1
- new version (0.15.4)

* Mon Dec 21 2009 Pavel Vainerman <pv@altlinux.ru> 0.14.4-alt2
- fixed minor bug for rebuild with current gtkdoc

* Fri Oct 06 2006 Pavel Vainerman <pv@altlinux.ru> 0.14.4-alt1
- new version (0.14.4)
- disable python
- enable doc
- disable demo

* Tue Dec 14 2004 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt1
- first build
