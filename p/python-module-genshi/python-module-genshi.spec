%def_with python3

Version: 0.6
Release: alt2
%setup_python_module genshi

Name: python-module-genshi
Summary: A toolkit for stream-based generation of output for the web
Source: %modulename-%version.tar
License: BSD
Group: Development/Python
Url: http://genshi.edgewall.org/
Packager: Python Development Team <python@packages.altlinux.org>

Obsoletes: python-module-Genshi

BuildArch: noarch
BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

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
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
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

%files doc
%doc doc

%files examples
%doc examples

%if_with python3
%files -n python3-module-genshi
%python3_sitelibdir/*
%endif

%changelog
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
