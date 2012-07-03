Name: libsexy
Version: 0.1.11
Release: alt3.2

Summary: A library that does naughty things to good widgets
License: LGPL
Group: System/Libraries

Url: http://www.chipx86.com/wiki/Libsexy
Source: http://releases.chipx86.com/libsexy/libsexy/%name-%version.tar.bz2
Packager: Yuri N. Sedunov <aris@altlinux.org>

# Fedora patches
# patch for clipboard & color support in sexy-url-label
Patch: %name-0.1.11-url-label.patch
# patch that allows SexyIconEntry to support images using icon-name
Patch1: %name-0.1.11-icon-name.patch

BuildRequires: glib2-devel libenchant-devel libgtk+2-devel
BuildRequires: libxml2-devel pkg-config zlib-devel

%description
libsexy is a collection of GTK+ widgets that extend the functionality of
such standard widgets as GtkEntry and GtkLabel by subclassing them and
working around the limitations of the widgets.

%package devel
Summary: Files for developing applications that use %name
Requires: %name = %version
Group: Development/GNOME and GTK+

%description devel
The header file for developing applications that use
%name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+

%description devel-doc
API documentation for %name generated with gtk-doc.

%prep
%setup -q
%patch -p1 -b .url-label
%patch1 -p1 -b .icon-name

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt3.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt3.1
- Rebuilt for soname set-versions

* Sun May 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt3
- fixed build
- fedora patches

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.11-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsexy
  * postun_ldconfig for libsexy

* Tue Mar 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.1.11-alt2
- Real 0.1.11 release (fixes #14847).

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.1.11-alt1
- 0.1.11 release.
- Minor spec cleanup.

* Wed Sep 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.10-alt1
- Updated to 0.1.10

* Sun Apr 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.8-alt1
- Updated to 0.1.8
- Updated URL
- Added libsexy-devel-doc

* Wed Nov 16 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.4-alt1
- initial build

