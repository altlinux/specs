%define  modulename portend

%def_with check

Name:    python3-module-%modulename
Version: 3.2.0
Release: alt1

Summary: Use portend to monitor TCP ports for bound or unbound states

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/portend
VCS:     https://github.com/jaraco/portend

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-tempora
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Tue Jul 04 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.
- Build with check.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 2.6-alt2
- Rename package, cleanup spec.

* Sun May 31 2020 Andrey Cherepanov <cas@altlinux.org> 2.6-alt1
- New version.

* Thu Jun 13 2019 Andrey Cherepanov <cas@altlinux.org> 2.5-alt1
- New version.

* Wed Apr 24 2019 Andrey Cherepanov <cas@altlinux.org> 2.4-alt2
- Build only for python3.

* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1
- Initial build for Sisyphus
