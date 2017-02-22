%define oname double-conversion
%def_disable statis

Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles
Name: lib%oname
Version: 2.0.1
Release: alt1
License: BSD
Group: System/Libraries
Url: https://github.com/floitsch/double-conversion

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Provides binary-decimal and decimal-binary routines for IEEE doubles.
The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been re-factored
and improved so that it can be used more easily in other projects.

%package devel
Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles
Group: Development/C
Requires: %name = %EVR

%description devel
Contains header files for developing applications that use the %name
library.

%package static
Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles
Group: Development/C
Requires: %name-devel = %EVR

%description static
Static %name library.

%prep
%setup
%patch -p1
rm -f BUILD

%build
%cmake \
        -DBUILD_SHARED_LIBS=ON \
        -DBUILD_STATIC_LIBS=OFF

%cmake_build

%install
%cmakeinstall_std

#%check
#pushd build-shared
#  ctest -V
#popd

%files
%doc LICENSE README.md AUTHORS Changelog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/cmake/%oname
%_includedir/%oname

%if_enabled static
%files static
%_libdir/*.a
%endif

%changelog
* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- Initial build
- master snapshot d8d4e668ee1e6e10b728f0671a89b07d7c4d45be
