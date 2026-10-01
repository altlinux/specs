%define _unpackaged_files_terminate_build 1
%define pypi_name hf-gradio
%define mod_name hf_gradio

Name: python3-module-%pypi_name
# Upstream doesn't make tags, version is taken from pyproject.toml.
Version: 0.4.1
Release: alt1
Summary: Hugging Face CLI extension for interacting with Gradio Spaces and Apps
License: MIT
Group: Development/Python3
Url: https://github.com/gradio-app/hf-gradio
Vcs: https://pypi.org/project/hf-gradio/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(hatchling)

# hf_gradio.cli uses gradio_client 2.x API.
Requires: python3-module-gradio-client >= 2.0

%py3_provides %pypi_name

%description
An extension of the Hugging Face CLI for interacting with Gradio Spaces
and Apps. It is used by Gradio to generate CLI snippets in the API docs.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# Upstream has no tests.

%files
%doc README.md LICENSE
%_bindir/hf-gradio
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Tue Sep 29 2026 Pavel Shilov <zerospirit@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
