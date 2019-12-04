%define oname filedepot
%def_disable check

Name: python3-module-%oname
Version: 0.7.1
Release: alt1
Summary: Toolkit for storing files and attachments in web applications
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/filedepot/

# https://github.com/amol-/depot.git
Source: %name-%version.tar
Patch1: %oname-0.5.0-alt.patch

BuildRequires(pre): rpm-macros-sphinx3 python3-module-sphinx-sphinx-build-symlink
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-unittest2
BuildRequires: python3-module-TurboGears2
BuildRequires: python3-module-webtest
BuildRequires: python3-module-repoze.lru python3-module-yaml python3(requests)
BuildRequires: python3-module-ecdsa python3-module-pbr
BuildRequires: python3-module-sphinx

%description
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%py3_provides %oname depot
%py3_requires pymongo sqlalchemy PIL ming boto

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs html

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- 0.7.1
- disabled python2 version

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Updated to upstream version 0.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150209
- Initial build for Sisyphus

