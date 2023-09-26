%define _unpackaged_files_terminate_build 1
%define pypi_name aio-pika
%define mod_name aio_pika

# tests require running broker service
%def_without check

Name: python3-module-%pypi_name
Version: 9.3.0
Release: alt1

Summary: AMQP 0.9 client designed for asyncio and humans
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aio-pika/
Vcs: https://github.com/mosquito/aio-pika

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter collective-checkdocs
%add_pyproject_deps_check_filter coveralls
%add_pyproject_deps_check_filter nox
%add_pyproject_deps_check_filter pytest-rst
%add_pyproject_deps_check_filter sphinx-autobuild
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A wrapper around aiormq for asyncio and humans.

Features:

* Completely asynchronous API.
* Object oriented API.
* Transparent auto-reconnects with complete state recovery with connect_robust
  (e.g. declared queues or exchanges, consuming state and bindings).
* Python 3.7+ compatible.
* For python 3.5 users available aio-pika<7
* Transparent publisher confirms support
* Transactions support
* Completely type-hints coverage.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst COPYING
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 9.3.0-alt1
- Updated to 9.3.0.

* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.2-alt1
- Updated to 9.2.2.

* Thu Aug 03 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.0-alt1
- Updated to 9.2.0.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 9.0.5-alt1
- Initial build for ALT Sisyphus.

