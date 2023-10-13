Name: libxlsxwriter
Version: 1.1.5
Release: alt1
Summary: A C library for creating Excel XLSX files
Group: Development/C
Packager: Ilya Mashkin <oddity@altlinux.ru>
# BSD: Most files
# Public Domain: third_party/md5/*
# MPL: third_party/tmpfileplus/*
License: BSD and Public Domain and MPLv2.0
Url: https://github.com/jmcnamara/libxlsxwriter/
Source0: https://github.com/jmcnamara/libxlsxwriter/archive/RELEASE_%version/%name-%version.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libminizip-devel
BuildRequires: zlib-devel
BuildRequires: python3-module-pytest

%description
Libxlsxwriter is a C library that can be used to write text, numbers, formulas
and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.

%package devel
Summary: Development files for %name
Requires: %name%{?_isa} = %version-%release
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-RELEASE_%version

%__subst 's|ZLIB REQUIRED "1.0"|ZLIB|' CMakeLists.txt

# Delete bundled minizip
rm -rf third_party/minizip
rm -f include/xlsxwriter/third_party/zip.h

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%cmake -DUSE_SYSTEM_MINIZIP=ON -DBUILD_TESTS=ON -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%doc Readme.md Changes.txt License.txt
%_libdir/%name.so.5*

%files devel
%_includedir/xlsxwriter.h
%_includedir/xlsxwriter/
%_libdir/%name.so
%_libdir/pkgconfig/xlsxwriter.pc

%changelog
* Fri Oct 13 2023 Ilya Mashkin <oddity@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- NMU: fix zlib find via cmake

* Fri Jan 07 2022 Ilya Mashkin <oddity@altlinux.ru> 1.1.4-alt1
- Build for Sisyphus

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Tue Aug 10 2021 Sandro Mani <manisandro@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 1.1.2-2
- Add libxlsxwriter_operator.patch

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Tue Jul 27 2021 Sandro Mani <manisandro@gmail.com> - 1.1.1-2
- Backport fix for test failure

* Fri Jul 23 2021 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sat Jul 10 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Apr 16 2021 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Wed Mar 31 2021 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for minizip 3.0.0

* Tue Feb 09 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-4
- Rebuild (minizip)

* Sat Nov 14 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-2
- Fix license
- Start with soversion 0
- Remove ldconfig scriptlets

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0
