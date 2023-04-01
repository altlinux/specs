%global pypi_name gbinder-python
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 1.1.1
Release: alt0.1
Summary: Python bindings for libgbinder
Group: Development/Python

License: GPLv3
Url: https://github.com/erfanoabdi/gbinder-python
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-Cython libgbinder-devel

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
python3 setup.py sdist --cython
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%python3_sitelibdir/*.so
%python3_sitelibdir/gbinder_python-%{version}.dist-info/

%changelog
* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.1.1-alt0.1
- Initial build for ALTLinux.
