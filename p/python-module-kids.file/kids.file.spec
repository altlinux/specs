%define mname kids
%define oname %mname.file

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150120.1.1
Summary: Kids file management library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.file.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-d2to1 python-module-nose
#BuildPreReq: python-module-minimock python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-d2to1 python3-module-nose
#BuildPreReq: python3-module-minimock python3-module-coverage
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: git-core python-module-coverage python-module-d2to1 python-module-minimock python-module-nose python-module-setuptools-tests python3-module-coverage python3-module-d2to1 python3-module-minimock python3-module-nose python3-module-setuptools-tests rpm-build-python3 time

%description
This very small module is part of KIDS (Keep It Dead Simple), and
propose some python coding shorcuts on very common tasks. Original tasks
I've shortcuted often requires to know 2 to 10 lines of python or
special cases or different modules location.

%package -n python3-module-%oname
Summary: Kids file management library
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR

%description -n python3-module-%oname
This very small module is part of KIDS (Keep It Dead Simple), and
propose some python coding shorcuts on very common tasks. Original tasks
I've shortcuted often requires to know 2 to 10 lines of python or
special cases or different modules location.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag "%version" -m "%version"

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
#exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
#python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1.git20150120.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150120
- Initial build for Sisyphus

