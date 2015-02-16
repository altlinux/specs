%define oname flex

%def_with python3

Name: python-module-%oname
Version: 3.2.0
Release: alt1.git20150214
Summary: Swagger Schema validation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/flex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pipermerriam/flex.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-drf-compound-fields python-module-django-tests
BuildPreReq: python-module-djangorestframework python-module-six
BuildPreReq: python-module-yaml python-module-iso8601
BuildPreReq: python-module-validate_email python-module-rfc3987
BuildPreReq: python-module-pytest-pythonpath python-module-tox
BuildPreReq: python-module-pytest-httpbin python-module-requests
BuildPreReq: python-module-factory_boy python-module-pip
BuildPreReq: python-module-click
BuildPreReq: python-module-sphinx-devel python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-drf-compound-fields python3-module-django-tests
BuildPreReq: python3-module-djangorestframework python3-module-six
BuildPreReq: python3-module-yaml python3-module-iso8601
BuildPreReq: python3-module-validate_email python3-module-rfc3987
BuildPreReq: python3-module-pytest-pythonpath python3-module-tox
BuildPreReq: python3-module-pytest-httpbin python3-module-requests
BuildPreReq: python3-module-factory_boy python3-module-pip
BuildPreReq: python3-module-click
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Validation tooling for Swagger 2.0 specifications.

%package -n python3-module-%oname
Summary: Swagger Schema validation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Validation tooling for Swagger 2.0 specifications.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Validation tooling for Swagger 2.0 specifications.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Validation tooling for Swagger 2.0 specifications.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
mv %buildroot%_bindir/%oname %buildroot%_bindir/%oname.py

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGELOG *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
#exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%_bindir/*.py3
%python3_sitelibdir/*
#exclude %python3_sitelibdir/tests
%endif

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1.git20150214
- Version 3.2.0

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.git20150211
- Version 3.1.0

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20141117
- Version 2.1.0

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141108
- Initial build for Sisyphus

