%define oname setuptools_scm

%def_with python3

Name: python-module-%oname
Version: 1.15.0
Release: alt1.1.1
Summary: The blessed package to manage your versions by scm tags
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/setuptools_scm/
Packager: Python Development Team <python at packages.altlinux.org>

# https://github.com/pypa/setuptools_scm.git
Source: %name-%version.tar
BuildArch: noarch

%py_provides %oname
Requires: git-core mercurial
%py_requires setuptools

BuildRequires: python-module-setuptools git-core mercurial
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools rpm-build-python3
BuildRequires: python3-module-pytest
%endif

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
Requires: git-core mercurial
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

git config --global user.email "python at packages.altlinux.org"
git config --global user.name "Python Development Team"
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
py.test3 -vv
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 1.15.0-alt1.1
- R: git-core instead of full-blown git metapackage
- fix build --with python3 (actually the test)

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt1
- Version 1.15.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.git20150812.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150812
- Version 1.7.0

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150723
- Version 1.6.0

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

