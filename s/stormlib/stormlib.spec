%define abiversion 9

Name: stormlib
Version: 9.30
Release: alt1

Summary: Library for reading and writing Blizzard MPQ archives
License: MIT
Group: Development/C++

URL: http://www.zezula.net/en/mpq/stormlib.html
VCS: https://github.com/ladislav-zezula/StormLib

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++

%package -n libstorm%abiversion
Summary: %summary (shared library)
Group: Development/C++

%package -n libstorm-devel
Summary: %summary (header files)
Group: Development/C++

%description
%summary

%description -n libstorm%abiversion
%summary (shared library)

%description -n libstorm-devel
%summary (header files)

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DSTORM_USE_BUNDLED_LIBRARIES=OFF \
	-DCMAKE_INSTALL_DATAROOTDIR='%_libdir/cmake'
%cmake_build

%install
%cmake_install

# %check
# No check because it's whole 25G of tests
# See https://github.com/ladislav-zezula/StormLib/issues/394
# You will also need to add -DSTORM_BUILD_TESTS to cmake and install libalsa-devel

%files -n libstorm%abiversion
%_libdir/libstorm.so.%abiversion
%_libdir/libstorm.so.%abiversion.*

%files -n libstorm-devel
%doc LICENSE README.md doc/
%_libdir/libstorm.so
%_includedir/StormLib.h
%_includedir/StormPort.h
%_cmakedir/StormLib/StormLibConfig.cmake
%_cmakedir/StormLib/StormLibConfig-noconfig.cmake

%changelog
* Wed Aug 27 2025 Ilya Sorochan <k0tran@altlinux.org> 9.30-alt1
- Initial build.
