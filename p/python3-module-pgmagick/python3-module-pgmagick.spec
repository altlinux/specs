%define pypi_name pgmagick

%def_with check

Name:    python3-module-%pypi_name
Version: 0.7.6
Release: alt1

Summary: pgmagick is a yet another boost.python based wrapper for GraphicsMagick/ImageMagick
License: MIT
Group:   Development/Python3
URL:     https://github.com/hhatto/pgmagick

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: libGraphicsMagick-c++-devel
BuildRequires: gcc-c++
BuildRequires: boost-python-headers
BuildRequires: boost-devel-headers
BuildRequires: boost-python3-devel
BuildRequires: fonts-ttf-ms
BuildRequires: fonts-type1-urw

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's/PYTHON?=python/PYTHON?=python3/' test/Makefile

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
make -C test all clean

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 03 2025 Alexander Burmatov <thatman@altlinux.org> 0.7.6-alt1
- Initial build for Sisyphus.
