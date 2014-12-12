%define mname sauna
%define oname %mname.reload
Name: python-module-%oname
Version: 0.5.4
Release: alt1.dev0.git20141019
Summary: Instant code reloading for Plone using a fork loop
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/sauna.reload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/sauna.reload.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-watchdog python-module-argh
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires z3c.autoinclude watchdog plone.app.theming plone.resource
%py_requires zope.interface zope.event zope.component zope.dottedname
%py_requires zope.publisher

%description
sauna.reload is a developer tool which restarts Plone and reloads your
changed source code every time you save a file. The restart is optimized
for speed and happens much faster than a normal start up process.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev0.git20141019
- Initial build for Sisyphus

