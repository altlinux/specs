%define oname stevedore

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.5.0
Release: alt1

Summary: Manage dynamic plugins for Python applications

Group: Development/Python3
License: Apache-2.0
URL: http://docs.openstack.org/developer/stevedore/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: stevedore.watch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinx-devel
%endif

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%py3_provides %oname

%description
Manage dynamic plugins for Python applications

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Manage dynamic plugins for Python applications

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Manage dynamic plugins for Python applications

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Manage dynamic plugins for Python applications

This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

%if_with docs
%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/
%endif

%build
%python3_build

%if_with docs
export PYTHONPATH=$PWD
export PBR_VERSION=$(pbr --version)
sphinx-build-3 doc/source html
sphinx-build-3 doc/source pickle
%endif

%install
%python3_install

%if_with docs
cp -fR pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=$PWD
# use pytest instead of stestr to break a build cycle between python-cliff, python-stestr and python-stevedore
%__python3 -m pytest stevedore/tests -k "not test_extension"

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/example
%exclude %python3_sitelibdir/%oname/example2
%exclude %python3_sitelibdir/%oname/tests
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc html/*
%endif

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/example
%python3_sitelibdir/%oname/example2

%changelog
* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Thu Mar 31 2022 Grigory Ustinov <grenka@altlinux.org> 1.32.0-alt3.2
- Fixed BuildRequires.

* Fri Jan 28 2022 Ivan A. Melnikov <iv@altlinux.org> 1.32.0-alt3.1
- Enable %%check.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.32.0-alt3
- Fixed BuildRequires.

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.32.0-alt2
- NMU: move example2 to tests subpackage (fix tests subpackage requires)

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.32.0-alt1
- Automatically updated to 1.32.0.
- Renamed spec file.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.31.0-alt2
- Build without python2.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.31.0-alt1
- Automatically updated to 1.31.0.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.30.1-alt1
- Automatically updated to 1.30.1

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.29.0-alt2
- Dropped dependency on python argparse (use stdlib's one).

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.29.0-alt1
- 1.29.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.20.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.20.1-alt1
- 1.20.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Avoid requirement on pbr in egg-info

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added module for Python 3
- Added docs
- Moved tests into separate package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.14-alt1
- First build for ALT (based on Fedora 0.14-1.fc21.src)

