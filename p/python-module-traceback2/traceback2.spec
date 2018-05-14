%define oname traceback2

%def_disable check
%def_without bootstrap

Name: python-module-%oname
Version: 1.4.0
Release: alt2

Summary: Backports of the traceback module
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/traceback2
# https://github.com/testing-cabal/traceback2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: git-core python-module-contextlib2
BuildRequires: python-module-mimeparse python-module-pbr
BuildRequires: python-module-pytest

%if_with bootstrap
BuildRequires: python-module-unittest2
%endif

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-contextlib2 python3-module-html5lib
BuildPreReq: python3-module-mimeparse python3-module-pbr
BuildPreReq: python3-module-pytest

%if_with bootstrap
BuildPreReq: python3-module-unittest2
%endif

%py_provides %oname
%py_requires linecache2 six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools


%description
A backport of traceback to older supported Pythons.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A backport of traceback to older supported Pythons.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Backports of the traceback module
Group: Development/Python3
%py3_provides %oname
%py3_requires linecache2 six

%description -n python3-module-%oname
A backport of traceback to older supported Pythons.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A backport of traceback to older supported Pythons.

This package contains tests for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export LC_ALL=en_US.UTF-8
python setup.py test -v
rm -fR build
py.test -vv

pushd ../python3
python3 setup.py test -v
rm -fR build
py.test-%_python3_version -vv
popd

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.git20150309.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20150309
- Initial build for Sisyphus

