%define oname js.fullcalendar

%def_with python3

Name: python-module-%oname
Version: 2.9.1
Release: alt1
Summary: Fanstatic packaging of FullCalendar
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.fullcalendar/

# https://github.com/Kotti/js.fullcalendar.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-fanstatic python-module-js.jquery
BuildRequires: python-module-js.momentjs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-fanstatic python3-module-js.jquery
BuildRequires: python3-module-js.momentjs
%endif

%py_provides %oname
%py_requires js js.jquery js.momentjs

%description
This library packages FullCalendar for fanstatic.

%if_with python3
%package -n python3-module-%oname
Summary: Fanstatic packaging of FullCalendar
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery js.momentjs

%description -n python3-module-%oname
This library packages FullCalendar for fanstatic.
%endif

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

%if "%_lib" == "lib64"
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
py.test3
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%endif

%changelog
* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt1
- Updated to upstream version 2.9.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.6-alt1.dev.git20150107.1.1
- (AUTO) subst_x86_64.

* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.2.6-alt1.dev.git20150107.1
- NMU rebuild.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6-alt1.dev.git20150107
- Version 2.2.6-dev

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev.git20141112
- Initial build for Sisyphus

