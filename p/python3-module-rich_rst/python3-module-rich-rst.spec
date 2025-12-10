%define _unpackaged_files_terminate_build 1
%define pypi_name rich_rst
# discrepancy between the expected and actual results when running in hasher
%def_without check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1
Summary: A reStructuredText renderer for rich
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich-rst
VCS: https://github.com/wasi-master/rich-rst

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
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
sed -i -e '/^dynamic/d' pyproject.toml \
       -e 's/^name = "rich-rst"/name = "rich_rst"\nversion = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README.md LICENSE

%changelog
* Mon Dec 08 2025 Vladislav Eliseev <general@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus.
