%define pypi_name pydriller

# Needs network
%def_without check

Name:    python3-module-%pypi_name
Version: 2.5.1
Release: alt1

Summary: Python Framework to analyse Git repositories
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/ishepard/pydriller

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-psutil
BuildRequires: python3-module-mock
BuildRequires: python3-module-lizard
BuildRequires: python3-module-GitPython
BuildRequires: python3-module-pytz
BuildRequires: unzip
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
PyDriller is a Python framework that helps developers in analyzing Git
repositories. With PyDriller you can easily extract information about commits,
developers, modified files, diffs, and source code.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
unzip test-repos.zip
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/PyDriller-2.5.1.dist-info/

%changelog
* Mon Nov 13 2023 Alexander Burmatov <thatman@altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus.
