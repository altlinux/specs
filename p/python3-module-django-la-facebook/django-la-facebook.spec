%define _unpackaged_files_terminate_build 1
%define oname django-la-facebook

%def_with bootstrap
%def_with docs
%def_without tests

Name: python3-module-%oname
Version: 0.1.1
Release: alt3

Summary: Definitive facebook auth for Django
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-la-facebook/
BuildArch: noarch

# https://github.com/cartwheelweb/django-la-facebook.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: python3-module-sphinx
%endif
BuildRequires: python-tools-2to3

%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults
%endif

%py3_requires django


%description
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

%if_with tests
%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains tests for %oname.
%endif

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains documentation for %oname.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/test_project
%exclude %python3_sitelibdir/*/tests

%if_with tests
%files tests
%python3_sitelibdir/*/tests
%endif

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt3
- build for python2 disabled

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20110418.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20110418.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20110418
- Initial build for Sisyphus

