%define _unpackaged_files_terminate_build 1
%define pypi_name dj-database-url
%def_with check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1.1

Summary: Use Database URLs in your Django Application
License: MIT
Group: Development/Python3
Url: https://github.com/jazzband/dj-database-url
Vcs: https://github.com/jazzband/dj-database-url.git
BuildArch: noarch

Source0: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-django
BuildRequires: /proc
%endif

%description
This simple Django utility allows you to utilize the 12factor inspired
DATABASE_URL environment variable to configure your Django application.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%python3_sitelibdir/dj_database_url
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1.1
- Demodernized packaging.

* Thu Jan 12 2026 Grant Makyan <karonus@altlinux.org> 3.1.0-alt1
- First build for ALT.
