%define modulename zconfig

%def_with python3

Name: python-module-%modulename
Version: 2.9.2
Release: alt1

Summary: Python configuration module from Zope
License: ZPL
Group: Development/Python

Url: http://pypi.python.org/pypi/ZConfig/
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%setup_python_module %modulename
BuildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig\'s model is very different
from the model supported by the ConfigParser module found in Python\'s standard
library, and is more suitable to configuration-intensive applications.

ZConfig schema are written in an XML-based language and are able to \"import\"
schema components provided by Python packages. Since components are able to
bind to conversion functions provided by Python code in the package (or
elsewhere), configuration objects can be arbitrarily complex, with values that
have been verified against arbitrary constraints. This makes it easy for
applications to separate configuration support from configuration loading even
with configuration data being defined and consumed by a wide range of separate
packages.

Authors:
--------
Zope Corporation < zodb-devAATTzope.org>

%if_with python3
%package -n python3-module-%modulename
Summary: Python 3 configuration module from Zope
Group: Development/Python3

%description -n python3-module-%modulename
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig\'s model is very different
from the model supported by the ConfigParser module found in Python\'s standard
library, and is more suitable to configuration-intensive applications.

ZConfig schema are written in an XML-based language and are able to \"import\"
schema components provided by Python packages. Since components are able to
bind to conversion functions provided by Python code in the package (or
elsewhere), configuration objects can be arbitrarily complex, with values that
have been verified against arbitrary constraints. This makes it easy for
applications to separate configuration support from configuration loading even
with configuration data being defined and consumed by a wide range of separate
packages.

Authors:
--------
Zope Corporation < zodb-devAATTzope.org>

%package -n python3-module-%modulename-tests
Summary: Tests for ZConfig
Group: Development/Python3
Requires: python3-module-%modulename = %version-%release
%py3_requires zope.testrunner

%description -n python3-module-%modulename-tests
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig\'s model is very different
from the model supported by the ConfigParser module found in Python\'s standard
library, and is more suitable to configuration-intensive applications.

This package contains tests for ZConfig.
%endif

%package tests
Summary: Tests for ZConfig
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testrunner

%description tests
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig\'s model is very different
from the model supported by the ConfigParser module found in Python\'s standard
library, and is more suitable to configuration-intensive applications.

This package contains tests for ZConfig.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py') scripts/zconfig*; do
	2to3 -w $i
done
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
	mv $i py3_$i
done
popd
%endif

%python_install

%files
%_bindir/*
%exclude %_bindir/py3_*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%modulename
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%modulename-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.2-alt1
- Version 2.9.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.9.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt2
- Added necessary requirements

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt1
- Version 2.9.0

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.1
- Rebuilt with python 2.6

* Tue Mar 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.6.2-alt1
- Initial build for Sisyphus

