%define oname selectors34

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.git20150715.1.1
Summary: Backport of the selectors module from Python 3.4
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/selectors34
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/berkerpeksag/selectors34.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-mock
%endif

%py_provides %oname selectors
%py_requires six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-funcsigs python-module-linecache2 python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-module-six python-module-traceback2 python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-linecache2 python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-traceback2 xz
BuildRequires: python-module-mock python-module-setuptools-tests python3-module-html5lib python3-module-pbr python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
selectors34 is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-Fran??ois Natali. This port is based
on Victor Stinner's trollius/selectors.py port.

%if_with python3
%package -n python3-module-%oname
Summary: Backport of the selectors module from Python 3.4
Group: Development/Python3
%py3_provides %oname selectors
%py3_requires six

%description -n python3-module-%oname
selectors34 is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-Fran??ois Natali. This port is based
on Victor Stinner's trollius/selectors.py port.
%endif

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
ln -s %oname.py %buildroot%python_sitelibdir/selectors.py

%if_with python3
pushd ../python3
%python3_install
popd
ln -s %oname.py %buildroot%python3_sitelibdir/selectors.py
%endif

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "import selectors"
python setup.py test -v
py.test -vv tests/
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "import selectors"
python3 setup.py test -v
py.test-%_python3_version -vv tests/
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150715.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.git20150715.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150715
- Initial build for Sisyphus

