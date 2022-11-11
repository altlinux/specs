%define _unpackaged_files_terminate_build 1

%define pypi_name sphinx-inline-tabs
%define norm_version 2022.1.2b11

Name: python3-module-%pypi_name
Version: 2022.01.02.beta11
Release: alt2
Summary: Add inline tabbed content to your Sphinx documentation. 
License: MIT
Group: Development/Python3
Url: https://sphinx-inline-tabs.readthedocs.io

BuildArch: noarch

# https://github.com/pradyunsg/sphinx-inline-tabs
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

BuildRequires: python3-module-sphinx

%py3_provides %pypi_name

%description
Add inline tabbed content to your Sphinx documentation.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/sphinx_inline_tabs
%python3_sitelibdir/sphinx_inline_tabs-%norm_version.dist-info/

%changelog
* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 2022.01.02.beta11-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Thu Apr 14 2022 Egor Ignatov <egori@altlinux.org> 2022.01.02.beta11-alt1
- new version 2022.01.02.beta11

* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 2021.08.17.beta10-alt1
- Initial build for ALT
