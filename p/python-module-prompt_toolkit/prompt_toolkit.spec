%define oname prompt_toolkit

%def_with python3

Name: python-module-%oname
Version: 0.46
Release: alt1.git20150808
Summary: Library for building powerful interactive command lines in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/prompt_toolkit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jonathanslenders/python-prompt-toolkit.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pygments python-module-six
BuildPreReq: python-module-wcwidth
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Pygments python3-module-six
BuildPreReq: python3-module-wcwidth
%endif

%py_provides %oname
%py_requires pygments six wcwidth
%add_python_req_skip asyncio

%description
prompt_toolkit is a library for building powerful interactive command
lines in Python.

%if_with python3
%package -n python3-module-%oname
Summary: Library for building powerful interactive command lines in Python
Group: Development/Python3
%py3_provides %oname
%py3_requires pygments six wcwidth

%description -n python3-module-%oname
prompt_toolkit is a library for building powerful interactive command
lines in Python.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
prompt_toolkit is a library for building powerful interactive command
lines in Python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
prompt_toolkit is a library for building powerful interactive command
lines in Python.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
python tests/run_tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 tests/run_tests.py -v
popd
%endif

%files
%doc CHANGELOG *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/_build/html

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt1.git20150808
- Initial build for Sisyphus

