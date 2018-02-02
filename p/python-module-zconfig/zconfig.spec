%define _unpackaged_files_terminate_build 1
%define oname zconfig

%def_with python3

Name: python-module-%oname
Version: 3.2.0
Release: alt1.1

Summary: Python configuration module from Zope
License: ZPL
Group: Development/Python

Url: http://pypi.python.org/pypi/ZConfig/
BuildArch: noarch

# https://github.com/zopefoundation/ZConfig.git
Source: %name-%version.tar
# https://github.com/zopefoundation/ZConfig/issues/34
Patch1: %oname-%version-upstream-schema2html.patch

%setup_python_module %oname
BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-zope.testrunner python2.7(manuel) python2.7(manuel.testing) python2.7(docutils)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-zope.testrunner python3(manuel) python3(manuel.testing) python3(docutils)
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
%package -n python3-module-%oname
Summary: Python 3 configuration module from Zope
Group: Development/Python3

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for ZConfig
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testrunner manuel manuel.testing docutils

%description -n python3-module-%oname-tests
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
%py_requires zope.testrunner manuel manuel.testing docutils

%description tests
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig\'s model is very different
from the model supported by the ConfigParser module found in Python\'s standard
library, and is more suitable to configuration-intensive applications.

This package contains tests for ZConfig.

%prep
%setup
%patch1 -p1

%if_with python3
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

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

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
%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.
- Fixed python3 build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt3.dev.git20140320.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt3.dev.git20140320
- cleanup buildreq

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt2.dev.git20140320
- Enabled testing

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.dev.git20140320
- Version 3.0.5dev

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt2.git20131015
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt2.git20130313
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.git20130313
- Version 3.0.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.9.2-alt1.1
- Rebuild with Python-3.3

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

