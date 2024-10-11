%define _unpackaged_files_terminate_build 1
%define pypi_name geopy
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1

Summary: Python Geocoding Toolbox
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/geopy/
Vcs: https://github.com/geopy/geopy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev-test
# setup.py: `docutils` from sphinx is used in tests
# sphinx is filtered by rpm-build-pyproject
BuildRequires: python3-module-sphinx
%endif

%description
geopy is a Python client for several popular geocoding web services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources.

geopy includes geocoder classes for the OpenStreetMap Nominatim, Google
Geocoding API (V3), and many other geocoding services.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra --skip-tests-requiring-internet

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 11 2024 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 1.19.0 -> 2.4.1.

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

