%define oname js.bootstrap_select

%def_with python3

Name: python-module-%oname
Version: 1.5.2
Release: alt1.git20140516.1
Summary: Fanstatic packaging of bootstrap-select.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.bootstrap_select/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tmassman/js.bootstrap_select.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-fanstatic python-module-js.bootstrap
#BuildPreReq: python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-fanstatic python3-module-js.bootstrap
#BuildPreReq: python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js js.bootstrap

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-fanstatic python-module-js python-module-js.query python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-module-shutilwhich python-module-webob python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-fanstatic python3-module-js python3-module-js.query python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools python3-module-webob xz
BuildRequires: python-module-js.bootstrap python-module-setuptools-tests python3-module-js.bootstrap python3-module-setuptools-tests rpm-build-python3 time

%description
This library packages bootstrap select for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of bootstrap-select.js
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.bootstrap

%description -n python3-module-%oname
This library packages bootstrap select for fanstatic.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.2-alt1.git20140516.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140516
- Initial build for Sisyphus

