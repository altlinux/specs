# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20120405.1.1
%define mname experimental
%define oname %mname.cssselect
Name: python-module-%oname
Version: 0.3
#Release: alt1.git20120405
Summary: Experimental version of lxml.cssselect
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/experimental.cssselect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lrowe/experimental.cssselect.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-lxml

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
This package contains an experimental fork of the lxml.cssselect module.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20120405.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20120405.1
- (AUTO) subst_x86_64.

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20120405
- Initial build for Sisyphus

