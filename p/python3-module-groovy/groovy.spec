%define _unpackaged_files_terminate_build 1
%define pypi_name groovy

%def_with check

Name: python3-module-%pypi_name
# Due to upstream doesn't make tags we need to pull version
# from groovy/version.txt 
Version: 0.1.2
Release: alt1
Summary: A small Python library created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/gradio-app/groovy
Vcs: https://pypi.org/project/groovy/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3(ruff)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
Groovy is a Python-to-JavaScript transpiler, meaning that it converts Python
functions to their JavaScript equivalents. It is used in the Gradio library, so
that developers can write functions in Python and have them run as fast as
client-side JavaScript. Instead of aiming for full coverage of Python features,
groovy prioritizes clear error reporting for unsupported Python code, making it
easier for developers to modify their functions accordingly.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#tox_create_default_config
#tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 06 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.

