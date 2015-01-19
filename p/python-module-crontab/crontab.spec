%define oname crontab

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.9.2
Release: alt1.bzr20150119
Summary: Python Crontab API
License: GPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/python-crontab/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:python-crontab
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dateutil python-module-croniter
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dateutil python3-module-croniter
%endif

%py_provides %oname
%py_requires croniter

%description
Crontab module for read and writing crontab files and accessing the
system cron automatically and simply using a direct API.

%package -n python3-module-%oname
Summary: Python Crontab API
Group: Development/Python3
%py3_provides %oname
%py3_requires croniter

%description -n python3-module-%oname
Crontab module for read and writing crontab files and accessing the
system cron automatically and simply using a direct API.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS ChangeLog README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog README
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1.bzr20150119
- Version 1.9.2

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.bzr20150102
- Initial build for Sisyphus

