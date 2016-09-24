%define major 0.9
Name: podofo
Version: %major.4
Release: alt1

Summary: PDF manipulation library and tools
Summary(ru_RU.UTF8): Библиотека и инструменты для работы с PDF

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: distributable (see COPYING)
Group: Office
URL: http://sourceforge.net/projects/podofo/

Source: http://prdownloads.sf.net/podofo/%name/%major/%name-%version.tar

BuildPrereq: rpm-macros-cmake zlib-devel libpng-devel

# Automatically added by buildreq on Thu Jan 21 2010
BuildRequires: cmake fontconfig-devel gcc-c++ libfreetype-devel libjpeg-devel libssl-devel libtiff-devel
Requires: lib%name = %version

%description
PoDoFo is a library and a set of tools to work with the PDF file format.

%description -l ru_RU.UTF8
PoDoFo - это библиотека и набор инструментов для работы с файлами формата PDF.

%package -n lib%name
Summary: PoDoFo library
Summary(ru_RU.UTF8): Библиотека PoDoFo
Group: System/Libraries

%description -n lib%name
Library to work with PDF files.

%description -n lib%name -l ru_RU.UTF8
Библиотека для работы с файлами формата PDF.

%package -n lib%name-devel
Summary: PoDoFo headers
Summary(ru_RU.UTF8): Заголовочные файлы PoDoFo
Group: Development/C
Requires: lib%name = %version

%description -n lib%name-devel
Development files for the PoDoFo library.

%description -n lib%name-devel -l ru_RU.UTF8
Файлы, необходимые для разработки с использованием библиотеки PoDoFo.

%prep
%setup
%cmake -G "Unix Makefiles" \
	-DCMAKE_INSTALL_PREFIX=%buildroot/%_prefix \
	-DPODOFO_BUILD_SHARED:BOOL=TRUE \
	-DFREETYPE_INCLUDE_DIR:FILEPATH=%_includedir/freetype2

%build
%make_build -C BUILD VERBOSE=1

%install
%make install -C BUILD

%files
%doc README.html FAQ.html
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so

%changelog
* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script)

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1
- Fixed build

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.1
- Rebuilt with libtiff5
- Built with libpng15

* Mon Jun 11 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2.2
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2.1
- Rebuilt for soname set-versions

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- cleanup spec
- fix build on x86_64

* Thu Jan 21 2010 Vyacheslav Dikonov <slava@altlinux.ru> 0.7.0-alt1
- ALT Linux build
