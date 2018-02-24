Name: libArcus
Version: 3.2.1
Release: alt1%ubt

Summary: Communication library between internal components for Ultimaker software
License: LGPL-3.0
Group: Development/Other
Url: https://github.com/Ultimaker/libArcus

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

Buildrequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-dev cmake gcc-c++ pkgconfig(protobuf) python3-module-sip-devel protobuf-compiler

%description
%summary

%package devel
Summary: Development files for %name
Group:   Development/Other
Requires: %name = %version-%release

%description devel
Development files for %name.

%package -n python3-module-Arcus
Summary: Communication library between internal components for Ultimaker software
Group:   Development/Python3
%py3_provides Arcus
Requires: %name = %version-%release

%description -n python3-module-Arcus
Communication library between internal components for Ultimaker software

%prep
%setup
# Move stuff to lib64 on 64 arches
# TODO propose a change to honor -DLIB_SUFFIX=64
sed -i 's|DESTINATION lib|DESTINATION %_lib|g' CMakeLists.txt
#sed -i 's|PYTHON_SITE_PACKAGES_DIR lib|PYTHON_SITE_PACKAGES_DIR %_lib|g' CMakeLists.txt

%build
%cmake 
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*
%doc LICENSE README.md

%files devel
%_libdir/*.so
%_includedir/Arcus
%_libdir/cmake/Arcus

%files -n python3-module-Arcus
%python3_sitelibdir/*

%changelog
* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1%ubt
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1%ubt
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1%ubt
- Initial build for ALT Sisyphus.
