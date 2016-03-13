%define oname ore.alchemist

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt3.1
Summary: sqlalchemy zope3 integration
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/ore.alchemist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: sqlalchemy zope3 integration
Group: Development/Python3
%py3_requires ore transaction SQLAlchemy

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/* LICENSE*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/* LICENSE*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

