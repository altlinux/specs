%define oname prompt_toolkit

%def_with python3

Name: python-module-%oname
Version: 1.0.14
Release: alt1.1
Summary: Library for building powerful interactive command lines in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/prompt_toolkit

# https://github.com/jonathanslenders/python-prompt-toolkit.git
Source: %name-%version.tar
BuildArch: noarch

%add_findreq_skiplist %python_sitelibdir/%oname/eventloop/win32.py
%add_findreq_skiplist %python3_sitelibdir/%oname/eventloop/win32.py
%add_findreq_skiplist %python_sitelibdir/%oname/terminal/win32_input.py
%add_findreq_skiplist %python3_sitelibdir/%oname/terminal/win32_input.py

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: time python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python-module-setuptools python-module-wcwidth
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-setuptools python3-module-sphinx python3-module-wcwidth
BuildRequires: python3-module-pytest
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
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Update to upstream release 1.0.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.46-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.46-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt1.git20150808
- Initial build for Sisyphus

