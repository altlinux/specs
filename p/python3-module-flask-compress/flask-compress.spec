%define _unpackaged_files_terminate_build 1
%define pypi_name flask-compress
%define mod_name flask_compress
%define distinfo_name Flask_Compress

%def_with check

Name: python3-module-%pypi_name
Version: 1.17
Release: alt1
Summary: Compress responses in your Flask app with gzip, deflate or brotli
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Compress
VCS: https://github.com/colour-science/flask-compress
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Flask-Compress allows you to easily compress your Flask application's
responses with gzip, deflate or brotli. It originally started as a fork
of Flask-gzip.
The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%distinfo_name-%version.dist-info/

%changelog
* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 1.17-alt1
- 1.14 -> 1.17.

* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 1.14-alt1
- Initial build for Sisyphus
