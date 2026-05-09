%define oname streamlit
%define pypi_name streamlit

# Optional integrations and example dependencies
%add_python3_req_skip langchain.callbacks.base langchain.schema
%add_python3_req_skip yfinance vega_datasets

Name: python3-module-%oname
Version: 1.57.0
Release: alt1

Summary: A faster way to build and share data apps

License: Apache-2.0
Group: Development/Python3
Url: https://streamlit.io

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Streamlit lets you transform Python scripts into interactive web apps in
minutes, instead of weeks. Build dashboards, generate reports, or create
chat apps. Once you've created an app, you can use Streamlit Community
Cloud platform to deploy, manage, and share your app.

%package -n %oname
Summary: Streamlit CLI to run data apps
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n %oname
Streamlit lets you transform Python scripts into interactive web apps in
minutes, instead of weeks.

This package contains the streamlit command line interface used to run
Streamlit apps.

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

%files -n %oname
%_bindir/streamlit

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 1.57.0-alt1
- new version (1.57.0)

