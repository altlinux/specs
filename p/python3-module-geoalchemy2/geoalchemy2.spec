%define oname geoalchemy2

Name: python3-module-%oname
Version: 0.20.0
Release: alt1

Summary: Geospatial extension to SQLAlchemy with PostGIS support

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/GeoAlchemy2/

# https://github.com/geoalchemy/geoalchemy2.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-SQLAlchemy python3-module-shapely

%if_disabled check
%else
BuildRequires: python3-module-pytest python3-module-alembic python3-module-packaging
BuildRequires: python3-module-psycopg2 libspatialite-module8
%endif

%description
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
# Tests that need a running database server (PostgreSQL/PostGIS, MySQL/MariaDB,
# MSSQL) cannot be run in the build environment, so only SQLite (SpatiaLite,
# GeoPackage) and database-independent tests are run. The raster gallery
# example needs rasterio which is not packaged.
export SPATIALITE_LIBRARY_PATH=%_libdir/mod_spatialite.so.8
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 \
    --ignore=tests/gallery/test_insert_raster.py \
    --ignore=tests/benchmarks \
    --ignore=tests/test_functional_postgresql.py \
    --ignore=tests/test_functional_mysql.py \
    --ignore=tests/test_functional_mssql.py \
    -k 'not mysql and not mariadb and not mssql and not postgresql'

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo GeoAlchemy2}/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt1
- new version 0.20.0
- build with pyproject macros
- drop obsolete documentation patches
- run tests that do not need a database server

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- build python3 module separately

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt1
- Updated to upstream version 0.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20140919.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.git20140919.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140919
- Initial build for Sisyphus

