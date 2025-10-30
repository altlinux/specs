%define _unpackaged_files_terminate_build 1
%define pypi_name mapclassify

%def_without check
#tests disable due to https://bugzilla.altlinux.org/48007

Name: python3-module-%pypi_name
Version: 2.10.0
Release: alt1
Summary: Classification schemes for choropleth mapping
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/mapclassify/
VCS: https://github.com/pysal/mapclassify
BuildArch: noarch
Source: %name-%version.tar

%py3_provides %pypi_name

%add_python3_req_skip matplotlib.testing.decorators

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-numpy
BuildRequires: python3-module-scipy
BuildRequires: python3-module-numpy-tests
BuildRequires: python3-module-pandas
BuildRequires: python3-module-scikit-learn
BuildRequires: python3-module-networkx
BuildRequires: python3-module-libpysal
%endif

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m 'not request'

%files
%doc *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 29 2025 Nikita Panov <nexxy@altlinux.org> 2.10.0-alt1
- Initial build for Sisyphus
