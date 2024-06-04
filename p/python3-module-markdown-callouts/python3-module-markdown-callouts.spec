%define pypi_name markdown-callouts
%define mod_name markdown_callouts

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Markdown extension: a classier syntax for admonitions
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/markdown-callouts
VCS:     https://github.com/oprypin/markdown-callouts

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-markdown
BuildRequires: python3-module-pytest-golden
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
* Wed Jun 05 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Automatically updated to 0.4.0.
- Built with check.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
