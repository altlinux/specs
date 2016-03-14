%define oname zope.release

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt2.svn20090727.1
Summary: Zope Release and Known-Good-Set (KGS) Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.release/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zc.buildout zc.lockfile zope.kgs

%description
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

%package -n python3-module-%oname
Summary: Zope Release and Known-Good-Set (KGS) Support
Group: Development/Python3
%py3_requires zope zc.buildout zc.lockfile zope.kgs

%description -n python3-module-%oname
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

%package -n python3-module-%oname-tests
Summary: Tests for zope.release
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

This package contains tests for zope.release.

%package tests
Summary: Tests for zope.release
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package has been developed to support the maintenance of a stable
set of Zope project distributions. It manages the controlled packages
configuration file and supports the generation of buildout configuration
files that can be used by developers.

This package contains tests for zope.release.

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
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt2.svn20090727.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2.svn20090727
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt1.svn20090727.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.svn20090727.1
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.svn20090727
- Initial build for Sisyphus

