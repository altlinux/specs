%define origname gtkimageview
%define _gtk_docdir %_datadir/gtk-doc/html

Name: lib%origname
Version: 1.6.4
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: GtkImageView is a simple image viewer widget for GTK
License: LGPLv2+
Group: System/Libraries

Url: http://trac.bjourne.webfactional.com/
Source0: gtkimageview-%version.tar.gz

# Automatically added by buildreq on Mon Nov 03 2008
BuildRequires: libgtk+2-devel

%description
GtkImageView is a simple image viewer widget for GTK. Similar to the
image viewer panes in gThumb or Eye of Gnome.

%package devel
Summary: Files to compile applications that use GtkImageView
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the files required to develop applications
using GtkImageView widget.

%package devel-doc
Summary: Development documentation for GtkImageView
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release
BuildArch: noarch

%description devel-doc
GtkImageView Reference Manual.

%prep
%setup -n %origname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-doc
%_gtk_docdir/*

%changelog
* Wed Nov 10 2010 Victor Forsiuk <force@altlinux.org> 1.6.4-alt2
- Rebuilt for soname set-versions.

* Wed Aug 12 2009 Victor Forsyuk <force@altlinux.org> 1.6.4-alt1
- 1.6.4

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.6.3-alt1
- 1.6.3

* Mon Nov 03 2008 Victor Forsyuk <force@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 1.5.0-alt1
- 1.5.0

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Aug 01 2007 Victor Forsyuk <force@altlinux.org> 1.3.0-alt1
- Initial build.
