%define _unpackaged_files_terminate_build 1
%define pypi_name flask-compress
%define mod_name flask_compress
%define distinfo_name Flask_Compress

%def_with check

Name:    python3-module-%pypi_name
Version: 1.14
Release: alt1

Summary: Compress responses in your Flask app with gzip, deflate or brotli.
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-Compress
VCS:     https://github.com/colour-science/flask-compress

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%py3_provides %mod_name

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

%description
Flask-Compress allows you to easily compress your Flask application's
responses with gzip, deflate or brotli. It originally started as a fork
of Flask-gzip.
The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.

%prep
%setup -n %pypi_name-%version
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{distinfo_name}*

%changelog
* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 1.14-alt1
- Initial build for Sisyphus
