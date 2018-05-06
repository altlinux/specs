Name: libArcus
Version: 3.3.0
Release: alt1%ubt

Summary: Communication library between internal components for Ultimaker software
License: LGPLv3+
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

%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF \
       -DCMAKE_SKIP_RPATH:BOOL=ON
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
* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1%ubt
- New version 3.3.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1%ubt.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1%ubt
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1%ubt
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1%ubt
- Initial build for ALT Sisyphus.
