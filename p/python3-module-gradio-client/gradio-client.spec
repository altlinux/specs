%define _unpackaged_files_terminate_build 1
%define pypi_name gradio-client
%define mod_name gradio_client

%def_with check

Name: python3-module-%pypi_name
Version: 1.11.0
Release: alt2
Summary: Use a Gradio app as an API -- in 3 lines of Python
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/gradio-app/gradio
Vcs: https://www.gradio.app/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3-module-hatch-requirements-txt
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-huggingface-hub
BuildRequires: python3-module-discord

Requires: python3-module-huggingface-hub
Requires: python3-module-discord

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
This directory contains the source code for gradio_client,
a lightweight Python library that makes it very easy to use
any Gradio app as an API.

%add_python3_req_skip discord.ext

%prep
%setup
%autopatch -p1

%build
cd client/python
%pyproject_build

%install
cd client/python
%pyproject_install

%check
#pyproject_run_pytest

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Fri Nov 07 2025 Pavel Shilov <zerospirit@altlinux.org> 1.11.0-alt2
- skip dependency

* Wed Aug 06 2025 Pavel Shilov <zerospirit@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus.
