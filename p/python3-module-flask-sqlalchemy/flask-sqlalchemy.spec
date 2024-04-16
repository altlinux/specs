%define oname Flask-SQLAlchemy
%def_without docs
%def_with check

Name: python3-module-flask-sqlalchemy
Version: 3.1.1
Release: alt1

Summary: Adds SQLAlchemy support to your Flask application

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/Flask-SQLAlchemy
VCS: https://github.com/pallets-eco/flask-sqlalchemy.git

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch: stop-using-utcnow.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-flit
BuildRequires: python3-module-pdm-pep517

%if_with check
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-flask
BuildRequires: python3-module-greenlet
%endif

%if_with docs
BuildRequires: python3-module-sphinx flask-sphinx-themes
%endif

Obsoletes: python3-module-flask_sqlalchemy
Provides: python3-module-flask_sqlalchemy

%description
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
cp -fR %_datadir/flask-sphinx-themes/* docs/_themes/
%endif

%build
%pyproject_build

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/*

%if_with docs
%files docs
%doc examples docs/_build/html
%endif

%changelog
* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Tue Mar 21 2023 Danil Shein <dshein@altlinux.org> 3.0.3-alt1
- new version 3.0.3
  + migrate to pyproject_installer

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- build python3 package separately

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- NMU: updated to 2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.git20141023.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt1.git20141023.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20141023
- Initial build for Sisyphus

