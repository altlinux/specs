%define oname pycountry

%def_with python3

%if_with python3
%define py3name python3-module-%oname
%define py3dir %py3name-%version
%endif

Name: python-module-%oname
Version: 1.10
Release: alt1.1.1
Summary: ISO country, subdivision, language, currency and script definitions
License: LGPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/pycountry

# hg clone https://bitbucket.org/gocept/pycountry
Source: %name-%version.tar
Patch10: %name-%version-alt-python3.patch

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose

%if_with python3
BuildPreReq: rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools python3-module-nose
%endif

%description
ISO country, subdivision, language, currency and script definitions and
their translations.

%package tests
Summary: Tests ISO country, subdivision, language, currency and script definitions
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description tests
Tests for ISO country, subdivision, language, currency and script
definitions and their translations.

%if_with python3
%package -n %py3name
Summary: Python3 ISO country, subdivision, language, currency and script definitions
Group: Development/Python3
BuildArch: noarch

%description -n %py3name
ISO country, subdivision, language, currency and script definitions and
their translations for Python3.

%package -n %py3name-tests
Summary: Python3 tests ISO country, subdivision, language, currency and script definitions
Group: Development/Python3
BuildArch: noarch
Requires: %py3name = %EVR

%description -n %py3name-tests
Tests for ISO country, subdivision, language, currency and script
definitions and their translations for Python3.

%endif

%prep
%setup
%patch10 -p1
%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
%endif

%build
%python_build_debug
%if_with python3
pushd ../%py3dir
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../%py3dir
%python3_install
popd
%endif

%check
python setup.py test
nosetests
%if_with python3
pushd ../%py3dir
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests.*

%files tests
%python_sitelibdir/%oname/tests.*

%if_with python3
%files -n %py3name
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests.*
%exclude %python3_sitelibdir/%oname/__pycache__/tests.*

%files -n %py3name-tests
%python3_sitelibdir/%oname/tests.*
%python3_sitelibdir/%oname/__pycache__/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Version 1.10

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0
- Version 1.3.dev0

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.8-alt1.1
- Fixed build

* Fri Mar 15 2013 Aleksey Avdeev <solo@altlinux.ru> 0.14.8-alt1
- Version 0.14.8
- Add %%name-tests subpackage
- Added module for Python 3

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.5-alt1
- Initial build for Sisyphus
