%define _unpackaged_files_terminate_build 1
%define pypi_name rply

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.8
Release: alt1

Summary: A pure Python parser generator, that also works with RPython
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/rply
Vcs: https://github.com/alex/rply

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-appdirs
%endif

%description
Welcome to RPLY! A pure Python parser generator, that also works with
RPython. It is a more-or-less direct port of David Beazley's awesome PLY,
with a new public API, and RPython support.

%prep
%setup -n %pypi_name-%version
# Tests still use the legacy "py.test" alias (removed from the "py" package
# years ago); rewrite them to call modern pytest directly.
sed -i \
    -e 's/^import py$/import pytest/' \
    -e 's/py\.test\.raises/pytest.raises/g' \
    -e 's/py\.test\.mark\.skip/pytest.mark.skip/g' \
    tests/test_parsergenerator.py tests/test_parser.py tests/test_utils.py 

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v \
    --ignore=tests/test_ztranslation.py

%files
%doc README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Mon Jun 29 2026 Nikita Panov <nexxy@altlinux.org> 0.7.8-alt1
- Initial build for Sisyphus.
