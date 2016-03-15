%define oname js.fullcalendar

%def_with python3

Name: python-module-%oname
Version: 2.2.6
Release: alt1.dev.git20150107.1
Summary: Fanstatic packaging of FullCalendar
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.fullcalendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/js.fullcalendar.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-js.jquery
BuildPreReq: python-module-js.momentjs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-js.jquery
BuildPreReq: python3-module-js.momentjs
%endif

%py_provides %oname
%py_requires js js.jquery js.momentjs

%description
This library packages FullCalendar for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of FullCalendar
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery js.momentjs

%description -n python3-module-%oname
This library packages FullCalendar for fanstatic.

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
* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.2.6-alt1.dev.git20150107.1
- NMU rebuild.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6-alt1.dev.git20150107
- Version 2.2.6-dev

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev.git20141112
- Initial build for Sisyphus

