%define oname enzyme

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.2
Release: alt1.dev.git20131128.1
Summary: Python video metadata parser
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/enzyme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Diaoul/enzyme.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-yaml
#BuildPreReq: python-module-sphinx-devel diaoul-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-yaml
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: diaoul-sphinx-themes python-module-alabaster python-module-chardet python-module-docutils python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-objects.inv python-module-pytest python-module-yaml python3-module-chardet python3-module-pytest python3-module-urllib3 python3-module-yaml rpm-build-python3 time

%description
Enzyme is a Python module to parse video metadata.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Enzyme is a Python module to parse video metadata.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python video metadata parser
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Enzyme is a Python module to parse video metadata.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Enzyme is a Python module to parse video metadata.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Enzyme is a Python module to parse video metadata.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Enzyme is a Python module to parse video metadata.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

rm -fR docs/_themes
cp -fR %_datadir/diaoul-sphinx-themes docs/_themes
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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.dev.git20131128.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev.git20131128
- Initial build for Sisyphus

