%define _unpackaged_files_terminate_build 1
%define pypi_name django-csp

%def_with check

Name: python3-module-%pypi_name
Version: 3.8
Release: alt1

Summary: Content Security Policy for Django.
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/mozilla/django-csp

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
%pyproject_builddeps_metadata_extra tests
%endif

%description
Django-CSP adds Content-Security-Policy headers to Django.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc *.rst *.md LICENSE
%python3_sitelibdir/csp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 17 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 3.8-alt1
- 3.7 -> 3.8

* Fri Sep 01 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 3.7-alt2
- fix FTBFS
  + build from latest upstream commit (git 17d94154)

* Tue Aug 22 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 3.7-alt1
- Initial build for ALT Linux

