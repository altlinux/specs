%define _unpackaged_files_terminate_build 1
%define pypi_name gradio-pdf
%define mod_name gradio_pdf

%def_with check

Name: python3-module-%pypi_name
# Due to upstream doesn't make tags we need to pull version
#based on pyprojest.toml version discovery.
Version: 0.0.22
Release: alt1
Summary: Easily display PDFs in Gradio
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/freddyaboulton/gradio-pdf
Vcs: https://pypi.org/project/gradio-pdf/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3(pip)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
Gradui-PDF: Easily display PDFs in Gradio

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Wed Aug 06 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.22-alt1
- Initial build for Sisyphus.