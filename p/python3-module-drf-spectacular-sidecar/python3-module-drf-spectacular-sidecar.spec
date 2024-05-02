%define pypi_name drf-spectacular-sidecar
%define mod_name drf_spectacular_sidecar

# upstream doesn't provide tests
%def_without check

Name: python3-module-%pypi_name
Version: 2024.5.1
Release: alt1

Summary: Serve self-contained distribution builds of Swagger UI and Redoc with Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/drf-spectacular-sidecar
Vcs: https://github.com/tfranzel/drf-spectacular-sidecar
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu May 02 2024 Anton Vyatkin <toni@altlinux.org> 2024.5.1-alt1
- New version 2024.5.1.

* Tue Apr 09 2024 Anton Vyatkin <toni@altlinux.org> 2024.4.1-alt1
- New version 2024.4.1.

* Tue Mar 05 2024 Anton Vyatkin <toni@altlinux.org> 2024.3.4-alt1
- New version 2024.3.4.

* Fri Mar 01 2024 Anton Vyatkin <toni@altlinux.org> 2024.3.1-alt1
- New version 2024.3.1.

* Thu Feb 01 2024 Anton Vyatkin <toni@altlinux.org> 2024.2.1-alt1
- New version 2024.2.1.

* Tue Jan 02 2024 Anton Vyatkin <toni@altlinux.org> 2024.1.1-alt1
- New version 2024.1.1.

* Mon Dec 04 2023 Anton Vyatkin <toni@altlinux.org> 2023.12.1-alt1
- New version 2023.12.1.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 2023.11.1-alt1
- New version 2023.11.1.

* Wed Oct 04 2023 Anton Vyatkin <toni@altlinux.org> 2023.10.1-alt1
- Initial build for Sisyphus
