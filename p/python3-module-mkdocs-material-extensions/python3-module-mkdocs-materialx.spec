%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-material-extensions

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Markdown extension resources for MkDocs Material
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-material-extensions

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(mkdocs)
BuildRequires: python3(markdown)
BuildRequires: python3(pymdownx)
BuildRequires: python3(material)
BuildRequires: python3(bs4)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
Markdown extension resources for MkDocs for Material

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# change fontawesome-solid-ambulance to fontawesome-solid-tree
# because there is no fontawesome-solid-ambulance icon in mkdocs-material
sed -i tests/extensions/test_emoji.py -e \
       '/fontawesome-solid/ s/ambulance/tree/'
%tox_check_pyproject

%files
%python3_sitelibdir/materialx
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- New version.

* Fri Aug 25 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus

