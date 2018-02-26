%define major 0.9
Name: podofo
Version: %major.0
Release: alt1

Summary: PDF manipulation library and tools
Summary(ru_RU.UTF8): Библиотека и инструменты для работы с PDF

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: distributable (see COPYING)
Group: Office
URL: http://sourceforge.net/projects/podofo/

Source: http://prdownloads.sf.net/podofo/%name/%major/%name-%version.tar
Patch: %name-64bit.patch

BuildPrereq: rpm-macros-cmake zlib-devel

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
%patch -p2
%cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%buildroot/%_prefix -DPODOFO_BUILD_SHARED:BOOL=TRUE

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
