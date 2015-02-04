%define oname uranium

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.49
Release: alt1.git20150203
Summary: A build system for python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/uranium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toumorokoshi/uranium.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-docopt python-module-jinja2
BuildPreReq: python-module-pip python-module-yaml
BuildPreReq: python-module-requests python-module-six
BuildPreReq: python-module-virtualenv python-module-zc.buildout
BuildPreReq: python-module-httpretty python-module-nose
BuildPreReq: python-module-mock python-module-tornado
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-docopt python3-module-jinja2
BuildPreReq: python3-module-pip python3-module-yaml
BuildPreReq: python3-module-requests python3-module-six
BuildPreReq: python3-module-virtualenv python3-module-zc.buildout
BuildPreReq: python3-module-httpretty python3-module-nose
BuildPreReq: python3-module-mock python3-module-tornado
%endif

%py_provides %oname
%py_requires docopt jinja2 pip yaml requests six virtualenv zc.buildout

%description
uranium is a build system that allows for compilation of python-based
services and tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires httpretty nose mock

%description tests
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A build system for python
Group: Development/Python3
%py3_provides %oname
%py3_requires docopt jinja2 pip yaml requests six virtualenv zc.buildout

%description -n python3-module-%oname
uranium is a build system that allows for compilation of python-based
services and tools.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires httpretty nose mock

%description -n python3-module-%oname-tests
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
uranium is a build system that allows for compilation of python-based
services and tools.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/example*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/example*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/example*
%exclude %python3_sitelibdir/*/*/example*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/example*
%python3_sitelibdir/*/*/example*
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.49-alt1.git20150203
- Version 0.0.49

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.39-alt1.git20150126
- Version 0.0.39

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.37-alt1.git20150125
- Version 0.0.37

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.26-alt1.git20150119
- New snapshot

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.26-alt1.git20150118
- Initial build for Sisyphus

