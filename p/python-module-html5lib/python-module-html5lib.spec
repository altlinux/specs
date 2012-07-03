%define module_name html5lib

%def_with python3

Name: python-module-%module_name
Version: 0.95
Release: alt3

Summary: Library for working with HTML5 documents

License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://code.google.com/p/html5lib

Source: %module_name-%version.tar

BuildRequires: python-module-setuptools

%setup_python_module %module_name

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

%package tests
Summary: Tests for html5lib
Group: Development/Python
Requires: %name = %version-%release

%description tests
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains tests for html5lib.

%if_with python3
%package -n python3-module-%module_name
Summary: Library for working with HTML5 documents (Python 3)
Group: Development/Python3

%description -n python3-module-%module_name
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

%package -n python3-module-%module_name-tests
Summary: Tests for html5lib (Python 3)
Group: Development/Python3
Requires: python3-module-%module_name = %version-%release

%description -n python3-module-%module_name-tests
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains tests for html5lib.
%endif

%prep
%setup -n %module_name-%version
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
%python_install --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc README
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%module_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt3
- Added modules for Python 3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Version 0.95

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.1-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt2.1
- Rebuilt with python 2.6

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt2
- install over --record option
- add README file

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt1
- Initial build for ALT Linux

