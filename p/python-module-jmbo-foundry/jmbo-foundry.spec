%define oname jmbo-foundry

%def_with python3

Name: python-module-%oname
Version: 1.2.6.1
Release: alt1.git20141107
Summary: Jmbo generic behaviour/templates app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-foundry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-foundry.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Jmbo Foundry ties together the various Jmbo products enabling you to
rapidly build multilingual web and mobi sites with the minimum amount of
code and customization.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jmbo Foundry ties together the various Jmbo products enabling you to
rapidly build multilingual web and mobi sites with the minimum amount of
code and customization.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Jmbo generic behaviour/templates app
Group: Development/Python3

%description -n python3-module-%oname
Jmbo Foundry ties together the various Jmbo products enabling you to
rapidly build multilingual web and mobi sites with the minimum amount of
code and customization.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jmbo Foundry ties together the various Jmbo products enabling you to
rapidly build multilingual web and mobi sites with the minimum amount of
code and customization.

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/foundry/templates/basic/foundry/test*

%files tests
%python_sitelibdir/*/tests.*
%python_sitelibdir/foundry/templates/basic/foundry/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/foundry/templates/basic/foundry/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/foundry/templates/basic/foundry/test*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6.1-alt1.git20141107
- Version 1.2.6.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5.1-alt1.git20140715
- Initial build for Sisyphus

