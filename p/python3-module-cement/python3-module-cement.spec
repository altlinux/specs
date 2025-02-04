%define _unpackaged_files_terminate_build 1
%define pypi_name cement

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.12
Release: alt1

Summary: Application Framework for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://builtoncement.com/
Vcs: https://github.com/datafolklabs/cement

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

# remove todo-tutorial to avoid tinydb dependency
%add_findreq_skiplist %python3_sitelibdir/%pypi_name/cli/templates/generate/todo-tutorial/*

%if_with check
%set_pyproject_deps_check_filter coverage mypy ruff
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra colorlog
%pyproject_builddeps_metadata_extra watchdog
%pyproject_builddeps_metadata_extra yaml
%pyproject_builddeps_metadata_extra jinja2
%pyproject_builddeps_metadata_extra redis
%pyproject_builddeps_metadata_extra memcached
%pyproject_builddeps_metadata_extra mustache
%pyproject_builddeps_metadata_extra tabulate
%pyproject_builddeps_check
%endif

%description
Cement is an advanced and flexible Python framework designed
for building command-line applications. It provides essential
features such as argument parsing, configuration management,
logging, plugin architecture, and much more to streamline the
development of CLI tools.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pdm dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# - "tests/ext/test_ext_smtp.py" requires a running SMTP server (Mailpit).
# - "tests/ext/test_ext_memcached.py" requires a running Memcached server.
# - "tests/ext/test_ext_redis.py" requires a running Redis server.
%pyproject_run_pytest -vra \
	--deselect "tests/ext/test_ext_redis.py" \
	--deselect "tests/ext/test_ext_smtp.py" \
	--deselect "tests/ext/test_ext_memcached.py" \
	tests

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/CHANGELOG.md
%exclude %python3_sitelibdir/CONTRIBUTORS.md
%doc README.* LICENSE

%changelog
* Mon Jan 27 2025 Denis Sergeev <zeff@altlinux.org> 3.0.12-alt1
- Initial build for Sisyphus.
