%define _unpackaged_files_terminate_build 1
%define pypi_name django-ckeditor-5
%define mod_name django_ckeditor_5

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.20
Release: alt1.1
Summary: CKEditor 5 for Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-ckeditor-5/
Vcs: https://github.com/hvlads/django-ckeditor-5.git
BuildArch: noarch
Source: %name-%version.tar
Source2: %name-%version-node_modules.tar

Requires: %name-frontend = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools
BuildRequires: node

%if_with check
BuildRequires: python3-module-bandit
BuildRequires: python3-module-black
BuildRequires: python3-module-coverage
BuildRequires: python3-module-django
BuildRequires: python3-module-mypy
BuildRequires: python3-module-mypy-extensions
BuildRequires: python3-module-pillow
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-tox
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-django-dbbackend-sqlite3
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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.20-alt1.1
- Demodernized packaging.

* Fri Feb 27 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.2.20-alt1
- New version (0.2.20).

* Thu Feb 19 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.19-alt2
- Vendored node_modules to package missing dist directory.
- Split frontend into python3-module-django-ckeditor-5-frontend subpackage.

* Thu Jan 15 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.19-alt1
- New version (0.2.19).

* Thu Dec 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.18-alt1
- Initial build for ALT.
