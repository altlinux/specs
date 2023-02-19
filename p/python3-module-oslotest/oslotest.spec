%define oname oslotest
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.5.0
Release: alt4.1

Summary: OpenStack Oslo test framework

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslotest

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-six >= 1.10.0

%if_with check
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-hacking >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
The Oslo Test framework provides common fixtures, support for debugging,
and better support for mocking results.

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

pushd %buildroot%_bindir
for i in $(ls); do
       sed -i 's|python|python3|g' $i
       sed -i 's|python33|python3|g' $i
       sed -i 's|tox|tox.py3|g' $i
done
popd

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslo_debug_helper
%_bindir/oslo_run_cross_tests
%_bindir/oslo_run_pre_release_tests
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt4.1
- Moved on modern pyproject macros.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt4
- Fixed watch file.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt2
- Added manual.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.
- Unified.

* Thu Mar 31 2022 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt2.1
- Fixed build.

* Fri Jul 30 2021 Ivan A. Melnikov <iv@altlinux.org> 4.2.0-alt2
- Enable %%check.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.

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

