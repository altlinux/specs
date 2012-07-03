%define oname markupsafe

%def_with python3

Name: python-module-%oname
Version: 0.15
Release: alt1
Summary: implements a XML/HTML/XHTML Markup safe string for Python

Group: Development/Python
License: GPL
Url: http://pypi.python.org/pypi/MarkupSafe

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: implements a XML/HTML/XHTML Markup safe string for Python 3
Group: Development/Python3

%description -n python3-module-%oname
%summary

%package -n python3-module-%oname-tests
Summary: Tests for MarkupSafe (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
%summary

This package contains tests for MarkupSafe.
%endif

%package tests
Summary: Tests for MarkupSafe
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for MarkupSafe.

%prep
%setup -q
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files
%python_sitelibdir/markupsafe
%exclude %python_sitelibdir/markupsafe/tests.*
%python_sitelibdir/MarkupSafe-%version-py?.?.egg-info
%doc AUTHORS LICENSE README.rst

%files tests
%python_sitelibdir/markupsafe/tests.*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/__pycache__/tests.*
%exclude %python3_sitelibdir/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/__pycache__/tests.*
%python3_sitelibdir/*/tests.*
%endif

%changelog
* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1
- Version 0.15
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1
- Rebuild with Python-2.7

* Tue Mar 01 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.3-alt1
- New version 0.9.3

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.2-alt1
- initial build

