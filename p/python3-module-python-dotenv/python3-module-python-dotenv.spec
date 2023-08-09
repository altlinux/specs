%define oname dotenv
%define pypi_name python-dotenv

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt3

Provides: python3-module-%oname = %EVR
Obsoletes: python3-module-%oname < 1.0.0-alt2

Summary: Reads the key-value pair from .env file and adds them to environment variable

License: BSD-3-Clause
Group: Development/Python
Url: https://github.com/theskumar/python-dotenv

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
BuildRequires: /dev/pts
BuildRequires: /proc
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Reads the key-value pair from .env file and adds them to environment
variable. It is great for managing app settings during development
and in production using 12-factor principles.

%prep
%setup -n %name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
# We don't support IPython for now (requires additional dependencies)
rm -f src/dotenv/ipython.py
%pyproject_build

%install
%pyproject_install

%check
# tests/test_docs.py:
# do not execute tests for docs
%pyproject_run_pytest -vra --deselect='tests/test_docs.py'

%files
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 09 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.0-alt3
- enabled the tests

* Mon Jul 31 2023 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt2
- rename package to use PyPI name
- incorporate changes from Alexander Shashkin (dutyrok@)

* Mon Mar 20 2023 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- new version

* Tue Feb 14 2023 Vladimir Didenko <cow@altlinux.org> 0.21.1-alt1
- new version

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 0.21.0-alt1
- new version

* Tue Mar 29 2022 Vladimir Didenko <cow@altlinux.org> 0.20.0-alt1
- new version

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.org> 0.19.2-alt1
- new version

* Fri Jul 30 2021 Vladimir Didenko <cow@altlinux.org> 0.19.0-alt1
- new version

* Wed May 26 2021 Vladimir Didenko <cow@altlinux.org> 0.17.1-alt1
- new version

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.org> 0.17.0-alt1
- new version

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 0.15.0-alt1
- new version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- new version

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- initial build for Sisyphus
