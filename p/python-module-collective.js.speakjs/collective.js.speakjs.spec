# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.dev0.git20130408.1.1
%define mname collective
%define oname %mname.js.speakjs
Name: python-module-%oname
Version: 1.0.1
#Release: alt2.dev0.git20130408
Summary: Text-to-Speech in JavaScript using eSpeak
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.speakjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.speakjs.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
Requires: python-module-%mname.js = %EVR

%description
This package provides JavaScript resources for speak.js for Plone, but
doesn't provide any other integration for it.

%package -n python-module-%mname.js
Summary: Core files of %mname.js
Group: Development/Python
%py_requires %mname

%description -n python-module-%mname.js
Core files of %mname.js.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd src/collective/js/speakjs
cp -fR configure.zcml profiles static \
	%buildroot%python_sitelibdir/collective/js/speakjs/
popd

install -p -m644 src/collective/js/__init__.py \
	%buildroot%python_sitelibdir/collective/js/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/js/__init__.py*

%files -n python-module-%mname.js
%dir %python_sitelibdir/%mname/js
%python_sitelibdir/%mname/js/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.dev0.git20130408.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.dev0.git20130408.1
- (AUTO) subst_x86_64.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.1-alt2.dev0.git20130408
- remove Zope2-test from build deps

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20130408
- Initial build for Sisyphus

