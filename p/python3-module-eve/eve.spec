%define oname eve

%def_disable check

%def_without docs

Name: python3-module-%oname
Version: 0.7.8
Release: alt1
Summary: REST API framework powered by Flask, MongoDB and good intentions
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/Eve/

# https://github.com/nicolaiarocci/eve.git
Source: %name-%version.tar
Patch1: %oname-0.7.5-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-cerberus python3-module-events
BuildRequires: python3-module-pytest
BuildRequires: python3-module-flask-pymongo

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-simplejson
%endif

%py3_provides %oname
%py3_requires flask_pymongo

%description
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR ~/code/eve.docs/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
python3 setup.py test

%files
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc ~/code/eve.docs/html/*
%endif

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.8-alt1
- Build new version.
- Build without python2.
- Build without docs, because they use too old api.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150112
- Version 0.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140620
- Initial build for Sisyphus

