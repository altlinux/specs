%define version 1.1.1
%define release alt1.3
%setup_python_module Extremes

%def_with python3

Name: %packagename
Version:%version
Release: alt1.3.1

Summary: Production-quality 'Min' and 'Max' objects

License: PSF or ZPL
Group: Development/Python
BuildArch: noarch
Url:  http://pypi.python.org/pypi/Extremes
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The ``peak.util.extremes`` module provides a production-quality implementation
of the ``Min`` and ``Max`` objects from PEP 326.  While PEP 326 was rejected
for inclusion in the language or standard library, the objects described in it
are useful in a variety of applications.  In PEAK, they have been used to
implement generic functions (in RuleDispatch and PEAK-Rules), as well as to
handle scheduling and time operations in the Trellis.  Because this has led to
each project copying the same code, we've now split the module out so it can
be used independently.

%package -n python3-module-%modulename
Summary: Production-quality 'Min' and 'Max' objects
Group: Development/Python3

%description -n python3-module-%modulename
The ``peak.util.extremes`` module provides a production-quality implementation
of the ``Min`` and ``Max`` objects from PEP 326.  While PEP 326 was rejected
for inclusion in the language or standard library, the objects described in it
are useful in a variety of applications.  In PEAK, they have been used to
implement generic functions (in RuleDispatch and PEAK-Rules), as well as to
handle scheduling and time operations in the Trellis.  Because this has led to
each project copying the same code, we've now split the module out so it can
be used independently.

%prep
%setup -n %modulename-%version

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/peak/util/extremes*
%python_sitelibdir/Extremes*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/peak/util/extremes*
%python3_sitelibdir/peak/util/__pycache__
%python3_sitelibdir/Extremes*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.2.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.2
- Fixed build

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.1.1-alt1
- Initial build for ALT Linux

