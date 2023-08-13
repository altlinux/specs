%define sover 1.4.0
%define libquazip libquazip1-qt6

%define rname quazip

Name: quazip-qt6
Version: 1.4
Release: alt1

Summary: Qt/C++ wrapper for the minizip library

License: GPL-2.0-or-later OR LGPL-2.1-or-later
Group: System/Libraries
Url: https://github.com/stachenov/quazip

# Source-url: https://github.com/stachenov/quazip/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest
BuildRequires: zlib-devel bzip2-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-5compat-devel

BuildRequires: doxygen graphviz

%description
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
(AKA Minizip) using Trolltech's Qt library.

If you need to write files to a ZIP archive or read files from one
using QIODevice API, QuaZip is exactly the kind of tool you need.

%package -n %libquazip
Summary: Qt wrapper for the minizip library
Group: System/Libraries
%description -n %libquazip
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
(AKA Minizip) using Trolltech's Qt library.

If you need to write files to a ZIP archive or read files from one
using QIODevice API, QuaZip is exactly the kind of tool you need.

%package devel
Summary: Development files for %rname
Group: Development/C++
Requires: %libquazip = %EVR

Requires: bzip2-devel
Requires: qt6-base-devel
Requires: qt6-5compat-devel
Requires: zlib-devel



%description devel
The %name-devel package contains libraries, header files and documentation
for developing applications that use %rname.

%prep
%setup

%build
%cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build

doxygen Doxyfile
for file in doc/html/*; do
    touch -r Doxyfile $file
done


%install
%cmake_install

%check
export QT_ENABLE_REGEXP_JIT=0
%ctest


%files -n %libquazip
%doc COPYING NEWS.txt *.md
%_libdir/libquazip1-qt6.so.%sover
%_libdir/libquazip1-qt6.so.%version

%files devel
%doc doc/html
%_includedir/QuaZip-Qt6-%version/
%_libdir/libquazip1-qt6.so
%_libdir/cmake/QuaZip-Qt6-%version/
%_pkgconfigdir/quazip1-qt6.pc

%changelog
* Sun Aug 13 2023 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- initial build Qt6 support (based on quazip-qt5 package)
