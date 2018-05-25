%define oname pytest-django

%def_with bootstrap
%def_disable check

Name: python-module-%oname
Version: 2.8.0
Release: alt3.1

Summary: A Django plugin for py.test
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-django/
# https://github.com/pytest-dev/pytest-django.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-alabaster python-module-django python-module-docutils 
BuildRequires: python-module-html5lib python-module-objects.inv 
BuildRequires: python-module-pytest-xdist python-module-tox python-module-sphinx-devel

BuildRequires(pre): rpm-build-python3
%if_with bootstrap
BuildPreReq: python3-module-pytest-xdist
%endif
BuildPreReq: python3-module-django python3-module-tox


%description
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%package -n python3-module-%oname
Summary: A Django plugin for py.test
Group: Development/Python3

%description -n python3-module-%oname
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

This package contains documentation for %oname.

%prep
%setup

cp -fR . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
python setup.py test
py.test

pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test-%_python3_version
popd


%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*


%changelog
* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3.1
- rebuild with all requires

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt2.git20150303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 2.8.0-alt2.git20150303
- cleanup buildreq
- disable tests

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.git20150303
- Version 2.8.0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20141012
- Initial build for Sisyphus

