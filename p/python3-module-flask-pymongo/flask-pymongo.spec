%define oname Flask-PyMongo

%def_disable check

Name: python3-module-flask-pymongo
Version: 2.3.0
Release: alt1

Summary: PyMongo support for Flask applications

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-PyMongo/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-vcversioner

%if_enabled check
BuildRequires: python3-module-coverage python3-module-nose python3-module-pytest
%endif

%description
PyMongo support for Flask applications.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
%if_enabled check
python3 setup.py test
%endif

%files
%doc *.md docs/*.rst examples
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt2
- build python3 package separately

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt1.git20131201.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20131201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20131201.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20131201
- Initial build for Sisyphus

