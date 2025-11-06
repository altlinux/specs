%define modname anytree
%def_enable check

Name: python-module-%modname
Version: 2.13.0
Release: alt2
Epoch: 1

Summary: Python Tree Data Structure Library
Group: Development/Python
License: Apache-2.0
Url: https://pypi.org/project/anytree
VCS: https://github.com/c0fec0de/anytree

# Source-url: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz
Source: %modname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pdm-backend
%if_enabled check
BuildRequires: python3-module-pytest-cov python3-module-test2ref python3-module-yaml
%endif

%description
Python module to manipulate tree data structures

%package -n python3-module-%modname
Summary: Python Tree Data Structure Library
Group: Development/Python3

%description -n python3-module-%modname
Python3 module to manipulate tree data structures

%prep
%setup -n %modname-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%if_enabled check
%check
%pyproject_run_pytest
%endif

%files -n python3-module-%modname
%doc README.rst LICENSE
%python3_sitelibdir_noarch/%{modname}*/

%changelog
* Thu Nov 06 2025 Leontiy Volodin <lvol@altlinux.org> 1:2.13.0-alt2
- Enabled check.

* Thu Oct 30 2025 Leontiy Volodin <lvol@altlinux.org> 1:2.13.0-alt1
- New version 2.13.0.
- Added VCS tag.

* Tue Jul 04 2023 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt1
- 3.0.0.
- Disabled python2 build again (by upstream) (ALT #44959).

* Thu Jul 28 2022 Leontiy Volodin <lvol@altlinux.org> 2.8.0-alt2
- Returned python2 build for mlnx-tools (ALT #41412, #43337).

* Tue Nov 23 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.0-alt1.1
- Returned into Sisyphus as require for mlnx-tools.

* Wed Jan 15 2020 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3
- disabled python2 build

* Mon Feb 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Feb 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- first build for Sisyphus



