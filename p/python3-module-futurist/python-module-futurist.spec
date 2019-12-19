%define oname futurist

Name: python3-module-%oname
Version: 1.10.0
Release: alt1
Summary: Useful additions to futures, from the future
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/futurist
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

Requires: python3-module-monotonic >= 0.6
Requires: python3-module-contextlib2 >= 0.4.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-contextlib2 >= 0.4.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-openstackdocstheme

%description
Code from the future, delivered to you in the now.

%package doc
Summary: Documentation for futurist library
Group: Development/Documentation

%description doc
Documentation for futurist library.

%package tests
Summary: Tests for futurist library
Group: Development/Python3
BuildArch: noarch

%description tests
Tests for futurist library.

%prep
%setup -n %oname-%version

%build
%python3_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- Automatically updated to 1.10.0.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Automatically updated to 1.8.1

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.0-alt1
- 0.21.0
- add tests package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial package.
