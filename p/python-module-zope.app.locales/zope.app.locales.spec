%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.app.locales

%def_with python3

Name: python-module-%oname
Version: 3.7.5
#Release: alt2.1
Summary: Zope locale extraction and management utilities
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.locales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/42/07/718c965a36b97827d90c2a80b913ccdad4479e97ffe6433be64a2ac6ab50/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app zope.i18nmessageid zope.interface

%description
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

%package -n python3-module-%oname
Summary: Zope locale extraction and management utilities
Group: Development/Python3
%py3_requires zope.app zope.i18nmessageid zope.interface

%description -n python3-module-%oname
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.locales
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.i18n zope.tal zope.testing

%description -n python3-module-%oname-tests
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

This package contains tests for zope.app.locales.

%package tests
Summary: Tests for zope.app.locales
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.i18n zope.tal zope.testing

%description tests
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

This package contains tests for zope.app.locales.

%prep
%setup -q -n %{oname}-%{version}

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
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.5-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.4-alt2.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Version 3.7.4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Version 3.7.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

