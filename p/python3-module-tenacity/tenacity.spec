%define oname tenacity

%def_with check

Name: python3-module-%oname
Version: 9.2.1
Release: alt1

Summary: Retrying library for Python

Group: Development/Python3
License: Apache-2.0
Url: https://tenacity.readthedocs.io
VCS: https://github.com/jd/tenacity

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tornado
# optional in tests/test_asyncio.py, but exercises the trio support of 9.x
BuildRequires: python3-module-trio
%endif

%description
Tenacity is an Apache 2.0  licensed general-purpose retrying library, written in
Python, to simplify the task of adding retry behavior to just about anything. It
originates from a fork of retrying which is sadly no longer maintained. Tenacity
isn't api  compatible with retrying  but adds significant new  functionality and
fixes a number of longstanding bugs.

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Oct 07 2026 Egor Ignatov <egori@altlinux.org> 9.2.1-alt1
- New version 9.2.1.

* Mon Sep 28 2026 Egor Ignatov <egori@altlinux.org> 9.2.0-alt1
- New version 9.2.0.
- Switched to building from upstream git.
- Fixes FTBFS under python3 3.14 (closes: #60618).

* Sun Jul 28 2024 Grigory Ustinov <grenka@altlinux.org> 8.5.0-alt1
- Build new version.

* Mon Apr 25 2022 Grigory Ustinov <grenka@altlinux.org> 8.0.1-alt1
- Build new version.
- Build with check.

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.12.0-alt2
- Drop python2 support.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.12.0-alt1
- 4.12.0

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- initial build

