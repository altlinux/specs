Name: geeqie
Version: 1.0
Release: alt4

Summary: Graphics file browser utility
License: GPLv2+
Group: Graphics

Packager: Victor Forsiuk <force@altlinux.org>

Url: http://geeqie.sourceforge.net/
Source: http://download.sourceforge.net/geeqie/geeqie-%version.tar.gz

Patch1: geeqie-1.0-libdir-fix.patch
Patch2: geeqie-1.0-largefile.patch

# Automatically added by buildreq on Thu Oct 21 2010
BuildRequires: doxygen gcc-c++ gnome-doc-utils graphviz intltool libexiv2-devel libgtk+2-devel liblcms-devel liblirc-devel perl-Encode-CN

%description
Geeqie is a lightweight image viewer. It was forked from GQview. The development
is focused on features for photo collection maintenance: raw format, Exif/IPTC/XMP
metadata and integration with programs like UFraw, ImageMagick, Gimp, gPhoto or
ExifTool.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --enable-lirc --enable-largefile --with-readmedir=%_datadir/geeqie
%make_build

%install
%makeinstall_std
install -pD -m644 geeqie.png %buildroot%_liconsdir/geeqie.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/geeqie
%_libdir/geeqie
%_desktopdir/*
%_pixmapsdir/*
%_liconsdir/*
%_man1dir/*

%changelog
* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt4
- rebuilt against libexiv2.so.11

* Thu Oct 21 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt3
- Patch to use arch-specific libdir instead of hardcoded /usr/lib.

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt2
- 1.0

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.0-alt1.beta2
- Rebuild with libexiv2.so.6.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta2
- 1.0 beta2.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta1
- 1.0 beta1.

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha2
- Update to 1.0 alpha2 and build with LIRC support.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt0.alpha1.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha1
- Initial build.
