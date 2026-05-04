%define oname fal-client
%define pypi_name fal_client

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Python client for fal.ai

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/fal-ai/fal

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%description
fal_client is a Python client for fal.ai serverless inference API.

It provides synchronous and asynchronous interfaces to run, submit
and stream model predictions, upload files, and consume server-sent
events from fal.ai endpoints.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog

* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus
