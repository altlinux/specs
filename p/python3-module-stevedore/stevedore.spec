%define oname stevedore
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.0.0
Release: alt1.1

Summary: Manage dynamic plugins for Python applications

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/stevedore

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
Python makes loading code dynamically easy, allowing you to configure and extend
your application by discovering and loading extensions ("plugins") at runtime.
Many applications implement their own library for doing this, using __import__
or importlib. stevedore avoids creating yet another extension mechanism
by building on top of setuptools entry points. The code for managing entry points
tends to be repetitive, though, so stevedore provides manager classes for
implementing common patterns for using dynamically loaded extensions.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run
#export PYTHONPATH=$PWD
# use pytest instead of stestr to break a build cycle between python-cliff, python-stestr and python-stevedore
#__python3 -m pytest stevedore/tests -k "not test_extension"

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/example
%exclude %python3_sitelibdir/%oname/example2

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/example
%python3_sitelibdir/%oname/example2

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

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

