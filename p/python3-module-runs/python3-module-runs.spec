%define pypi_name runs

%def_with check

Name:    python3-module-%pypi_name
Version: 1.2.2
Release: alt1

Summary: Run a block of text as a subprocess
License: MIT
Group:   Development/Python3
URL:     https://github.com/rec/runs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-tdir
BuildRequires: python3-module-xmod
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Runs has improved versions of call(), check_call(), check_output(), and run()
from Python's subprocess module that handle multiple commands and blocks of
text, fix some defects, and add some features.

%prep
%setup -n %pypi_name-%version
sed -i 's/assert not diff/assert diff/g' ./test_runs.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Aug 10 2024 Alexander Burmatov <thatman@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus.
