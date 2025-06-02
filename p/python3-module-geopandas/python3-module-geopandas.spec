%define pypi_name geopandas

%ifarch i586
%def_without check
%else
%def_with check
%endif

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Python tools for geographic data
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/geopandas
Vcs: https://github.com/geopandas/geopandas

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pandas
BuildRequires: python3-module-pandas-tests
BuildRequires: python3-module-shapely
BuildRequires: python3-module-fiona
BuildRequires: python3-module-rtree
BuildRequires: python3-module-fsspec
BuildRequires: python3-module-geopy
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-scipy
BuildRequires: python3-module-pyproj
BuildRequires: proj
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-pyarrow
%endif

%description
%summary.

%package tests
Summary: Tests for geopandas
Group: Development/Python3
Requires: %name = %EVR

%description tests
%summary.

This package contains tests for geopandas.

%prep
%setup -n %pypi_name-%version

# do not use versioneer
sed -i 's/^dynamic = \["version"\]$/version = "%version"/' pyproject.toml
sed -i '/import versioneer/d' setup.py
sed -i 's/version=versioneer.get_version(),/version="%version",/' setup.py
sed -i '/cmdclass=versioneer.get_cmdclass(),/d' setup.py
rm -rf setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -rsfE -m 'not web' -k " \
not test_predicates_vector_scalar[geom_almost_equals-args10] \
and not test_predicates_vector_vector[geom_almost_equals-args10]"

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/tests
%exclude %python3_sitelibdir/%pypi_name/*/tests
%exclude %python3_sitelibdir/%pypi_name/conftest.py

%files tests
%python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/*/tests
%python3_sitelibdir/%pypi_name/conftest.py

%changelog
* Mon Jun 02 2025 Anton Vyatkin <toni@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Sat May 03 2025 Anton Vyatkin <toni@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
