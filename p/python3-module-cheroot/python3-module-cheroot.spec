%define modulename cheroot

%def_with check
# Nessesary for cherrypy
%def_with tests

Name:    python3-module-%modulename
Version: 11.1.1
Release: alt1

Summary: Cheroot is the high-performance, pure-Python HTTP server used by CherryPy
License: BSD-3-Clause
Group:   Development/Python
URL:     https://pypi.org/project/cheroot
VCS:     https://github.com/cherrypy/cheroot

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build
%if_with check
BuildRequires: python3(pytest_cov)
%add_pyproject_deps_check_filter pypytools pytest-clarity
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif
BuildArch: noarch

%description
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.

%package tests
Summary: Tests for Cheroot
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for Cheroot

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dependencies/tests.in
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
%if_without tests
rm -rf %python3_sitelibdir/%{modulename}/test
rm -f %python3_sitelibdir/%{modulename}/testing.py
%endif

%check
# see cheroot/test/conftest.py
export HTTP_REQUEST_TIMEOUT=3
%pyproject_run_pytest -vra

%files
%_bindir/cheroot
%python3_sitelibdir/%modulename-%version.dist-info
%python3_sitelibdir/%{modulename}*
%exclude %python3_sitelibdir/%{modulename}/test
%exclude %python3_sitelibdir/%{modulename}/testing.py

%if_with tests
%files tests
%python3_sitelibdir/%{modulename}/test
%python3_sitelibdir/%{modulename}/testing.py
%endif

%changelog
* Thu Nov 06 2025 Anton Farygin <rider@altlinux.com> 11.1.1-alt1
- 10.0.1 -> 11.1.1

* Wed May 28 2025 Stanislav Levin <slev@altlinux.org> 10.0.1-alt4
- Fixed FTBFS (an attempt to workaround flaky tests).

* Wed Dec 11 2024 Anton Vyatkin <toni@altlinux.org> 10.0.1-alt3
- Fixed FTBFS.

* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 10.0.1-alt2
- Built with tests.
- Built with check.

* Thu Apr 25 2024 Andrey Cherepanov <cas@altlinux.org> 10.0.1-alt1
- New version.

* Sun May 21 2023 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Sun Nov 20 2022 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.
- Disabled tests packaging.

* Tue Jan 04 2022 Andrey Cherepanov <cas@altlinux.org> 8.6.0-alt1
- New version.

* Tue Jul 13 2021 Andrey Cherepanov <cas@altlinux.org> 8.5.2-alt1
- New version.
- Disable %%check for all architectures (ALT #40332).

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 8.2.1-alt1
- 8.2.1

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 7.0.0-alt1
- removed python-2.7 support
- added tests

* Thu Sep 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.8-alt1
- New version.

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.7-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.6-alt1
- New version.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.5-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.4-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 6.5.3-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 6.5.2-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.3-alt1
- New version.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.2-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.1-alt2
- Require module instead of package.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.1-alt1
- Initial build for Sisyphus
