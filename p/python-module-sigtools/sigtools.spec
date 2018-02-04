%define oname sigtools

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.b2.git20150217.1.1
Summary: Python module to manipulate function signatures
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sigtools/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/epsy/sigtools.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-funcsigs
#BuildPreReq: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-funcsigs
#BuildPreReq: python3-module-sphinx
%endif

%py_provides %oname
%py_requires six funcsigs sphinx

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer
BuildRequires: python-module-docutils python-module-funcsigs python-module-html5lib python-module-setuptools python-module-sphinx python3-module-html5lib python3-module-jinja2-tests python3-module-setuptools python3-module-sphinx rpm-build-python3

%description
Utilities for working with 3.3's inspect.Signature objects.
The sigtools python library provides:

* Decorators to specify keyword-only parameters, annotations and
  positional-only parameters, even on python2: sigtools.modifiers
* Decorators to specify how *args, **kwargs are handled, in a way that
  can be introspected: sigtools.specifiers
* Function combination routines that preserve signatures:
  sigtools.wrappers
* Functions to manipulate signature objects likewise: sigtools.signatures

%package -n python3-module-%oname
Summary: Python module to manipulate function signatures
Group: Development/Python3
%py3_provides %oname
%py3_requires six funcsigs sphinx

%description -n python3-module-%oname
Utilities for working with 3.3's inspect.Signature objects.
The sigtools python library provides:

* Decorators to specify keyword-only parameters, annotations and
  positional-only parameters, even on python2: sigtools.modifiers
* Decorators to specify how *args, **kwargs are handled, in a way that
  can be introspected: sigtools.specifiers
* Function combination routines that preserve signatures:
  sigtools.wrappers
* Functions to manipulate signature objects likewise: sigtools.signatures

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.b2.git20150217.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.b2.git20150217.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt2.b2.git20150217
- NMU: added python-module-sphinx to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.b2.git20150217.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b2.git20150217
- Version 0.1b2

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.git20150111
- Initial build for Sisyphus

