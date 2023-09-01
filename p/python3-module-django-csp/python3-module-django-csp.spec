%define _unpackaged_files_terminate_build 1
%define pypi_name django-csp

%def_with check

Name: python3-module-%pypi_name
Version: 3.7
Release: alt2

Summary: Content Security Policy for Django.
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/mozilla/django-csp

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-django
BuildRequires: python3(django)
BuildRequires: python3(jinja2)
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif


%description
Django-CSP adds Content-Security-Policy headers to Django.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream setup.cfg (remove --pep8 and --flakes arguments)
cat > setup.cfg <<'EOF'
[tool:pytest]
addopts = -vs --tb=short
DJANGO_SETTINGS_MODULE = csp.tests.settings
EOF
%pyproject_run_pytest

%files
%doc *.rst *.md LICENSE
%python3_sitelibdir/csp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 01 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 3.7-alt2
- fix FTBFS
  + build from latest upstream commit (git 17d94154)

* Tue Aug 22 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 3.7-alt1
- Initial build for ALT Linux

