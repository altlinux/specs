%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx_design

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt2
Summary: A sphinx extension for designing beautiful, view size responsive web components
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/sphinx_design
Source0: %pypi_name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/sphinx_design/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.2.0-alt1
- Autobuild version bump to 0.2.0

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.0.1-alt1
- Initial version for ALT
