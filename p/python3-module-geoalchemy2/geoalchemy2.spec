%define oname geoalchemy2

Name: python3-module-%oname
Version: 0.4
Release: alt2

Summary: Geospatial extension to SQLAlchemy with PostGIS support

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/GeoAlchemy2/

# https://github.com/geoalchemy/geoalchemy2.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
Patch2: 146.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-flake8 python3-module-psycopg2 python3-module-pytest-cov python3-module-setuptools
BuildRequires: python3-module-SQLAlchemy python3-module-shapely

%description
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

%prep
%setup
%patch1 -p1
%patch2 -p1

#prepare_sphinx3 .
#ln -s ../objects.inv doc/

%build
%python3_build_debug

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 || :

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
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

