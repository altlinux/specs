%define oname Flask-SQLAlchemy
%def_without docs

Name: python3-module-flask-sqlalchemy
Version: 2.5.1
Release: alt1

Summary: Adds SQLAlchemy support to your Flask application

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-SQLAlchemy/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
%if_with docs
BuildRequires: python3-module-sphinx flask-sphinx-themes
%endif

Obsoletes: python3-module-flask_sqlalchemy
Provides: python3-module-flask_sqlalchemy

%py3_use flask >= 0.10
%py3_use SQLAlchemy >= 0.7

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

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
cp -fR %_datadir/flask-sphinx-themes/* docs/_themes/
%endif

%build
%python3_build_debug

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%install
%python3_install
%python3_prune

%check
python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*

%if_with docs
%files docs
%doc examples docs/_build/html
%endif

%changelog
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

