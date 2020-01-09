%define oname oslotest

%def_disable check

Name: python3-module-%oname
Version: 3.9.0
Release: alt1
Summary: OpenStack test framework
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/oslotest/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslotest.watch
BuildArch: noarch

BuildRequires: git-core

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-subunit
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-testrepository
BuildRequires: python3-module-testscenarios
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-mox3 >= 0.20.0
BuildRequires: python3-module-hacking
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mimeparse
BuildRequires: python3-module-mccabe
BuildRequires: python3-module-flake8
BuildRequires: python3-pyflakes
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-requests
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-reno
BuildRequires: python3-module-oslo.config

%py3_provides %oname

%description
OpenStack test framework and test fixtures.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
OpenStack test framework and test fixtures.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
OpenStack test framework and test fixtures.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version
rm -rf {test-,}requirements.txt

%build
%python3_build

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%install
%python3_install
pushd %buildroot%_bindir
for i in $(ls); do
       sed -i 's|python|python3|g' $i
       sed -i 's|python33|python3|g' $i
       sed -i 's|tox|tox.py3|g' $i
done
popd

%check
python3 setup.py test
py.test-%_python3_version

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 3.9.0-alt1
- Automatically updated to 3.9.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Automatically updated to 3.8.1.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141105
- Initial build for Sisyphus

