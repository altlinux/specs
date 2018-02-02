Name: makesurface
Version: 0.2.14
Release: alt1.1
Summary: Create vector datasets from raster surfaces
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/makesurface/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapbox/make-surface.git
Source0: https://pypi.python.org/packages/7d/a8/d6b3561d36bc45eaa6aba7b05624b9fa351430be7ac4b05cbb5d1c0958af/%{name}-%{version}dev.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-click python-module-fiona
BuildPreReq: python-module-numpy python-module-rasterio
BuildPreReq: python-module-shapely python-module-scipy
BuildPreReq: python-module-mercantile python-module-pyproj

%py_provides %name
%py_requires click fiona numpy rasterio shapely scipy mercantile pyproj

%description
Raster -> vector surface creation tools in python.

%prep
%setup -q -n %{name}-%{version}dev

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.14-alt1
- automated PyPI update

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.git20150218
- Initial build for Sisyphus

