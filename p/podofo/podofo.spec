%define major 0.10
%define abiversion 2

Name: podofo
Version: %major.4
Release: alt1

Summary: PDF manipulation library and tools
Summary(ru_RU.UTF8): Библиотека и инструменты для работы с PDF

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: LGPLv2-plus AND GPLv2-plus
Group: Office
URL: https://github.com/podofo/podofo

# Source-url: https://github.com/podofo/podofo/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel
BuildRequires: zlib-devel libxml2-devel libssl-devel

# Just to hide 'Package bzip2 was not found in the pkg-config search path.'
# See https://bugzilla.altlinux.org/30001
BuildRequires: bzlib-devel

%define libname lib%name%abiversion

Requires: %libname = %EVR

%description
PoDoFo is a library and a set of tools to work with the PDF file format.

%description -l ru_RU.UTF8
PoDoFo - это библиотека и набор инструментов для работы с файлами формата PDF.

%package -n %libname
Summary: PoDoFo library
Summary(ru_RU.UTF8): Библиотека PoDoFo
Group: System/Libraries

%description -n %libname
Library to work with PDF files.

%description -n %libname -l ru_RU.UTF8
Библиотека для работы с файлами формата PDF.

%package -n lib%name-devel
Summary: PoDoFo headers
Summary(ru_RU.UTF8): Заголовочные файлы PoDoFo
Group: Development/C
Requires: %libname = %EVR

%description -n lib%name-devel
Development files for the PoDoFo library.

%description -n lib%name-devel -l ru_RU.UTF8
Файлы, необходимые для разработки с использованием библиотеки PoDoFo.

%prep
%setup
subst "s|@PODOFO_VERSION@|%version|" src/podofo/libpodofo.pc.in
# fix broken copying rule
#mkdir test/TokenizerTest/objects

%build
%cmake -DPODOFO_BUILD_TOOLS=ON
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_cmakedir/
mv %buildroot%_datadir/%name %buildroot%_cmakedir/

%files
%doc README.md
%_bindir/podofo*

%files -n %libname
%doc README.md AUTHORS.md CHANGELOG.md
%_libdir/libpodofo.so.%abiversion
%_libdir/libpodofo.so.%version

%files -n lib%name-devel
%_includedir/%name/
%_pkgconfigdir/libpodofo.pc
%_cmakedir/%name/
%_libdir/libpodofo.so

%changelog
* Tue Dec 03 2024 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt1
- new version 0.10.4 (with rpmrb script)

* Wed Feb 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.10.3-alt1
- new version 0.10.3 (with rpmrb script)
- more strict paths in files section
- build lib package as libpodofo2

* Wed Feb 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- the release is complete re-imagination of PoDoFo 0.9.x API in C++17,
  and it's API/ABI incompatible with the previous releases.
- cleanup spec, change URL and Source URL to github place

* Fri Dec 09 2022 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version 0.9.8 (with rpmrb script)
- CVE-2021-30469, CVE-2021-30470, CVE-2021-30471, CVE-2021-30472

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt2
- fix build with cmake 3.13.1 (ALT bug 35732)
- build with -D_FILE_OFFSET_BITS=64

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (with rpmrb script)

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5 (with rpmrb script)

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
