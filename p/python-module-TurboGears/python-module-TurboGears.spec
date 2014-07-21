%define version 1.5.1
%define release alt1
%setup_python_module TurboGears

%def_without python3

Name: %packagename
Version: 1.5.1
Release: alt1

Summary: Back-to-front web development in Python

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://www.turbogears.org

# http://www.turbogears.org/1.5/downloads/1.5.1/TurboGears-1.5.1.tar.gz
Source: %modulename-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires turbokid turbocheetah paste.script
# has no pythonX.Y() provides
Requires: python-module-decoratortools
Requires: python-module-PasteDeploy
# TurboGears needs old CherryPy
Requires: python-module-cherrypy2

%description
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

%package tests
Summary: Tests for TurboGears
Group: Development/Python
Requires: %name = %EVR

%description tests
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

This package contains tests for TurboGears.

%package -n python3-module-%modulename
Summary: Back-to-front web development in Python
Group: Development/Python3
%py3_requires turbokid turbocheetah paste.script
# has no pythonX.Y() provides
Requires: python3-module-decoratortools
Requires: python3-module-PasteDeploy
# TurboGears needs old CherryPy
Requires: python3-module-cherrypy2

%description -n python3-module-%modulename
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

%package -n python3-module-%modulename-tests
Summary: Tests for TurboGears
Group: Development/Python3
Requires: python3-module-%modulename = %EVR

%description -n python3-module-%modulename-tests
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

This package contains tests for TurboGears.

%prep
%setup -n %modulename-%version
# fix for TurboJson
subst "s|, < 1.2||g" setup.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

./doc/build_api_docs.sh

%files
%doc README.txt
%_bindir/tg-admin
%python_sitelibdir/turbogears
%python_sitelibdir/TurboGears*.egg-info
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/turbogears/qstemplates/quickstart/test.cfg_tmpl

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/turbogears/qstemplates/quickstart/test.cfg_tmpl

%if_with python3
%files -n python3-module-%modulename
%doc README.txt
%_bindir/tg-admin.py3
%python3_sitelibdir/turbogears
%python3_sitelibdir/TurboGears*.egg-info
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/tests
%exclude %python3_sitelibdir/turbogears/qstemplates/quickstart/test.cfg_tmpl

%files -n python3-module-%modulename-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/*/tests
%python3_sitelibdir/turbogears/qstemplates/quickstart/test.cfg_tmpl
%endif

%changelog
* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Version 1.5.1

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Version 1.1.3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt3.1
- Rebuild with Python-2.7

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt3
- add CherryPy 2 requires

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt2
- fix requires (ALT bug #19979)

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- new version (1.0.9) import in git

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 1.0.8-alt1
- Initial build for ALT Linux

