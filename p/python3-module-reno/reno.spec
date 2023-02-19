%define oname reno
%def_without check
%def_without docs

Name: python3-module-%oname
Version: 3.5.0
Release: alt1.1

Summary: RElease NOtes manager

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/reno

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-packaging >= 20.4

%if_with check
BuildRequires: python3-module-stestr
BuildRequires: python3-module-dulwich >= 0.15.0
BuildRequires: gnupg
BuildRequires: git-core
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
%endif

%description
Reno is a release notes manager for storing
release notes in a git repository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

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
%__python3 -m stestr --test-path %oname/tests run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/%oname
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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.
- Renamed spec file.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Build new version.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- NMU: new version 3.2.0 (with rpmrb script)

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.11.3-alt1
- Automatically updated to 2.11.3.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 2.11.2-alt1
- 2.11.2

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- add git to requires

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
