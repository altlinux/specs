%define mname kids
%define oname %mname.test

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150204.1
Summary: Kids test library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.test/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.test.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-d2to1 python-module-coverage
#BuildPreReq: python-module-nose python-module-minimock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests git
#BuildPreReq: python3-module-d2to1 python3-module-coverage
#BuildPreReq: python3-module-nose python3-module-minimock
%endif

%py_provides %oname
%py_requires %mname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: git-core python-module-coverage python-module-d2to1 python-module-minimock python-module-nose python-module-setuptools-tests python3-module-coverage python3-module-d2to1 python3-module-minimock python3-module-nose python3-module-setuptools-tests rpm-build-python3 time

%description
kids.test is a Python library providing helpers when writing tests in
python. It's part of 'Kids' (for Keep It Dead Simple) library.

%package -n python3-module-%oname
Summary: Kids test library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname

%description -n python3-module-%oname
kids.test is a Python library providing helpers when writing tests in
python. It's part of 'Kids' (for Keep It Dead Simple) library.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst TODO
%python_sitelibdir/%mname/test
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/%mname/test
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20150204.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150204
- Initial build for Sisyphus

