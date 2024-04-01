%define oname flaky

%def_with check

Name: python3-module-%oname
Version: 3.8.1
Release: alt1

Summary: Plugin for nose or py.test that automatically reruns flaky tests

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/flaky
VCS: https://github.com/box/flaky

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Flaky is a plugin for py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely
on components that aren't 100%% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%prep
%setup

# fix version
sed -i 's/3.7.0/%version/' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
# adapted from upstream's tox.ini
%pyproject_run_pytest -v -k 'example and not options' --doctest-modules test/test_pytest/
%pyproject_run_pytest -v -k 'example and not options' test/test_pytest/
%pyproject_run_pytest -v -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
%pyproject_run_pytest -v --force-flaky --max-runs 2 test/test_pytest/test_pytest_options_example.py

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Automatically updated to 3.8.1.

* Mon Mar 11 2024 Grigory Ustinov <grenka@altlinux.org> 3.8.0-alt1
- Automatically updated to 3.8.0.
- Built with check.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt2
- Removed nose dependency.

* Thu Sep 10 2020 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 3.6.1-alt2
- Drop python2 support.

* Thu Aug 08 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.1-alt1
- Build new version.

* Mon Jul 08 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Build new version.

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.3-alt1
- Build new version.

* Tue Jan 15 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.2-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.0-alt1
- Initial build for ALT.
