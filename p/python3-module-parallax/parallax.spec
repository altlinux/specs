%global oname parallax

Name: python3-module-%oname
Version: 1.0.8
Release: alt1
Summary: Execute commands and copy files over SSH to multiple machines at once

Group: Development/Python3
License: BSD-3-Clause
URL: https://pypi.org/project/parallax
# https://github.com/krig/parallax
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Execute commands and copy files over SSH to multiple machines at once.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md COPYING
%_bindir/parallax-askpass
%python3_sitelibdir/*

%changelog
* Thu Dec 01 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.8-alt1
- Build new version.

* Thu May 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt1
- Build new version.
- Fix license.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Build new version.
- Build without python2.

* Mon Sep 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build
