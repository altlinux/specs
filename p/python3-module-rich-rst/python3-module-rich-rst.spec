%define _unpackaged_files_terminate_build 1
%define pypi_name rich-rst
%define module_name rich_rst
%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: A reStructuredText renderer for rich
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich-rst
VCS: https://github.com/wasi-master/rich-rst

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

Provides: python3-module-rich_rst = %version-%release
Obsoletes: python3-module-rich_rst < 2.1.0

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-docutils
BuildRequires: python3-module-rich
BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-Pygments
%endif

%description
%summary.

%prep
%setup

# Removing built-in dependencies
rm -rf rich_rst/_vendor/

# Replacing imports with system dependencies
find rich_rst/ -name "*.py" -exec sed -i -E 's/rich_rst\._vendor\.docutils/docutils/g' {} +
find rich_rst/ -name "*.py" -exec sed -i -E 's/from rich_rst\._vendor import/import/g' {} +

find tests/ -name "*.py" -exec sed -i -E 's/rich_rst\._vendor\.docutils/docutils/g' {} +
find tests/ -name "*.py" -exec sed -i -E 's/from rich_rst\._vendor import/import/g' {} +

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%doc README.md LICENSE

%changelog
* Tue Jul 07 2026 Vladislav Eliseev <general@altlinux.org> 2.1.0-alt1
- New version 2.1.0.
- Unvendored docutils to fix broken dependencies.
- Enabled tests.
- Renamed package.

* Mon Dec 08 2025 Vladislav Eliseev <general@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus.
