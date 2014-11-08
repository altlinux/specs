%define oname apscheduler

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.1.0
Release: alt1.dev1.git20141020
Summary: In-process task scheduler with Cron-like capabilities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/APScheduler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/agronholm/apscheduler.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-pytz
BuildPreReq: python-module-tzlocal python-module-futures
BuildPreReq: python-module-PyQt4 python-module-gevent
BuildPreReq: python-module-pymongo python-module-redis-py
BuildPreReq: python-module-tornado python-module-twisted-core
BuildPreReq: python-module-mock python-modules-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-pytz
BuildPreReq: python3-module-tzlocal python-module-gevent
BuildPreReq: python3-module-PyQt4 python-module-pymongo
BuildPreReq: python3-module-redis-py python3-module-tornado
BuildPreReq: python3-module-twisted-core python3-module-asyncio
BuildPreReq: python3-module-mock python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires twisted.internet

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

%package -n python3-module-%oname
Summary: In-process task scheduler with Cron-like capabilities
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.internet asyncio

%description -n python3-module-%oname
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
Group: Development/Python

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.dev1.git20141020
- Initial build for Sisyphus

