%define oname pycedict

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20150113.1
Summary: A library for parsing CEDict and adding tone marks to pinyin
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pycedict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jdillworth/pycedict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides cedict
%add_python_req_skip cedict_parser pinyin

%description
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A library for parsing CEDict and adding tone marks to pinyin
Group: Development/Python3
%py3_provides cedict

%description -n python3-module-%oname
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
python cedict/tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150113
- Initial build for Sisyphus

