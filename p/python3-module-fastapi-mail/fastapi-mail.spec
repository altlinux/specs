%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-mail
%define module_name fastapi_mail

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.4
Release: alt1

Summary: A simple lightweight mail system, for sending emails and attachments
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-mail
Vcs: https://github.com/sabuhish/fastapi-mail

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter mkdocs-markdownextradata-plugin
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
FastAPI-Mail is a lightweight and flexible email-sending library for FastAPI.
It supports individual and bulk email delivery, attachments, asynchronous
sending, background tasks, and Jinja2 HTML templates. The library also
provides utilities for validating email addresses, including support for
custom domain blocking and te

%prep
%setup
%autopatch1 -p1
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
# ignore network-dependent tests
# test_default_checker - attempts to fetch temporary email domains list
# from external resource
# test_redis_checker - attempts DNS query to verify domain MX records
%pyproject_run_pytest -k "not test_default_checker and not test_redis_checker"

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 13 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.6.4-alt1
- Updated to new version 1.6.4.

* Thu Feb 19 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.6.2-alt1
- Updated to new version v1.6.2.

* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.6.1-alt1
- Initial build for ALT Sisyphus.
