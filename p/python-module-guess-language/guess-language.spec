%define oname guess-language

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.svn20100801.1.1
Summary: Guess the natural language of a text
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/guess-language/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://guess-language.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides guess_language

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-pytest rpm-build-python3 time python3-module-pytest

%description
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip blocks

%description tests
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Guess the natural language of a text
Group: Development/Python3
%py3_provides guess_language

%description -n python3-module-%oname
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

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
rm -fR build
py.test
#if_with python3
%if 0
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test.*

%files tests
%python_sitelibdir/*/*test.*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test.*
%exclude %python3_sitelibdir/*/*/*test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*test.*
%python3_sitelibdir/*/*/*test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.svn20100801.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.svn20100801.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20100801
- Initial build for Sisyphus

