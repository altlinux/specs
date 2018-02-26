%define oname ore.alchemist
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: sqlalchemy zope3 integration
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/ore.alchemist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ore transaction SQLAlchemy

%description
ore.alchemist provides core features for zope3 relational database
applications utilizing sqlalchemy. it includes transformation of zope3
schemas to sqlalchemy tables, sqlalchemy transformation into zope3
schemas, and containers.

it maintains a minimal api for sqlalchemy abstraction, you can use
whatever constructions sqlalchemy supports.

additionally ore.alchemist is the foundation package for a range of
additional services, including a range of user interface components and
widgets for interacting with domain models. more information can be
found on the project's homepage.

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
%doc *.txt docs/* LICENSE*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

