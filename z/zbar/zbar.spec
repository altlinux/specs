%set_automake_version 1.11

Name: zbar
Version: 0.10
Release: alt7.qa1
%define libname libzbar

Summary: A library for scanning and decoding bar codes

Group: Graphics
License: GPLv2
Url: http://zbar.sourceforge.net/
Source: %name-%version.tar
Patch1: 0001-Description-Linux-2.6.38-and-later-do-not-support-th.patch
Patch2: python-zbar-import-fix-am.patch

# Automatically added by buildreq on Thu Apr 04 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libICE-devel libSM-devel libX11-devel libXext-devel libXv-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libqt4-core libqt4-devel libqt4-gui libstdc++-devel pkg-config python-base python-devel python-module-distribute python-module-pygobject-devel python-modules python-modules-compiler xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ libImageMagick-devel libv4l-devel python-module-pygtk-devel

BuildRequires: libqt4-devel

%description
Zbar is the utils and library for scanning and decoding bar codes from
various sources such as video streams, image files or raw intensity
sensors. It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5.
Included with the library are basic applications for decoding
captured bar code images and using a video device (eg, webcam) as a
bar code scanner. The flexible, layered architecture features a fast,
streaming interface with a minimal memory footprint.

%package -n %libname
Group: Development/C++
Summary: Bar code library files

%description -n %libname
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of
5. Included with the library are basic applications for decoding
captured bar code images and using a video device (eg, webcam) as a
bar code scanner.

%package -n %libname-devel
Group: Development/C++
Summary: Bar code library extra development files
Requires: %libname = %version

%description -n %libname-devel
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional libraries used for
developing applications that read bar codes with this library.

%package -n %libname-devel-static
Group: Development/C++
Summary: Bar code library extra development files and static libraries
Requires: %libname = %version

%description -n %libname-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains additional static libraries used for
developing applications that read bar codes with this library.

%package -n %libname-gtk
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK widget
Requires: %libname = %version

%description -n %libname-gtk
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use with GUI
applications based on GTK+-2.0.

%package -n %libname-gtk-devel
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK widget extra development files
Requires: %libname-gtk = %version, %libname-devel = %version

%description -n %libname-gtk-devel
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional libraries used for
developing GUI applications based on GTK+-2.0 that include a bar code
scanning widget.

%package -n %libname-gtk-devel-static
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK widget extra development files and static libraries
Requires: %libname-gtk = %version, %libname-devel = %version

%description -n %libname-gtk-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional static libraries used for
developing GUI applications based on GTK+-2.0 that include a bar code
scanning widget.

%package -n python-module-%name
Group: Development/Python
Summary: Bar code reader PyGTK widget

%description -n python-module-zbar
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use in GUI
applications based on PyGTK.

%package -n %libname-qt
Group: Development/KDE and QT
Summary: Bar code reader Qt widget

%description -n %libname-qt
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use with GUI
applications based on Qt4.

%package -n %libname-qt-devel
Group: Development/KDE and QT
Summary: Bar code reader Qt widget extra development files
Requires: %libname-qt = %version, %libname-devel = %version

%description -n %libname-qt-devel
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional libraries used for
developing GUI applications based on Qt4 that include a bar code
scanning widget.

%package -n %libname-qt-devel-static
Group: Development/KDE and QT
Summary: Bar code reader Qt widget extra development files and static libraries
Requires: %libname-qt = %version, %libname-devel = %version

%description -n %libname-qt-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional static libraries used for
developing GUI applications based on Qt4 that include a bar code
scanning widget.

%prep
%setup
%patch1 -p1
%patch2 -p1
for F in `grep -rl dprintf *`; do
sed -i.dprintf 's/dprintf/debprintf/g' $F
done

%build
%autoreconf
%configure 

#	--without-qt
#	--without-xshm \
#	--without-xv \
#	--without-npapi \
#	--without-gtk \
#	--without-python \
#	--without-imagemagick \
#	--disable-libtool-lock \
#	--disable-pthread \
#	--disable-video \
#	--disable-assert

%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %libname
%_libdir/%libname.so.*
%doc %_docdir/%name/COPYING
%doc %_docdir/%name/INSTALL
%doc %_docdir/%name/NEWS
%doc %_docdir/%name/README
%doc %_docdir/%name/TODO
%doc %_docdir/%name/LICENSE

%files
%_bindir/zbarimg
%_bindir/zbarcam
%_man1dir/*

%files -n %libname-devel
%doc %_docdir/%name/HACKING
%_libdir/%libname.so
%_pkgconfigdir/%name.pc
%_includedir/%name.h
%_includedir/%name/Exception.h
%_includedir/%name/Symbol.h
%_includedir/%name/Image.h
%_includedir/%name/Scanner.h
%_includedir/%name/Decoder.h
%_includedir/%name/ImageScanner.h
%_includedir/%name/Video.h
%_includedir/%name/Window.h
%_includedir/%name/Processor.h

%files -n %libname-devel-static
%_libdir/%libname.a

%files -n %libname-gtk
%_libdir/libzbargtk.so.*

%files -n %libname-gtk-devel
%_libdir/libzbargtk.so
%_pkgconfigdir/zbar-gtk.pc
%_includedir/%name/zbargtk.h

%files -n %libname-gtk-devel-static
%_libdir/libzbargtk.a

%files -n python-module-%name
%python_sitelibdir/%name.la
%python_sitelibdir/%name.so
%python_sitelibdir/zbarpygtk.la
%python_sitelibdir/zbarpygtk.so

%files -n %libname-qt
%_libdir/libzbarqt.so.*

%files -n %libname-qt-devel
%_libdir/libzbarqt.so
%_pkgconfigdir/zbar-qt.pc
%_includedir/%name/Q*.h

%files -n %libname-qt-devel-static
%_libdir/libzbarqt.a

%changelog
* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.10-alt7.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.10-alt7
- Rebuild with new libImageMagick

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt6.1
- Fixed build

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.10-alt6
- Rebuild with new libImageMagick

* Thu Apr 04 2013 Fr. Br. George <george@altlinux.ru> 0.10-alt5
- Switch back to precious upstream sources
- Add Debian patches
- Fix dprintf redefinition

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.10-alt4.2.1
- Rebuild with new libImageMagick

* Mon May 28 2012 Sergey Alembekov <rt@altlinux.ru> 0.10-alt4.2
- fix build against new version of glibc-kernheaders:
  use libv4l1-videodev.h instead linux/videodev.h

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt4.1
- Rebuild with Python-2.7

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.10-alt4
- rebuild with new ImageMagick

* Mon Sep 13 2010 Sergey Alembekov <rt@altlinux.ru> 0.10-alt3
rebuild with new ImageMagic

* Fri Jul 16 2010 Anton Farygin <rider@altlinux.ru> 0.10-alt2
- rebuild with new ImageMagick

* Sun Dec 06 2009 Sergey Alembekov <rt@altlinux.ru> 0.10-alt1
- the project has changed name from zebra to zbar
- new version

* Tue Feb 03 2009 Sergey Alembekov <rt@altlinux.ru> 0.5svn75-alt1.1
- move static libs to separate packages
- fixed dependencies

* Sun Jan 25 2009 Sergey Alembekov <rt@altlinux.ru> 0.5svn75-alt1
- initial buils for ALTLinux Sisyphus
