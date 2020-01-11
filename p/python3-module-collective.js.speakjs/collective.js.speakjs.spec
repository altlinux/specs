%define _unpackaged_files_terminate_build 1
%define mname collective
%define oname %mname.js.speakjs

%def_with check

Name: python3-module-%oname
Version: 1.0.1
Release: alt3.dev0.git20130408
Summary: Text-to-Speech in JavaScript using eSpeak
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.js.speakjs/
#Git:  https://github.com/collective/collective.js.speakjs.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
Requires: python3-module-%mname.js = %EVR

%description
This package provides JavaScript resources for speak.js for Plone, but
doesn't provide any other integration for it.

%package -n python3-module-%mname.js
Summary: Core files of %mname.js
Group: Development/Python3
%py3_requires %mname

%description -n python3-module-%mname.js
Core files of %mname.js.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd src/collective/js/speakjs
cp -fR configure.zcml profiles static \
	%buildroot%python3_sitelibdir/collective/js/speakjs/
popd

install -p -m644 src/collective/js/__init__.py \
	%buildroot%python3_sitelibdir/collective/js/

%check
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/js/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/js/__init__.py*

%files -n python3-module-%mname.js
%dir %python3_sitelibdir/%mname/js
%python3_sitelibdir/%mname/js/__init__.py*
%exclude %python3_sitelibdir/*.pth

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.1-alt3.dev0.git20130408
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.dev0.git20130408.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.dev0.git20130408.1
- (AUTO) subst_x86_64.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.1-alt2.dev0.git20130408
- remove Zope2-test from build deps

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20130408
- Initial build for Sisyphus

