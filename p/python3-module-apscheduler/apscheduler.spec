Name: python3-module-apscheduler
Version: 3.10.4
Release: alt1

Summary: In-process task scheduler with Cron-like capabilities
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/APScheduler/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)

%description
Advanced Python Scheduler (APScheduler) is a Python library that lets
you schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.

Among other things, APScheduler can be used as a cross-platform,
application specific replacement to platform specific schedulers, such
as the cron daemon or the Windows task scheduler. Please note, however,
that APScheduler is not a daemon or service itself, nor does it come
with any command line tools. It is primarily meant to be run inside
existing applications. That said, APScheduler does provide some building
blocks for you to build a scheduler service or to run a dedicated
scheduler process.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%python3_sitelibdir/apscheduler
%python3_sitelibdir/APScheduler-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.4-alt1
- 3.10.4 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.1-alt1
- 3.10.1 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.1-alt1
- 3.9.1 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.0-alt1
- 3.7.0 released

* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.1.0-alt2
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1.dev1.git20141020.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt1.dev1.git20141020.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt1.dev1.git20141020.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.dev1.git20141020
- Initial build for Sisyphus

