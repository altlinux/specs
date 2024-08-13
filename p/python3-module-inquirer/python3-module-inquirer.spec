%define pypi_name inquirer

%def_with check

Name:    python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: A collection of common interactive command line user interfaces, based on Inquirer.js
License: MIT
Group:   Development/Python3
URL:     https://github.com/magmax/python-inquirer

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-blessed
BuildRequires: python3-module-readchar
BuildRequires: python3-module-editor
BuildRequires: python3-module-pexpect
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

# Fix interpreter invocations in tests
sed -i 's:python:python3:g' tests/acceptance/*.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --deselect=tests/acceptance/test_checkbox.py \
    --deselect=tests/acceptance/test_list.py \
    --deselect=tests/acceptance/test_password.py \
    --deselect=tests/acceptance/test_pre_answers.py \
    --deselect=tests/acceptance/test_shortcuts.py \
    --deselect=tests/acceptance/test_text.py

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
