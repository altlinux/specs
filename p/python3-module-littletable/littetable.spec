%define _unpackaged_files_terminate_build 1
%define pypi_name littletable

%def_with check
Name: python3-module-%pypi_name
Version: 3.0.2
Release: alt1
Summary: An in-memory database of Python objects, searchable using quasi-SQL API.
License: MIT
Group: Development/Python3
Url: https://github.com/ptmcg/littletable
Vcs: https://pypi.org/project/littletable/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(rich)
BuildRequires: python3(openpyxl)
BuildRequires: python3(pandas)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(attrs)
BuildRequires: python3(traits)
BuildRequires: python3(traitlets)
BuildRequires: python3(pydantic)
BuildRequires: python3(pyparsing)
BuildRequires: python3(tox)
BuildRequires: python3(bandit)
BuildRequires: python3(defusedxml)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md HowToUseLittletable.txt 
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 20 2025 Pavel Shilov <zerospirit@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus. 

