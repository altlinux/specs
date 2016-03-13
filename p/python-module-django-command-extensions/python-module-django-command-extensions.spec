%define module_name django-command-extensions

%define git_commit 1fe658

%def_with python3

Name: python-module-%module_name
Version: 1.3.9
Release: alt1.dev.git%git_commit.1

Summary: Management extensions for the Django Framework

License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-command-extensions

# https://github.com/django-extensions/django-extensions.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Management extensions for the Django Framework.

%package -n python3-module-%module_name
Summary: Management extensions for the Django Framework
Group: Development/Python3

%description -n python3-module-%module_name
Management extensions for the Django Framework.

%package -n python3-module-%module_name-tests
Summary: Tests for django-command-extensions
Group: Development/Python3
Requires: python3-module-%module_name = %version-%release

%description -n python3-module-%module_name-tests
Management extensions for the Django Framework.

This package contains tests for django-command-extensions.

%package tests
Summary: Tests for django-command-extensions
Group: Development/Python
Requires: %name = %version-%release

%description tests
Management extensions for the Django Framework.

This package contains tests for django-command-extensions.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/*
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.9-alt1.dev.git1fe658.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.9-alt1.dev.git1fe658
- Version 1.3.9.dev
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7pre-alt1.git5e0582.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7pre-alt1.git5e0582
- Version 0.7pre
- Extracted tests into separate package

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.4.2pre-alt2.git9bf983
- fix inherit with alt gear-repo

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.4.2pre-alt1.git9bf983
- new version
- using rpm-build-python macros

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.gitee7c76.1
- Rebuilt with python 2.6

* Wed Oct 07 2009 Denis Klimov <zver@altlinux.org> 0.4.1-alt1.gitee7c76
- new version

* Thu Jan 22 2009 Denis Klimov <zver@altlinux.org> 0.3-alt1
- Initial build for ALT Linux

