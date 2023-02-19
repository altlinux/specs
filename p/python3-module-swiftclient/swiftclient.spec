%define oname swiftclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.1.0
Release: alt2.1

Summary: OpenStack Object Storage API Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-swiftclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-requests >= 2.4.0

%if_with check
BuildRequires: python3-module-keystoneclient >= 0.7.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-mock >= 1.2.0
BuildRequires: python3-module-hacking >= 3.2.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-openstacksdk >= 0.11.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
There's a Python API (the swiftclient module), and a command-line script (swift).

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
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/swift.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/swift.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/swift
%python3_sitelibdir/%oname
%python3_sitelibdir/python_swiftclient-%version.dist-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/swift.bash_completion

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%_man1dir/swift.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.9.0-alt1
- Automatically updated to 3.9.0.
- Unify documentation building.
- Renamed spec file.
- Fix license.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Automatically updated to 3.8.1.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- new version 3.5.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem at altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1
- add python3 package

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- New version (based on Fedora 2.1.0-1.fc21.src)

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
