Name: libsavitar
Version: 3.0.3
Release: alt1%ubt
Summary: C++ implementation of 3mf loading with SIP Python bindings
License: AGPLv3+
Group: Development/Other
Url: https://github.com/Ultimaker/libSavitar
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: %name-no-pugixml.patch

Buildrequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake dos2unix gcc-c++ libpugixml-devel python3-devel python3-module-sip-devel %_bindir/sip

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package devel
Summary: Development files for libsavitar
# The cmake scripts are BSD
License: AGPLv3+ and BSD
Group: Development/Other
Requires: %name = %version-%release

%description devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n python3-module-savitar
Summary: Python 3 libSavitar bindings
Group: Development/Python3
Requires: %name = %version-%release
%py3_provides Savitar

%description -n python3-module-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%setup
%patch -p1

# Wrong end of line encoding
dos2unix README.md

# Bundling
rm pugixml -rf
%__subst 's|"../pugixml/src/pugixml.hpp"|<pugixml.hpp>|g' src/*.cpp src/*.h

# Move stuff to lib64 on 64 arches
# TODO propose a change to honor -DLIB_SUFFIX=64
%__subst 's|DESTINATION lib|DESTINATION %_lib|g' CMakeLists.txt
%__subst 's|PYTHON_SITE_PACKAGES_DIR lib|PYTHON_SITE_PACKAGES_DIR %_lib|g' CMakeLists.txt

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md LICENSE
%_libdir/libSavitar.so.*

%files devel
%_libdir/libSavitar.so
%_includedir/Savitar
# Own the dir not to depend on cmake:
%_libdir/cmake

%files -n python3-module-savitar
%doc README.md LICENSE
%python3_sitelibdir/Savitar.so

%changelog
* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1%ubt
- Initial build for ALT Sisyphus.
