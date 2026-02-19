%define _unpackaged_files_terminate_build 1
%define pypi_name django-ckeditor-5
%define mod_name django_ckeditor_5

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.19
Release: alt2
Summary: CKEditor 5 for Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-ckeditor-5/
Vcs: https://github.com/hvlads/django-ckeditor-5.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: %name-%version-node_modules.tar

Requires: %name-frontend = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: node
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
%add_pyproject_deps_check_filter codespell safety
%pyproject_builddeps_metadata_extra dev
%endif

%description
Django CKEditor 5 integration.

%package frontend
Summary: CKEditor 5 frontend assets for django-ckeditor-5
License: GPL-2.0-or-later
Group: Development/Python3
Requires: %name = %EVR

%description frontend
Pre-built CKEditor 5 JavaScript and styles for the django-ckeditor-5 Django app.

%prep
%setup -a2
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
cd django_ckeditor_5
./node_modules/.bin/webpack --mode production
cd ..
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
%exclude %python3_sitelibdir/%mod_name/static/django_ckeditor_5/dist

%files frontend
%python3_sitelibdir/%mod_name/static/django_ckeditor_5/dist/

%changelog
* Thu Feb 19 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.19-alt2
- Vendored node_modules to package missing dist directory.
- Split frontend into python3-module-django-ckeditor-5-frontend subpackage.

* Thu Jan 15 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.19-alt1
- New version (0.2.19).

* Thu Dec 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.18-alt1
- Initial build for ALT.
