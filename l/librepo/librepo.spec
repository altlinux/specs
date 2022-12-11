Name:    librepo
Version: 1.15.1
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
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: python3-dev

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
%cmake -DWITH_ZCHUNK=OFF
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
* Sun Dec 11 2022 Andrey Cherepanov <cas@altlinux.org> 1.15.1-alt1
- New version.

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 1.14.5-alt1
- Initial build for Sisyphus
