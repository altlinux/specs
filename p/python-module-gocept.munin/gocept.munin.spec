# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname gocept
%define oname %mname.munin
Name: python-module-%oname
Version: 0.1
#Release: alt1
Summary: Utilities for writing munin plugins
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.munin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
This package provides base classes for defining Munin graphs and a
main function to handle munin-typical symlinked scripts.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

