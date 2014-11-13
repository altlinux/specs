%define oname js.angular_ui_calendar

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.beta.1
Summary: Fanstatic packaging of angular-ui ui-calendar
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular_ui_calendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-js.angular
BuildPreReq: python-module-js.fullcalendar python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-js.angular
BuildPreReq: python3-module-js.fullcalendar python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js js.angular js.fullcalendar

%description
This library packages angular-ui-calendar for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of angular-ui ui-calendar
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.angular js.fullcalendar

%description -n python3-module-%oname
This library packages angular-ui-calendar for fanstatic.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.beta.1
- Initial build for Sisyphus

