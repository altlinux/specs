%define oname GitPython

%def_disable check

Name: python3-module-%oname
Version: 3.1.14
Release: alt1

Summary: GitPython is a python library used to interact with Git repositories

License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/GitPython/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch1: %oname-alt-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

#BuildRequires: git-core

BuildRequires: python3-module-setuptools python3(gitdb) python3-module-ddt python3-module-mock

Requires: git-core

%description
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%prep
%setup
#patch1 -p1

%build
%python3_build

%install
%python3_install
%python3_prune

%check
# needed for tests
#git config --global user.email "darktemplar at altlinux.org"
#git config --global user.name "darktemplar"

rm -f .gitmodules

git init
git add -A
git commit -m "%version"
git tag %version -m "%version"

git tag 0.1.6 -m "0.1.6"

nosetests3

%files
%python3_sitelibdir/*

%changelog
* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.14-alt1
- new version
- build python3 module standalone

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.10-alt1
- Updated to upstream version 2.1.10.

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

