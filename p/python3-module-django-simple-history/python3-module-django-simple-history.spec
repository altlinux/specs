%define _unpackaged_files_terminate_build 1

%define pypi_name django-simple-history
%define mod_name simple_history
%define distinfo_name django_simple_history

%def_with check

Name: python3-module-%pypi_name
Version: 3.7.0
Release: alt1

Summary: Store model history and view/revert changes from admin site.
License: BSD-3-Clause
Group: Development/Python3
Url: https://django-simple-history.readthedocs.io/
Vcs: https://github.com/jazzband/django-simple-history
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%python3_sitelibdir/%mod_name-%version/docs
sed -i 's/__version__ = metadata.version("%pypi_name")/__version__ = "%version"/' %mod_name/__init__.py

%check
python3 runtests.py

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %distinfo_name}/

%changelog
* Mon Sep 16 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 3.7.0-alt1
- Initial build for ALT Linux

