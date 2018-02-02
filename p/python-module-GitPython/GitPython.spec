%define oname GitPython

%def_with python3

Name: python-module-GitPython
Version: 2.1.5
Release: alt1.1

Summary: GitPython is a python library used to interact with Git repositories

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

# https://github.com/gitpython-developers/GitPython.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildArch: noarch

%setup_python_module %oname

BuildRequires: python-module-setuptools python-module-GitDB python-module-ddt python-module-mock
BuildRequires: git-core
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-gitdb python3-module-ddt python3-module-mock
%endif

Requires: git-core

%description
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%package -n python3-module-%oname
Summary: GitPython is a python library used to interact with Git repositories
Group: Development/Python3
Requires: git-core

%description -n python3-module-%oname
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%prep
%setup
%patch1 -p1

# needed for tests
git config --global user.email "darktemplar at altlinux.org"
git config --global user.name "darktemplar"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
py.test ||:
%if_with python3
pushd ../python3
py.test3 ||:
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/git/test

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/git/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- Updated to upstream version 2.1.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1rc1.2
- Fixed build

* Mon Jul 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1rc1.1
- merge upstream/master

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt0rc1.1
- 0.3.2-rc1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4.1-alt1.1
- Rebuilt with python 2.6

* Fri Nov 28 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.1.4.1-alt1
- Initial build for ALTLinux Sisyphus

