Name: makesurface
Version: 0.2.9
Release: alt1.git20150218
Summary: Create vector datasets from raster surfaces
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/makesurface/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapbox/make-surface.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-click python-module-fiona
BuildPreReq: python-module-numpy python-module-rasterio
BuildPreReq: python-module-shapely python-module-scipy
BuildPreReq: python-module-mercantile python-module-pyproj

%py_provides %name
%py_requires click fiona numpy rasterio shapely scipy mercantile pyproj

%description
Raster -> vector surface creation tools in python.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.git20150218
- Initial build for Sisyphus

