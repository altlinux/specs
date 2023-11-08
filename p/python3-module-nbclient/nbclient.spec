%define _unpackaged_files_terminate_build 1

%define oname nbclient

%def_with check

Name: python3-module-%oname
Version: 0.9.0
Release: alt1
Summary: A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/nbclient/
VCS: https://github.com/jupyter/nbclient.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
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
BuildRequires: python3(flaky)
BuildRequires: python3(pytest_asyncio)
BuildRequires: /proc
BuildRequires: python3(ipykernel)
BuildRequires: python3(testpath)
%endif

%description
NBClient, a client library for programmatic notebook execution,
is a tool for running Jupyter Notebooks in different execution contexts.
NBClient was spun out of nbconvert's former ExecutePreprocessor.

NBClient lets you execute notebooks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_many_parallel_notebooks randomly fail
%pyproject_run_pytest -v --color=no -k 'not test_many_parallel_notebooks'

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/jupyter-execute
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*.dist-info

%changelog
* Wed Nov 08 2023 Anton Vyatkin <toni@altlinux.org> 0.9.0-alt1
- New version 0.9.0.
- Drop tests subpackage.

* Fri Jul 21 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt3
- FTBFS: add missing BR.

* Mon Jul 10 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt2
- FTBFS: fix BuildRequires.

* Thu Jul 06 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Mon Dec 05 2022 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- 0.5.4 -> 0.7.2
- tests was disabled due to reqursive dependencies with nbconvert (bootstrap)

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.4-alt1
- Updated to upstream version 0.5.4.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt1
- Updated to upstream version 0.5.3.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
