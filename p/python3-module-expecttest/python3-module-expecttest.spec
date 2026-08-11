%define _unpackaged_files_terminate_build 1

%define pypi_name expecttest

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Python library for inline expected-output testing
License: MIT
Group:   Development/Python3
URL:     https://github.com/pytorch/expecttest

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This library implements expect tests (also known as "golden" tests).
Expect tests are a method of writing tests where instead of hard-coding
the expected output of a test, you run the test to get the output,
and the test framework automatically populates the expected output.
If the output of the test changes, you can rerun the test with
the environment variable EXPECTTEST_ACCEPT=1 to automatically update
the expected output.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 27 2026 Nikita Shmatko <nash@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
