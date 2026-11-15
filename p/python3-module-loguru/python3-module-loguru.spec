%define _unpackaged_files_terminate_build 1
%define pypi_name loguru
%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1
Summary: Python logging made (stupidly) simple
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/loguru
VCS: https://github.com/Delgan/loguru

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
# Some datetime tests use values that don't fit into a 32-bit C long.
# The package is noarch, so %ifarch doesn't work here, detect 32-bit builders via uname.
case "$(uname -m)" in
    i?86|arm*|mips*)
        export TOX_TESTENV_PASSENV="NO_INTERNET PYTEST_ADDOPTS"
        export PYTEST_ADDOPTS="--deselect 'tests/test_datetime.py::test_value_of_gmtoff_is_invalid' --deselect 'tests/test_datetime.py::test_formatting[YYYY-MM-DD HH:mm:ss.SSSSSS x-date35-timezone35-2242-03-16 12:56:32.999999 8589934592999999]'"
        ;;
esac
%tox_check_pyproject

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 14 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Updated to version 0.8.0.

* Sat Jul 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.3-alt6
- Fixed exception formatting test with Python 3.14.

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
