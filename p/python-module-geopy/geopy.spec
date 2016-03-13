%define oname geopy

%def_with python3

Name: python-module-%oname
Version: 1.7.0
Release: alt1.git20141230.1.1
Summary: Python Geocoding Toolbox
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/geopy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geopy/geopy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
geopy is a Python 2 and 3 client for several popular geocoding web
services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, ESRI
ArcGIS, Google Geocoding API (V3), Baidu Maps, Bing Maps API, Yahoo!
PlaceFinder, GeoNames, MapQuest, OpenMapQuest, OpenCage, SmartyStreets,
geocoder.us, and GeocodeFarm geocoder services. The various geocoder
classes are located in geopy.geocoders.

%package -n python3-module-%oname
Summary: Python Geocoding Toolbox
Group: Development/Python3

%description -n python3-module-%oname
geopy is a Python 2 and 3 client for several popular geocoding web
services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, ESRI
ArcGIS, Google Geocoding API (V3), Baidu Maps, Bing Maps API, Yahoo!
PlaceFinder, GeoNames, MapQuest, OpenMapQuest, OpenCage, SmartyStreets,
geocoder.us, and GeocodeFarm geocoder services. The various geocoder
classes are located in geopy.geocoders.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc *.md docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/test

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.git20141230.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20141230.1
- NMU: Use buildreq for BR.

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20141230
- Version 1.7.0

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141208
- Version 1.6.0

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140923
- Initial build for Sisyphus

