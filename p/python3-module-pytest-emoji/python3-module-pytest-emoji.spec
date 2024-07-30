%define pypi_name pytest-emoji
%define mod_name pytest_emoji

# only to see a possible output
%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: A pytest plugin that adds emojis to your test result report
License: MIT
Group:   Development/Python3
URL:     https://github.com/hackebrot/pytest-emoji

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
