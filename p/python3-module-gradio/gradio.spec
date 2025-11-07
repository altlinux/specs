%define _unpackaged_files_terminate_build 1
%define pypi_name gradio
%define mod_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 5.42.0
Release: alt2
Summary: Build and share delightful machine learning apps, all in Python.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/gradio-app/gradio
Vcs: https://pypi.org/project/gradio/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(numpy)
BuildRequires: python3(fastapi)
BuildRequires: python3(numba)
BuildRequires: python3(orjson)
BuildRequires: python3(multipart)
BuildRequires: python3(scipy)
BuildRequires: python3(hatchling)
BuildRequires: python3-module-hatch-requirements-txt
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-groovy
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-huggingface-hub

Requires: python3-module-gradio-client
Requires: python3-module-gradio-pdf
Requires: python3-module-groovy
Requires: python3-module-multipart
Requires: python3-module-python-multipart
Requires: python3-module-safehttpx
Requires: python3-module-mcp

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%add_python3_req_skip python_multipart.multipart 

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%_bindir/upload_theme
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 07 2025 Pavel Shilov <zerospirit@altlinux.org> 5.42.0-alt2
- Update requires.

* Sun Aug 10 2025 Pavel Shilov <zerospirit@altlinux.org> 5.42.0-alt1
- Initial build for Sisyphus.

