%define _unpackaged_files_terminate_build 1
%define pypi_name Flask-RQ
%define pypi_nname flask-rq
%define mod_name flask_rq

# Tests hang on aarch64
%ifarch aarch64
%def_without check
%else
%def_with check
%endif

Name: python3-module-%pypi_nname
Version: 0.3.3
Release: alt1

Summary: RQ (Redis Queue) integration for Flask and Quart applications
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-RQ/
Vcs: https://github.com/pallets-eco/flask-rq

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra quart
%pyproject_builddeps_check
BuildRequires: python3-module-flask+async
BuildRequires: redis
%endif

%description
Flask-RQ is a Flask/Quart extension that background job execution
using RQ. RQ allows queueing functions to be run in separate worker
processes, allowing long-running jobs to run in the background without
blocking the web app from returning a response quickly. Flask-RQ
allows configuring RQ using Flask's config, and handles executing jobs
in the application context, so other services like database
connections are available.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export PATH="$PATH:%_sbindir"
%pyproject_run_pytest -vra

%files
%doc CHANGES.md LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 02 2025 Anton Zhukharev <ancieg@altlinux.org> 0.3.3-alt1
- Packaged for ALT Sisyphus.
