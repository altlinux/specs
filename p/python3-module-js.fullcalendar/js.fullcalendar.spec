%define oname js.fullcalendar

Name: python3-module-%oname
Version: 2.9.1
Release: alt2

Summary: Fanstatic packaging of FullCalendar
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.fullcalendar/

# https://github.com/Kotti/js.fullcalendar.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic
BuildRequires: python3-module-js.jquery
BuildRequires: python3-module-js.momentjs
BuildRequires: python3-module-pytest

%py3_requires js js.jquery js.momentjs

%description
This library packages FullCalendar for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
py.test3

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.9.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

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

