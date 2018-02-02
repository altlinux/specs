%define oname mercantile

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1.1
Summary: Spherical mercator and XYZ tile utilities
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mercantile/

# https://github.com/mapbox/mercantile.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-click-tests
BuildPreReq: python-modules-json python-modules-logging
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-click-tests
BuildRequires: python3-module-pytest
%endif

%description
The mercantile module provides ul(xtile, ytile, zoom) and bounds(xtile,
ytile, zoom) functions that respectively return the upper left corner
and bounding longitudes and latitudes for XYZ tiles, a xy(lng, lat)
function that returns spherical mercator x and y coordinates, and a
tile(lng, lat, zoom) function that returns the tile containing a given
point.

%package -n python3-module-%oname
Summary: Spherical mercator and XYZ tile utilities
Group: Development/Python3


%description -n python3-module-%oname
The mercantile module provides ul(xtile, ytile, zoom) and bounds(xtile,
ytile, zoom) functions that respectively return the upper left corner
and bounding longitudes and latitudes for XYZ tiles, a xy(lng, lat)
function that returns spherical mercator x and y coordinates, and a
tile(lng, lat, zoom) function that returns the tile containing a given
point.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
py.test -vv
%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%doc *.txt *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.0-alt1
- Updated to upstream version 0.10.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20141216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141216
- Initial build for Sisyphus

