%define oname flaky

Name: python3-module-%oname
Version: 3.7.0
Release: alt1
Summary: Plugin for nose or py.test that automatically reruns flaky tests
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/flaky
BuildArch: noarch

# https://github.com/box/flaky.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-mock python3-module-genty python3-module-nose

%description
Flaky is a plugin for nose or py.test that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely
on components that aren't 100%% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
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
