%define oname repoze.who

%def_with python3

Name:           python-module-%oname
Version:        2.0
Release:        alt3
Summary:        Identification and authentication framework for WSGI
Group:          Development/Python
License:        BSD-derived
URL:            http://pypi.python.org/pypi/repoze.who/
Source:         %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel python-module-sphinx-devel
BuildPreReq: texlive-latex-recommended gif2png
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-paste python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-zope.interface
BuildPreReq: python3-module-paste python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze paste zope.interface

%description
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

%if_with python3
%package -n python3-module-%oname
Summary: Identification and authentication framework for WSGI (Python 3)
Group: Development/Python3
%py3_requires repoze paste zope.interface

%description -n python3-module-%oname
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

%package -n python3-module-repoze
Summary: Root files for repoze (Python 3)
Group: Development/Python3
%py3_provides repoze

%description -n python3-module-repoze
Root files for repoze.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

This package contains tests for repoze.who.
%endif

%package -n python-module-repoze
Summary: Root files for repoze
Group: Development/Python
%py_provides repoze

%description -n python-module-repoze
Root files for repoze.

%package tests
Summary: Tests for repoze.who
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

This package contains tests for repoze.who.

%package docs
Summary: Documentation for repoze.who
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

This package contains documentation for repoze.who.

%package pickles
Summary: Pickles for repoze.who
Group: Development/Python

%description pickles
repoze.who is an identification and authentication framework for
arbitrary WSGI applications. It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service
(PAS) (but repoze.who is not dependent on Zope in any way; it is useful
for any WSGI application). It provides no facility for authorization
(ensuring whether a user can or cannot perform the operation implied by
the request). This is considered to be the domain of the WSGI
application.

This package contains pickles for repoze.who.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

export PYTHONPATH=$PWD
pushd docs/.static
gif2png logo_hi.gif
popd
%make -C docs latex

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -p -m644 repoze/__init__.py %buildroot%python_sitelibdir/repoze
for i in $(find %buildroot%python_sitelibdir/repoze -type d)
do
	touch $i/__init__.py
done

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install

%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

install -p -m644 repoze/__init__.py %buildroot%python3_sitelibdir/repoze
for i in $(find %buildroot%python3_sitelibdir/repoze -type d)
do
	touch $i/__init__.py
done

popd
%endif

%files
%doc *.txt PKG-INFO
%python_sitelibdir/%oname-*
%exclude %python_sitelibdir/*.pth
%python_sitelibdir/repoze/*
%exclude %python_sitelibdir/repoze/__init__.py*
%exclude %python_sitelibdir/repoze/who/tests
%exclude %python_sitelibdir/repoze/who/plugins/tests

%files -n python-module-repoze
%dir %python_sitelibdir/repoze
%python_sitelibdir/repoze/__init__.py*

%files tests
%python_sitelibdir/repoze/who/tests
%python_sitelibdir/repoze/who/plugins/tests

%files docs
%doc docs/.build/latex/*.pdf
%doc docs/.build/html

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt PKG-INFO
%python3_sitelibdir/%oname-*
%exclude %python3_sitelibdir/*.pth
%python3_sitelibdir/repoze/*
%exclude %python3_sitelibdir/repoze/__init__.py*
%exclude %python3_sitelibdir/repoze/who/tests
%exclude %python3_sitelibdir/repoze/who/plugins/tests

%files -n python3-module-repoze
%dir %python3_sitelibdir/repoze
%python3_sitelibdir/repoze/__init__.py*

%files -n python3-module-%oname-tests
%python3_sitelibdir/repoze/who/tests
%python3_sitelibdir/repoze/who/plugins/tests
%endif

%changelog
* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Version 2.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.b1.3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.3
- Excluded *.pth

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.2
- Added necessary runtime requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.1
- Set as archdep package

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1
- Version 2.0b1

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a4
- Version 2.0a4

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a3.1
- Rebuilt with python-module-sphinx-devel

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a3
- Version 2.0a3

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.18-alt1
- Initial build for Sisyphus

