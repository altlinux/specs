%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-api
Version: 0.3.2
Release: alt1

Summary: API for Lomiri shell integration
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-api

Source: %name-%version.tar

# sync with version 0.2.3-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: doxygen
BuildRequires: /usr/bin/dot
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libqtdbustest-1)

%if_with check
BuildRequires: ctest
BuildRequires: ayatana-cmake-modules
%endif

%description
Lomiri Operating Environment is a convergent work shell designed for use
cases on phone, tablet or desktop devices.

Lomiri API Library for integrating with the Lomiri shell.

%package -n liblomiri-api0
Summary: API for Lomiri shell integration (shared library)
Group: System/Libraries

%description -n liblomiri-api0
Lomiri Operating Environment is a convergent work shell designed for use
cases on phone, tablet or desktop devices.

Lomiri API Library for integrating with the Lomiri shell.

This package contains the shared library.

%package -n liblomiri-api-doc
Summary: API for Lomiri shell integration (documentation)
Group: Documentation

%description -n liblomiri-api-doc
Lomiri Operating Environment is a convergent work shell designed for use
cases on phone, tablet or desktop devices.

Lomiri API Library for integrating with the Lomiri shell.

This package contains the API documentation.

%package -n liblomiri-api-devel
Summary: API for Lomiri shell integration (development headers)
Group: Development/C
Requires: liblomiri-api0 = %{version}-%{release}

%description -n liblomiri-api-devel
Lomiri Operating Environment is a convergent work shell designed for use
cases on phone, tablet or desktop devices.

Lomiri API Library for integrating with the Lomiri shell.

This package contains the development files.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DCMAKE_LIBRARY_ARCHITECTURE=../../%{_libdir} \
%if_with check
       -DNO_TESTS=OFF \
       -Dqmltestrunner_exe=%_qt5_bindir/qmltestrunner
%else
       -DNO_TESTS=ON
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -V

%files -n liblomiri-api0
%doc AUTHORS COPYING NEWS README
%_libdir/liblomiri-api.so.0
%_libdir/liblomiri-api.so.0.2

%files -n liblomiri-api-devel
%dir %_includedir/lomiri-api
%_includedir/lomiri-api/*
%dir %_includedir/lomiri-shell-api
%_includedir/lomiri-shell-api/*
%_libdir/liblomiri-api.so
%_libdir/pkgconfig/*.pc

%files -n liblomiri-api-doc
%dir %_docdir/lib%{name}/
%_docdir/lib%{name}/*

%changelog
* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.3-alt1
- New version 0.2.3.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
