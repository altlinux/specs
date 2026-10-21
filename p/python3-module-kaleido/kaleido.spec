%define _unpackaged_files_terminate_build 1
%define pypi_name kaleido
%define python_subdir src/py

Name:    python3-module-%{pypi_name}
Version: 1.5.0
Release: alt1

Summary: Fast static image export for web-based visualization libraries
License: MIT
Group:   Development/Python3
Url:     https://github.com/plotly/kaleido
Vcs:     https://github.com/plotly/kaleido.git

BuildArch: noarch

Source:  %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
Patch0:  %pypi_name-%version-alt-set-starting-version.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%description
Kaleido is a cross-platform Python library for generating static images
(e.g. png, svg, pdf, etc.) for Plotly.js, to be used by Plotly.py.

Rendering requires a Chromium-based browser at runtime, e.g. the
chromium package.

%package -n %pypi_name-tools
Summary: Batch renderer of Plotly figures for testing Kaleido
Group:   Development/Tools
Requires: %name = %EVR

%description -n %pypi_name-tools
kaleido_mocker is an integration-test utility of Kaleido. It loads
Plotly figures from JSON files and renders them to png, pdf, jpg,
webp, svg or json, reporting errors and timing.

%prep
%setup -n %{pypi_name}-%{version}
%autopatch -p1
cd %{python_subdir}
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
cd %{python_subdir}
%pyproject_build

%install
cd %{python_subdir}
%pyproject_install
# kaleido_get_chrome fetches a prebuilt Google Chrome for Testing archive over
# the network and unpacks it into the user's home directory. Not shipped:
# use the chromium package from the repository instead.
rm -f %buildroot%_bindir/kaleido_get_chrome

# No %%check: upstream tests need pytest, pytest-asyncio, hypothesis, plotly
# and, for most of them, a running Chromium browser.

%files -n %pypi_name-tools
%_bindir/kaleido_mocker

%files
%python3_sitelibdir_noarch/%{pypi_name}/
%python3_sitelibdir_noarch/%{pypi_name}-%{version}.dist-info/
%doc README.md LICENSE

%changelog
* Tue Oct 20 2026 Mikhail Nogin <joycap@altlinux.org> 1.5.0-alt1
- Initial build for ALT Sisyphus.
