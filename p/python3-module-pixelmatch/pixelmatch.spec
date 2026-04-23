#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename pixelmatch
%def_with check

Name: python3-module-%modulename
Version: 0.4.0
Release: alt1
Summary: A fast pixel-level image comparison python library
Group: Development/Python3
License: ISC

URL: https://pypi.org/project/pixelmatch/
VCS: https://github.com/whtsky/pixelmatch-py/

Source: %name-%version.tar
Source1: fixtures.tar

BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-poetry-core

%if_with check
Buildrequires: python3-module-pillow
Buildrequires: python3-module-pytest-benchmark
%endif

%description
A fast pixel-level image comparison library, originally created to compare
screenshots in tests. Now with additional support of PIL.

%prep
%setup -a1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Thu Apr 23 2026 Polina Poidenko <polipoki@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Tue Dec 23 2025 Polina Poidenko <polipoki@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
