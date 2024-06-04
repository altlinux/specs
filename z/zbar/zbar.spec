%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_without java

%def_with qt5
%if_without qt5
%def_without qt
%endif

Name: zbar
Version: 0.23.93
Release: alt1
%define libname libzbar

Summary: A library for scanning and decoding bar codes

Group: Graphics
License: GPLv2+
Url: https://github.com/mchehab/zbar
Source: %name-%version.tar

BuildRequires: glibc-devel-static libImageMagick-devel libdbus-devel libgtk+3-devel libjpeg-devel libv4l-devel python3-dev xmlto

%if_with qt5
BuildRequires: qt5-x11extras-devel
%endif

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

%description -n %libname-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains additional static libraries used for
developing applications that read bar codes with this library.

%package -n %libname-gtk3
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK3 widget

%description -n %libname-gtk3
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use with GUI
applications based on GTK+-2.0.

%package -n %libname-gtk3-devel
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK widget extra development files

%description -n %libname-gtk3-devel
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional libraries used for
developing GUI applications based on GTK+-3.0 that include a bar code
scanning widget.

%package -n %libname-gtk3-devel-static
Group: Development/GNOME and GTK+
Summary: Bar code reader GTK3 widget extra development files and static libraries

%description -n %libname-gtk3-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional static libraries used for
developing GUI applications based on GTK+-3.0 that include a bar code
scanning widget.

%package -n python3-module-%name
Group: Development/Python3
Summary: Bar code reader PyGTK3 widget

%description -n python3-module-zbar
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use in GUI
applications based on PyGTK.

%package gtk
Group: Graphics
Summary: Bar code camera reader GTK3 aplication

%description gtk
%summary

%if_with qt5
%package qt5
Group: Graphics
Summary: Bar code camera reader Qt5 aplication

%description qt5
%summary

%package -n %libname-qt5
Group: Development/KDE and QT
Summary: Bar code reader Qt5 widget

%description -n %libname-qt5
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains a bar code scanning widget for use with GUI
applications based on Qt5.

%package -n %libname-qt5-devel
Group: Development/KDE and QT
Summary: Bar code reader Qt widget extra development files

%description -n %libname-qt5-devel
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional libraries used for
developing GUI applications based on Qt5 that include a bar code
scanning widget.

%package -n %libname-qt5-devel-static
Group: Development/KDE and QT
Summary: Bar code reader Qt5 widget extra development files and static libraries

%description -n %libname-qt5-devel-static
Zbar is a library for scanning and decoding bar codes from various
sources such as video streams, image files or raw intensity sensors.
It supports EAN, UPC, Code 128, Code 39 and Interleaved 2 of 5. The
flexible, layered architecture features a fast, streaming interface
with a minimal memory footprint.

This package contains header files and additional static libraries used for
developing GUI applications based on Qt5 that include a bar code
scanning widget.
%endif

%prep
%setup

# TODO
sed -i 's/gtk+-2.0/gtk+-3.0/' zbar-gtk.pc.in

%build
%autoreconf
export LIBS=-lm
%configure \
	%{subst_with qt} \
	%{subst_with qt5} \
	%{subst_with java} \
	--with-python=python3 \
	--with-gtk=gtk3 \
	--with-gir=yes \

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/zbarimg
%_bindir/zbarcam
%_man1dir/*

%files -n %libname
%_libdir/%libname.so.*
%doc %_docdir/%name/[^H]*.md

%files -n %libname-devel
%doc %_docdir/%name/HACKING*
%_libdir/%libname.so
%_pkgconfigdir/%name.pc
%_includedir/%name.h
%_includedir/%name/*.h
%exclude %_includedir/%name/*gtk.h
%if_with qt5
%exclude %_includedir/%name/Q*
%endif

%files -n %libname-devel-static
%_libdir/%libname.a

%files -n %libname-gtk3
%_libdir/libzbargtk.so.*

%files -n %libname-gtk3-devel
%_libdir/libzbargtk.so
%_pkgconfigdir/zbar-gtk.pc
%_includedir/%name/*gtk.h

%files -n %libname-gtk3-devel-static
%_libdir/libzbargtk.a

%files -n python3-module-%name
%python3_sitelibdir/*.so

%files gtk
%_bindir/*gtk

%if_with qt5
%files qt5
%_bindir/*qt

%files -n %libname-qt5
%_libdir/libzbarqt.so.*

%files -n %libname-qt5-devel
%_libdir/libzbarqt.so
%_pkgconfigdir/zbar-qt.pc
%_includedir/%name/Q*.h

%files -n %libname-qt5-devel-static
%_libdir/libzbarqt.a
%endif

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 0.23.93-alt1
- Automatically updated to 0.23.93.

* Wed Jan 03 2024 Grigory Ustinov <grenka@altlinux.org> 0.23.92-alt5
- Add python3.12 support.

* Sat Jan 28 2023 Grigory Ustinov <grenka@altlinux.org> 0.23.92-alt4
- Add python3.11 support.

* Mon Oct 04 2021 Ivan A. Melnikov <iv@altlinux.org> 0.23.92-alt3
- re-enable Qt5 support on riscv64

* Sat Sep 18 2021 Anton Farygin <rider@altlinux.ru> 0.23.92-alt2
- fixed build with enabled LTO

* Wed Apr 14 2021 Anton Farygin <rider@altlinux.org> 0.23.92-alt1
- update to 0.23.92

* Fri Jan 29 2021 Grigory Ustinov <grenka@altlinux.org> 0.23.1-alt2
- Add python3.9 support.

* Thu Jun 04 2020 Fr. Br. George <george@altlinux.ru> 0.23.1-alt1
- Autobuild version bump to 0.23.1

* Fri Dec 20 2019 Fr. Br. George <george@altlinux.ru> 0.23-alt1
- Huge version update
- Switch to python3/qt5/gtk3
- Autobuild version bump to 0.23

* Mon Aug 05 2019 Nikita Ermakov <arei@altlinux.org> 0.10-alt10
- NMU: Disable qt4 for RISC-V.

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 0.10-alt9
- Rebuilt for ImageMagick.

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 0.10-alt8
- Rebuilt for ImageMagick.

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
