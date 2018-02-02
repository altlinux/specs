%define oname linecache2

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150306.2.1
Summary: Backports of the linecache module
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/linecache2

# https://github.com/testing-cabal/linecache2.git
Source: %name-%version.tar
BuildArch: noarch
Patch1: %oname-%version-alt-build.patch

#BuildPreReq: python-devel python-module-setuptools git
#BuildPreReq: python-module-fixtures python-module-unittest2
#BuildPreReq: python-module-mimeparse
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-fixtures python3-module-unittest2
#BuildPreReq: python3-module-mimeparse
%endif

%py_provides %oname

%add_findreq_skiplist %python_sitelibdir/%oname/tests/inspect_fodder2.py

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-pbr python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-testtools python3-module-traceback2 python3-module-unittest2
BuildRequires: git-core
BuildRequires: python-module-fixtures  python-module-setuptools  python-module-pbr  python-module-unittest2
%if_with python3
BuildRequires: python3-module-fixtures python3-module-setuptools python3-module-pbr python3-module-unittest2 python3-module-html5lib
%endif

%description
A backport of linecache to older supported Pythons.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A backport of linecache to older supported Pythons.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Backports of the linecache module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A backport of linecache to older supported Pythons.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A backport of linecache to older supported Pythons.

This package contains tests for %oname.
%endif

%prep
%setup
%patch1 -p1

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

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
python -m unittest2 -v
%if_with python3
pushd ../python3
python3 -m unittest2 -v
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.git20150306.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.git20150306.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150306.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20150306.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150306
- Initial build for Sisyphus

