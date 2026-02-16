%define _unpackaged_files_terminate_build 1
%define pypi_name django-ckeditor-5
%define mod_name django_ckeditor_5

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.19
Release: alt1
Summary: CKEditor 5 for Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-ckeditor-5/
Vcs: https://github.com/hvlads/django-ckeditor-5.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
%add_pyproject_deps_check_filter codespell safety
%pyproject_builddeps_metadata_extra dev
%endif

%description
Django CKEditor 5 integration.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Same as in CI workflow
cp -R django_ckeditor_5 example/blog/
export PYTHONPATH=example/blog:$PYTHONPATH
%pyproject_run_pytest -p pytest_django \
--ds=blog.test_settings \
--override-ini="addopts=" \
--override-ini="pythonpath=example/blog" \
-vra example/blog

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jan 15 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.19-alt1
- New version (0.2.19).

* Thu Dec 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.18-alt1
- Initial build for ALT.
