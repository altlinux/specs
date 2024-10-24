%define  modulename multipart

%def_with check

Name:    python3-module-%modulename
Version: 1.1.0
Release: alt1

Summary: Multipart parser for Python3

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/multipart
VCS:     https://github.com/defnull/multipart

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__/%{modulename}*
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Sat Oct 05 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Wed Sep 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Wed Aug 21 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt1
- Automatically updated to 0.2.5.
- Built with check.

* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus.
