%define oname 2gis

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20140722
Summary: 2gis library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/2gis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/svartalf/python-2gis.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-six
BuildPreReq: python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-six
BuildPreReq: python3-module-mock
%endif

%py_provides dgis
%py_requires requests six

%description
A Python library for accessing the 2gis API.

%package -n python3-module-%oname
Summary: 2gis library for Python
Group: Development/Python3
%py3_provides dgis
%py3_requires requests six

%description -n python3-module-%oname
A Python library for accessing the 2gis API.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A Python library for accessing the 2gis API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A Python library for accessing the 2gis API.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140722
- Initial build for Sisyphus

