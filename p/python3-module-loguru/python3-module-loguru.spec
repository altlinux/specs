%define _unpackaged_files_terminate_build 1
%define pypi_name loguru
%def_with check

Name: python3-module-%pypi_name
Version: 0.7.3
Release: alt5
Summary: Python logging made (stupidly) simple
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/loguru
VCS: https://github.com/Delgan/loguru

Source: %name-%version.tar
Patch: alt-fix-tests-with-mypy.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-colorama
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest-mypy-plugins
%endif

%description
Loguru is a library which aims to bring enjoyable logging in Python.

%prep
%setup
%patch -p1

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
* Wed Jun 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt5
- Fixed tests with mypy 2.0.0.

* Sat Apr 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt4
- Fixed tests with mypy 1.20.

* Fri Aug 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt3
- Fixed tests.

* Wed Dec 18 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt2
- Fixed BuildRequires.

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
