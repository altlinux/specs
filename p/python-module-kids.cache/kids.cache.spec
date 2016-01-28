%define mname kids
%define oname %mname.cache

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150202.1
Summary: Kids caching library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.cache.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-d2to1 python-module-nose
#BuildPreReq: python-module-cachetools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests git
#BuildPreReq: python3-module-d2to1 python3-module-nose
#BuildPreReq: python3-module-cachetools
%endif

%py_provides %oname
%py_requires %mname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: git-core python-module-d2to1 python-module-nose python-module-setuptools-tests python3-module-d2to1 python3-module-nose python3-module-setuptools-tests rpm-build-python3

%description
kids.cache is a Python library providing a cache decorator. It's part of
'Kids' (for Keep It Dead Simple) library.

It main concern is to offer a very simple default usage. Without
forgetting to offer power inside when needed.

%package -n python3-module-%oname
Summary: Kids caching library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname

%description -n python3-module-%oname
kids.cache is a Python library providing a cache decorator. It's part of
'Kids' (for Keep It Dead Simple) library.

It main concern is to offer a very simple default usage. Without
forgetting to offer power inside when needed.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
%endif

%build
./autogen.sh
%python_build_debug

%if_with python3
pushd ../python3
./autogen.sh
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/cache
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/cache
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1.git20150202.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150202
- Initial build for Sisyphus

