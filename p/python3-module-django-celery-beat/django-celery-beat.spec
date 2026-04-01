%define _unpackaged_files_terminate_build 1

%define oname django-celery-beat

%def_with check

Name: python3-module-%oname
Version: 2.8.1
Release: alt3

Summary: Database-backed Periodic Tasks
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-celery-beat
VCS: https://github.com/celery/django-celery-beat

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-django-timezone-field
BuildRequires: python3-module-celery
BuildRequires: python3-module-tzdata
BuildRequires: python3-module-ephem
BuildRequires: python3-module-python-crontab
BuildRequires: python3-module-cron-descriptor
%endif

Source0: %name-%version.tar

Patch: %name-%version-%release.patch

%description
This extension enables you to store the periodic task schedule in the
database. The periodic tasks can be managed from the Django Admin
interface, where you can create, edit and delete periodic tasks
and how often they should run.

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
%doc README.*
%python3_sitelibdir/django_celery_beat/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Sat Mar 28 2026 Yaroslav Bahtin <alpacost@altlinux.org> 2.8.1-alt3
- Fixed FTBFS (cron-descriptor >= 2.0)

* Thu Feb 19 2026 Stanislav Levin <slev@altlinux.org> 2.8.1-alt2
- NMU: fixed FTBFS (pytest 9).

* Wed Oct 22 2025 Yaroslav Bahtin <alpacost@altlinux.org> 2.8.1-alt1
- 2.7.0 -> 2.8.1

* Tue Oct 15 2024 Yaroslav Bahtin <alpacost@altlinux.org> 2.7.0-alt1
- Initial build
