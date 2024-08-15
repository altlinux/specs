Name:    librepo
Version: 1.18.1
Release: alt1

Summary: A library providing C and Python (libcURL like) API for downloading packages and linux repository metadata in rpm-md format
License: LGPL-2.1
Group:   System/Libraries
Url:     https://github.com/rpm-software-management/librepo

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: glib2-devel
BuildRequires: libcheck-devel
BuildRequires: libcurl-devel
BuildRequires: libgio-devel
BuildRequires: libgpgme-devel
BuildRequires: libselinux-devel
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: python3-dev
BuildRequires: doxygen

%description
%{summary}.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%{summary}.

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3

%description -n python3-module-%name
%{summary}.

%prep
%setup

%build
%cmake -Wno-dev \
       -DWITH_ZCHUNK=OFF
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/librepo
%_libdir/pkgconfig/librepo.pc

%files -n python3-module-%name
%python3_sitelibdir/%name

%changelog
* Thu Aug 15 2024 Andrey Cherepanov <cas@altlinux.org> 1.18.1-alt1
- New version.

* Wed Jul 03 2024 Andrey Cherepanov <cas@altlinux.org> 1.18.0-alt1
- New version.

* Wed Jun 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.17.2-alt1
- New version.

* Wed Mar 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.17.1-alt1
- New version.

* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Fri Sep 01 2023 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1
- New version.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 1.15.2-alt1
- New version.

* Sun Dec 11 2022 Andrey Cherepanov <cas@altlinux.org> 1.15.1-alt1
- New version.

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 1.14.5-alt1
- Initial build for Sisyphus
