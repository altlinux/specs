%def_without check
%define _unpackaged_files_terminate_build 1

%define oname nbclient

Name: python3-module-%oname
Version: 0.7.2
Release: alt1
Summary: A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor.
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/nbclient/
VCS: https://github.com/jupyter/nbclient.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-hatchling
BuildRequires: python3(jupyter_client)
BuildRequires: python3(nbformat)
BuildRequires: python3(traitlets)
%if_with check
BuildRequires: python3(async_generator)
BuildRequires: python3(nest_asyncio)
BuildRequires: python3(xmltodict)
BuildRequires: python3(nbconvert)
BuildRequires: python3(ipywidgets)
%endif

%description
NBClient, a client library for programmatic notebook execution,
is a tool for running Jupyter Notebooks in different execution contexts.
NBClient was spun out of nbconvert's former ExecutePreprocessor.

NBClient lets you execute notebooks.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv

%files
%doc LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/jupyter-execute
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Mon Dec 05 2022 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- 0.5.4 -> 0.7.2
- tests was disabled due to reqursive dependencies with nbconvert (bootstrap)

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.4-alt1
- Updated to upstream version 0.5.4.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt1
- Updated to upstream version 0.5.3.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
