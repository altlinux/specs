%define oname setuptools_scm

%def_with python3

Name: python-module-%oname
Version: 1.7.0
Release: alt1.git20150812.1
Summary: The blessed package to manage your versions by scm tags
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/setuptools_scm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pypa/setuptools_scm.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: git mercurial
#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
Requires: git mercurial
%py_requires setuptools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: git-core mercurial python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

It uses metadata from the SCM to generate the version of a project and
is able to list the files belonging to that project (which makes the
MANIFEST.in file unnecessary in many cases).

It falls back to PKG-INFO/.hg_archival.txt when necessary.

%if_with python3
%package -n python3-module-%oname
Summary: The blessed package to manage your versions by scm tags
Group: Development/Python3
%py3_provides %oname
Requires: git mercurial
%py3_requires setuptools

%description -n python3-module-%oname
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

It uses metadata from the SCM to generate the version of a project and
is able to list the files belonging to that project (which makes the
MANIFEST.in file unnecessary in many cases).

It falls back to PKG-INFO/.hg_archival.txt when necessary.
%endif

%prep
%setup

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
python setup.py egg_info
%python_install

%if_with python3
pushd ../python3
python3 setup.py egg_info
%python3_install
popd
%endif

%check
python setup.py test
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150812
- Version 1.7.0

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150723
- Version 1.6.0

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

