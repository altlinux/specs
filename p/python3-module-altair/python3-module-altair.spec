%define pypi_name altair

Name: python3-module-altair
Version: 6.1.0
Release: alt1

Summary: Vega-Altair: A declarative statistical visualization library for Python

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/vega/altair

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

# Optional backends and integrations imported lazily; do not force at runtime.
%add_python3_req_skip altair_tiles anywidget
%add_python3_req_skip pandas numpy pyarrow polars geopandas
%add_python3_req_skip vegafusion vl_convert
%add_python3_req_skip IPython.core IPython.display ipykernel
%add_python3_req_skip traitlets

%description
Vega-Altair is a declarative statistical visualization library for Python,
based on Vega and Vega-Lite. It offers a powerful and concise grammar that
lets you build a wide range of statistical visualizations quickly.

With Vega-Altair, you can spend more time understanding your data and its
meaning. The API contains a large set of well-tested, intuitive plot types
and configuration options, allowing you to focus on data exploration
rather than chart construction details.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 6.1.0-alt1
- initial build for ALT Sisyphus

