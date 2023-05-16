%define _unpackaged_files_terminate_build 1
%define oname django-environ
%define pypi_name django-environ

%def_with check

Name: python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application.
License: MIT
Group: Development/Python3
Url: https://django-environ.readthedocs.io/en/latest/
BuildArch: noarch

# VCS:https://github.com/joke2k/django-environ
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
The idea of this package is to unify a lot of packages that make the same stuff:
Take a string from os.environ, parse and cast it to some of useful python typed
variables. To do that and to use the 12factor approach, some connection strings
are expressed as url, so this package can parse it and return a urllib.parse.ParseResult.
These strings from os.environ are loaded from a .env file and filled in os.environ with
setdefault method, to avoid to overwrite the real environ.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/environ/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}


%changelog
* Mon May 15 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 0.10.0-alt1
- New version v0.10.0

* Thu Dec 02 2021 Dmitry Lyalyaev <fruktime@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux
