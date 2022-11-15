%define oname venusian

%def_with bootstrap
%def_without docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt1.1

Summary: A library for deferring decorator actions
License: BSD-derived
Group: Development/Python3
Url: http://pypi.python.org/pypi/venusian
BuildArch: noarch

# git://github.com/Pylons/venusian.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%add_python3_req_skip doesnt
%if_with bootstrap
%add_python3_req_skip doesnt.exist
%endif

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests

%description
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

%package tests
Summary: Tests for Venusian
Group: Development/Python3
Requires: %name = %version-%release
%add_python3_req_skip doesnt

%description tests
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains tests for Venusian.

%if_with docs
%package pickles
Summary: Pickles for Venusian
Group: Development/Python3

%description pickles
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains pickles for Venusian.

%package docs
Summary: Documentation for Venusian
Group: Development/Documentation

%description docs
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains documentation for Venusian.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

%build
%python3_build

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd docs
%make pickle
%make html
cp -fR _build/pickle %buildroot%python3_sitelibdir/%oname/
popd
%endif

cp -fR tests/ %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*
%endif


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 3.0.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- Version updated to 3.0.0
- build for python2 disabled

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Version 1.0

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0-alt1.a7
- Version 1.0a7

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a6
- Version 1.0a6
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2
- Version 1.0a2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

