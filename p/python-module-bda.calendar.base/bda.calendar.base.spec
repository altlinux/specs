# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname bda.calendar
%define oname %mname.base
Name: python-module-%oname
Version: 1.2.2
#Release: alt1
Summary: Base common calendaring features: Convinience or not coverd yet
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/bda.calendar.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-pytz python-module-zope.interface

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.interface

%description
bda.calendar.base contains functions adressing programmers all-day tasks
not (or only partly) covered by pythons datetime or zopes DateTime.

Major part of these function is timezone aware. Also ist easy to deal
with timezones. An TimezoneFactory can be provided in the specific
application to i.e. be aware of the users timezone (i.e. in case of
webapps).

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires bda

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/bda/calendar/__init__.py \
	%buildroot%python_sitelibdir/bda/calendar/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/bda/calendar/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/bda/calendar/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/bda/calendar
%python_sitelibdir/bda/calendar/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1
- (AUTO) subst_x86_64.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

