%define _unpackaged_files_terminate_build 1

%def_with check

%define oname python-crontab

Name: python3-module-%oname
Version: 3.2.0
Release: alt1

Summary: Python Crontab API
License: LGPL-3.0
Group: Development/Python3
URL: https://pypi.org/project/python-crontab/
VCS: https://gitlab.com/doctormo/python-crontab

BuildArch: noarch

Source0: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-dateutil
%endif

%description
Crontab module for reading and writing crontab files and accessing
the system cron automatically and simply using a direct API.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.*
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%python3_sitelibdir/cronlog.py
%python3_sitelibdir/crontab.py
%python3_sitelibdir/crontabs.py

%changelog
* Wed Nov 27 2024 Yaroslav Bahtin <alpacost@altlinux.org> 3.2.0-alt1
- Initial build
