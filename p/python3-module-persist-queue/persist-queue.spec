%define _unpackaged_files_terminate_build 1
%define pypi_name persist-queue
%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: A thread-safe disk based persistent queue in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/persist-queue
Vcs: https://github.com/peter-wangxu/persist-queue
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# deprecated, not need for build
%add_pyproject_deps_check_filter cov-core
%pyproject_builddeps_metadata_extra extra
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
%endif

%description
Persist-queue implements a file-based queue and a serial of sqlite3-based queues.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# require running mysql on 127.0.0.1
rm -v persistqueue/tests/test_mysqlqueue.py
%pyproject_run -- python3 -m nose2 -v

%files
%python3_sitelibdir/persistqueue
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 03 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.0.0-alt1
- New version.

* Sat Feb 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.8.1-alt1
- First build for ALT.
