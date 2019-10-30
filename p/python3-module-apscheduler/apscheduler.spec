%define oname apscheduler

%def_disable check

Name: python3-module-%oname
Version: 3.1.0
Release: alt2

Summary: In-process task scheduler with Cron-like capabilities
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/APScheduler/
# https://bitbucket.org/agronholm/apscheduler.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx

%py3_provides %oname
%py3_requires twisted.internet asyncio

BuildRequires: python3-module-html5lib python3-module-pbr
BuildRequires: python3-module-pycares python3-module-pygobject3
BuildRequires: python3-module-pytz python3-module-serial
BuildRequires: python3-module-unittest2 python3-module-zope


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

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Advanced Python Scheduler (APScheduler) is a Python library that lets
you schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Advanced Python Scheduler (APScheduler) is a Python library that lets
you schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.

This package contains documentation for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
pushd docs
sphinx-build-3 -b pickle -d build/doctrees . build/pickle
sphinx-build-3 -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc examples docs/build/html


%changelog
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

