%define _unpackaged_files_terminate_build 1
%define pypi_name plotly
%def_with check

Name:    python3-module-%pypi_name
Version: 7.1.0
Release: alt1

Summary: Interactive data visualization library for Python
License: MIT
Group:   Development/Python3
Url:     https://plotly.com/python/
Vcs:     https://github.com/plotly/plotly.py.git
BuildArch: noarch

Source:  %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

# Optional dependencies: anywidget and traitlets are required only
# for FigureWidget, matplotlib for matplotlylib, skimage for ternary
# contours.
%filter_from_requires /^python3(\(anywidget\|traitlets\|matplotlib\|skimage\)[.)]/d

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

# ruff is used upstream only for codegen formatting, not for tests.
%add_pyproject_deps_check_filter ruff
%if_with check
%pyproject_builddeps_metadata_extra dev-core
%endif

%description
Plotly is an interactive, open-source plotting library for Python.
It supports over 40 chart types covering statistical, financial,
geographic, scientific and 3-dimensional use cases. Figures are
rendered by plotly.js and can be displayed in Jupyter notebooks,
saved to standalone HTML files or embedded in web applications.

The package provides the high-level plotly.express interface and
the low-level plotly.graph_objects API.

%package -n jupyterlab-%pypi_name
Summary: Plotly extension for JupyterLab
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-jupyterlab

%description -n jupyterlab-%pypi_name
JupyterLab extension for displaying Plotly graphs.

%prep
%setup -q -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
# plotly.js bundle (plotly/package_data) and the JupyterLab extension
# are prebuilt upstream and committed to the source tree; rebuilding
# them requires npm dependencies which are not available in hasher.
%pyproject_install
# drop Chrome downloader for kaleido image export
rm %buildroot%_bindir/plotly_get_chrome
# labextension is shipped in jupyterlab-plotly from %_datadir
rm -r %buildroot%python3_sitelibdir/%pypi_name/labextension
# drop upstream tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/matplotlylib/tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/matplotlylib/mplexporter/tests

%check
%pyproject_run_pytest tests/test_core

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info/
%python3_sitelibdir_noarch/_plotly_utils/
%doc README.md LICENSE.txt

%files -n jupyterlab-%pypi_name
%dir %_datadir/jupyter/labextensions
%_datadir/jupyter/labextensions/jupyterlab-%pypi_name/

%changelog
* Tue Oct 20 2026 Mikhail Nogin <joycap@altlinux.org> 7.1.0-alt1
- Initial build for ALT Sisyphus (Closes: #58371).
