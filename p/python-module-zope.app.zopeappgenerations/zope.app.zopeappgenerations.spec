%define oname zope.app.zopeappgenerations
Name: python-module-%oname
Version: 3.6.1
Release: alt2.1
Summary: Zope Application ZODB Update Generations
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.zopeappgenerations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.annotation zope.app.authentication zope.app.component
%py_requires zope.copypastemove zope.dublincore zope.generations

%description
This package provides the ZODB schema update generations for all
components included in the classic Zope 3 releases.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Add necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

