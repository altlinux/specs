Name: geeqie
Version: 1.1
Release: alt1

Summary: Graphics file browser utility
License: GPLv2+
Group: Graphics

Packager: Victor Forsiuk <force@altlinux.org>

Url: http://geeqie.sourceforge.net/
Source: http://download.sourceforge.net/geeqie/geeqie-%version.tar.gz

Patch: %name-1.1-alt-lfs.patch
Patch1: geeqie-1.0-libdir-fix.patch

# Automatically added by buildreq on Sat Jul 28 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gnome-doc-utils-xslt libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libstdc++-devel libwayland-client libwayland-server perl-XML-Parser pkg-config python-base shared-mime-info xml-common xml-utils xsltproc
BuildRequires: ImageMagick-tools doxygen exiftran exiv2 gcc-c++ gnome-doc-utils intltool libexiv2-devel libgtk+2-devel liblcms-devel liblirc-devel ufraw zenity

%description
Geeqie is a lightweight image viewer. It was forked from GQview. The development
is focused on features for photo collection maintenance: raw format, Exif/IPTC/XMP
metadata and integration with programs like UFraw, ImageMagick, Gimp, gPhoto or
ExifTool.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%autoreconf
%configure --enable-lirc --enable-largefile --with-readmedir=%_datadir/geeqie
%make_build

%install
mkdir -p %buildroot/usr/share/geeqie/html
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
* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1
- removed obsolete patches, more fixes for lfs

* Sat Jul 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt5
- rebuild

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
