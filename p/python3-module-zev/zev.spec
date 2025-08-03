%define _unpackaged_files_terminate_build 1
%define pypi_name zev
%define mod_name %pypi_name

#def_with check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
Summary: A simple CLI tool to help you remember terminal commands.
License: MIT
Group: Terminals
Url: https://github.com/dtnewman/zev
Vcs: https://pypi.org/project/zev/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-openai
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pyperclip
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-questionary
BuildRequires: python3-module-rich
BuildRequires: python3-module-h11 >= 0.13
BuildRequires: python3-module-httpcore
BuildRequires: python3-module-httpx

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#project didn't have tests
#pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Aug 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
