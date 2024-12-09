%define _unpackaged_files_terminate_build 1
%define pypi_name loguru
%def_with check

Name: python3-module-%pypi_name
Version: 0.7.3
Release: alt1
Summary: Python logging made (stupidly) simple
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/loguru
VCS: https://github.com/Delgan/loguru

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-colorama
BuildRequires: python3-module-flit-core
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest-mypy-plugins
%endif

%description
Loguru is a library which aims to bring enjoyable logging in Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Dec 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt1
- Updated to version 0.7.3.

* Tue Sep 12 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.2-alt1
- Updated to version 0.7.2.

* Mon Jun 19 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.0-alt2
- Builded for ppc64le arch, but skipped tests for it (closes: #46589)

* Sat Jun 17 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.0-alt1
- Updated to version 0.7.0

* Sun Mar 05 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt1.gitc926fd0
- Initial build for ALT
