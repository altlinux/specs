%def_with python3

Version: 0.7
Release: alt1.1
%setup_python_module genshi

Name: python-module-genshi
Summary: A toolkit for stream-based generation of output for the web
Source: %modulename-%version.tar
License: BSD
Group: Development/Python
Url: http://genshi.edgewall.org/
Packager: Python Development Team <python@packages.altlinux.org>

Obsoletes: python-module-Genshi

#BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

%package tests
Summary: Tests for Genshi
Group: Development/Python
Requires: %name = %EVR

%description tests
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

This package contains tests for Genshi.

%if_with python3
%package -n python3-module-genshi
Summary: A toolkit for stream-based generation of output for the web (Python 3)
Group: Development/Python
%add_python3_req_skip compiler

%description -n python3-module-genshi
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

%package -n python3-module-genshi-tests
Summary: Tests for Genshi
Group: Development/Python
Requires: python3-module-genshi = %EVR

%description -n python3-module-genshi-tests
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

This package contains tests for Genshi.
%endif

%package doc
Summary: Documentation for Genshi
Group: Development/Documentation
BuildArch: noarch

%description doc
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

This package contains documentation for Genshi.

%package examples
Summary: Examples for Genshi
Group: Development/Documentation
BuildArch: noarch

%description examples
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

This package contains examples for Genshi.

%prep
%setup  -q -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install --optimize=2 --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%dir %python_sitelibdir/%modulename
%dir %python_sitelibdir/%modulename/filters/
%dir %python_sitelibdir/%modulename/template/
%exclude %python_sitelibdir/%modulename/tests
%exclude %python_sitelibdir/%modulename/*/tests

%files tests
%python_sitelibdir/%modulename/tests
%python_sitelibdir/%modulename/*/tests

%files doc
%doc doc

%files examples
%doc examples

%if_with python3
%files -n python3-module-genshi
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%modulename/tests
%exclude %python3_sitelibdir/%modulename/*/tests

%files -n python3-module-genshi-tests
%python3_sitelibdir/%modulename/tests
%python3_sitelibdir/%modulename/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt2.1
- Rebuild with Python-3.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6
- Added docs and examples

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Rebuilt with python 2.6

* Sun Nov 16 2008 Ivan Fedorov <ns@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sun Jan 06 2008 Ivan Fedorov <ns@altlinux.org> 0.4.4-alt2
- fix building

* Sun Jan 06 2008 Ivan Fedorov <ns@altlinux.org> 0.4.4-alt1
- Initial build for ALT Linux Sisyphus.
