%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname ZopeUndo

%def_with python3

Name: python-module-%oname
Version: 4.1
Release: alt1.1
Summary: ZODB undo support for Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/ZopeUndo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/ZopeUndo.git
Source0: https://pypi.python.org/packages/ce/40/51bc73896bdc23e1e16db55530c54f293d40d0a2c41e5a79efd4ea66dc1c/%{oname}-%{version}.zip
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package is included in Zope 2. It can be used in a ZEO server to
allow it to support Zope 2's undo log , without pulling in all of Zope
2.

%package -n python3-module-%oname
Summary: ZODB undo support for Zope2
Group: Development/Python3

%description -n python3-module-%oname
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package is included in Zope 2. It can be used in a ZEO server to
allow it to support Zope 2's undo log , without pulling in all of Zope
2.

%package -n python3-module-%oname-tests
Summary: Tests for ZopeUndo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package contains tests for ZopeUndo.

%package tests
Summary: Tests for ZopeUndo
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package contains tests for ZopeUndo.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev.git20130313.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20130313
- Version 4.0.1dev
- Enabled testing

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.0-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus

