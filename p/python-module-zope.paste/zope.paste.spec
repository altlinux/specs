%define oname zope.paste
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Zope 3 and PasteDeploy
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.paste/0.3
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope paste.deploy zope.interface zope.app.appsetup
%py_requires zope.app.wsgi zope.app.twisted zope.app.server

%description
zope.paste allows you to

* employ WSGI middlewares inside a Zope 3 application
* deploy the Zope 3 application server on any WSGI-capable webserver

using PasteDeploy. These are two completely different modi operandi
which only have in common that they are facilitate PasteDeploy.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

