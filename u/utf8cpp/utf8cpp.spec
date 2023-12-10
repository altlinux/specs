Name:    utf8cpp
Version: 4.0.4
Release: alt1

Summary: UTF-8 with C++ in a Portable Way
License: BSL-1.0
Group:   Other
Url:     https://github.com/nemtrif/utfcpp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: %name-alt-cmake-dir.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
%summary

%prep
%setup
%patch0 -p1

%build
cmake -Wno-dev \
      -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DUTF8_TESTS=OFF \
      -DUTF8_SAMPLES=ON \
      .
%make_build

%install
%makeinstall_std

%files -n lib%name-devel
%doc README.md
%_includedir/*
%_libdir/cmake/*

%changelog
* Sun Dec 10 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt1
- New version.

* Mon Dec 04 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.3-alt1
- New version.

* Sat Nov 04 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- New version.

* Sat Oct 28 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.

* Mon Oct 23 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Mon Sep 25 2023 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Sun Aug 13 2023 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus.
