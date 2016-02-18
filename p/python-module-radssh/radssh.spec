%define oname radssh

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1.git20150714.1
Summary: RadSSH Module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/radssh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/radssh/radssh.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-paramiko python-module-netaddr
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-paramiko python3-module-netaddr
%endif

%py_provides %oname
%py_requires paramiko netaddr
%add_python_req_skip genders

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-ecdsa python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pycrypto python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-ecdsa python3-module-pycrypto python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-netaddr python-module-objects.inv python-module-paramiko python-module-setuptools-tests python3-module-netaddr python3-module-paramiko python3-module-setuptools-tests rpm-build-python3 time

%description
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: RadSSH Module
Group: Development/Python3
%py3_provides %oname
%py3_requires paramiko netaddr
%add_python3_req_skip genders

%description -n python3-module-%oname
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README *.md api_sample
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README *.md api_sample
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.git20150714.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150714
- Version 1.0.5

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150203
- Initial build for Sisyphus

