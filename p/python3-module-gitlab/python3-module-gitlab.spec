%define _unpackaged_files_terminate_build 1
%define module_name gitlab
%define pypi_name python-gitlab
%def_with check

Name: python3-module-%module_name
Version: 5.2.0
Release: alt2
Summary: A python wrapper for the GitLab API
License: LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/python-gitlab
VCS: https://github.com/python-gitlab/python-gitlab

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(gql)
BuildRequires: python3(httpx)
BuildRequires: python3(respx)
BuildRequires: python3(responses)
BuildRequires: python3(requests)
BuildRequires: python3(requests_toolbelt)
BuildRequires: python3(pytest)
%endif

Conflicts: gitlab

%py3_provides %pypi_name

%description
Python package providing access to the GitLab server API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rv tests/{install,functional,smoke}
%pyproject_run_pytest

%files
%_bindir/%module_name
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Dec 25 2024 Alexander Makeenkov <amakeenk@altlinux.org> 5.2.0-alt2
- Added conflict with gitlab package.

* Sat Dec 21 2024 Alexander Makeenkov <amakeenk@altlinux.org> 5.2.0-alt1
- Updated to version 5.2.0.

* Sat Jan 20 2024 Alexander Makeenkov <amakeenk@altlinux.org> 4.4.0-alt1
- Updated to version 4.4.0.

* Thu Dec 28 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.3.0-alt1
- Updated to version 4.3.0.

* Thu Dec 21 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.2.0-alt1
- Updated to version 4.2.0.

* Thu Mar 09 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.13.0-alt2
- Disabled tests

* Wed Feb 08 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.13.0-alt1
- Updated to version 3.13.0

* Wed Jan 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.12.0-alt1
- Updated to version 3.12.0
- Enabled tests

* Tue Jul 26 2022 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.0-alt1
- Initial build for ALT
