%define modulename cheroot

# there is no ipv6 support on our build system and cheroot tests do not support this configuration
# ERROR: Could not find a version that satisfies the requirement pytest-cov==2.10.1
%def_disable check
%def_without tests

Name:    python3-module-%modulename
Version: 9.0.0
Release: alt1

Summary: Cheroot is the high-performance, pure-Python HTTP server used by CherryPy
License: BSD
Group:   Development/Python
URL:     https://github.com/cherrypy/cheroot

Source: %name-%version.tar 
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools_scm
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-testmon
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-sugar
BuildRequires: python3-module-pytest-watch
BuildRequires: python3-module-jaraco.functools
BuildRequires: python3-module-trustme
BuildRequires: python3-module-requests-unixsocket
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-OpenSSL
%if_enabled check
BuildRequires: python3-module-jaraco.text
BuildRequires: python3-module-jaraco.context
BuildRequires: python3-module-portend
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-pytest-cov
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

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
%if_without tests
rm -rf %python3_sitelibdir/%{modulename}/test
rm -f %python3_sitelibdir/%{modulename}/testing.py
%endif

%check
rm -f pyproject.toml
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%_bindir/cheroot
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%{modulename}*
%exclude %python3_sitelibdir/%{modulename}/test
%exclude %python3_sitelibdir/%{modulename}/testing.py

%if_with tests
%files tests
%python3_sitelibdir/%{modulename}/test
%python3_sitelibdir/%{modulename}/testing.py
%endif

%changelog
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
