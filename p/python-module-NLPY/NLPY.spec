%define oname NLPY

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141106
Summary: Natural Language Processing on Python
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/nlpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zomux/nlpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: libnumpy-devel python-module-gensim
BuildPreReq: python-module-nltk
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: libnumpy-py3-devel python3-module-gensim
BuildPreReq: python3-module-nltk python-tools-2to3
%endif

%py_provides nlpy

%description
nlpy - A NLP (Natural Language Processing) tookit focusing on high level
tasks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
nlpy - A NLP (Natural Language Processing) tookit focusing on high level
tasks.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Natural Language Processing on Python
Group: Development/Python3
%py3_provides nlpy

%description -n python3-module-%oname
nlpy - A NLP (Natural Language Processing) tookit focusing on high level
tasks.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
nlpy - A NLP (Natural Language Processing) tookit focusing on high level
tasks.

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
cp -fR nlpy %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
%python3_install
cp -fR nlpy %buildroot%python3_sitelibdir/
popd
%endif

%check
export PYTHONPATH=$PWD
python nlpy/test/ex/FrequencyKeywordExtractorTest.py
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 nlpy/test/ex/FrequencyKeywordExtractorTest.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141106
- Initial build for Sisyphus

