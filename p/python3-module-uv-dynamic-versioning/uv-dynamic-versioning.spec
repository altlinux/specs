%define _unpackaged_files_terminate_build 1
%define pypi_name uv-dynamic-versioning
%define mod_name uv_dynamic_versioning

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.2
Release: alt1
Summary: Dynamic versioning based on VCS tags for uv/hatch project.
License: MIT
Group: Development/Python3
Url: https://github.com/ninoseki/uv-dynamic-versioning/
Vcs: https://pypi.org/project/uv-dynamic-versioning/

BuildArch: noarch 

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(uv)
BuildRequires: python3(hatchling)
BuildRequires: python3(dunamai)
BuildRequires: python3(jinja2)
BuildRequires: python3(pydantic)
BuildRequires: python3(tomlkit)

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
#pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Sat Aug 09 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus.
