%define _unpackaged_files_terminate_build 1
%define pypi_name gradio-test
%define mod_name gradio_test
%def_with check

Name: python3-module-%pypi_name
Version: 0.5.30
Release: alt1
Summary: Build and share delightful machine learning apps, all in Python.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/gradio-app/gradio
Vcs: https://pypi.org/project/gradio/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(hatchling)
BuildRequires: python3-module-hatch-requirements-txt
BuildRequires: python3-module-hatch-fancy-pypi-readme

%if_with check
BuildRequires: python3(pytest)
%endif

%description
%summary

%prep
%setup
%autopatch -p1
sed -i -r '/^\[project\]/,/^\[/{ s/^([[:space:]]*version[[:space:]]*=[[:space:]]*).*/\1"%version"/ }' pyproject.toml

%build
cd js/preview/test/test
%pyproject_build

%install
cd js/preview/test/test
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-*.dist-info/

%changelog
* Sun Aug 10 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.30-alt1
- Initial build for Sisyphus

