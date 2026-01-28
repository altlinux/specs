%global pypi_name gbinder-python
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 1.3.0
Release: alt1
Summary: Python bindings for libgbinder
Group: Development/Python

License: GPL-3.0-only
Url: https://github.com/erfanoabdi/gbinder-python
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: python3-devel
BuildRequires: python3-module-wheel python3-module-Cython libgbinder-devel

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python

%description
Cython extension module for gbinder.

%description -n python3-module-%{pypi_name}
Cython extension module for gbinder.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%python3_sitelibdir/*.so
%python3_sitelibdir/gbinder_python-%{version}.dist-info/

%changelog
* Wed Jan 28 2026 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt1
- 1.3.0.

* Sat Dec 21 2024 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt0.2
- ix86: Fix FTBFS with gcc14.

* Thu Oct 26 2023 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt0.1
- 1.1.2.

* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.1.1-alt0.1
- Initial build for ALTLinux.
