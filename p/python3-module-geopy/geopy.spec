%define oname geopy

%def_with check

Name: python3-module-%oname
Version: 1.19.0
Release: alt1.1

Summary: Python Geocoding Toolbox
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/geopy/
BuildArch: noarch

# https://github.com/geopy/geopy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme

%if_with check
BuildRequires: python3-module-geographiclib
%endif


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

%package tests
Summary: Tests %name
Group: Development/Python3
Requires: %name = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/test

%description tests
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

This package contains tests for %name.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

mv test/ %buildroot%python3_sitelibdir/%oname

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%if_with check
%check
%__python3 setup.py test
%endif

%files
%doc *.md docs/_build/html
%python3_sitelibdir/*

%exclude %python3_sitelibdir/%oname/test

%files tests
%python3_sitelibdir/%oname/test


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.19.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.19.0-alt1
- Version updated to 1.19.0
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.7.0-alt1.git20141230.1.2
- (NMU) rebuild with python3.6

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

