%define oname stsci.distutils

%def_with python3

Name: python-module-%oname
Version: 0.3.7
Release: alt1.1

Summary: distutils/packaging-related utilities used by some of STScI's packages
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/stsci.distutils/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-d2to1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3 python3-module-d2to1
%endif

Requires: python-module-stsci.core = %EVR
Requires: python-module-zest.releaser

%description
This package contains utilities used to package some of STScI's Python
projects; specifically those projects that comprise stsci_python and
Astrolib.

It currently consists mostly of some setup_hook scripts meant for use
with distutils2/packaging and/or d2to1, and a customized easy_install
command meant for use with distribute.

This package is not meant for general consumption, though it might be
worth looking at for examples of how to do certain things with your own
packages, but YMMV.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains utilities used to package some of STScI's Python
projects; specifically those projects that comprise stsci_python and
Astrolib.

It currently consists mostly of some setup_hook scripts meant for use
with distutils2/packaging and/or d2to1, and a customized easy_install
command meant for use with distribute.

This package is not meant for general consumption, though it might be
worth looking at for examples of how to do certain things with your own
packages, but YMMV.

This package contains tests for %oname.

%package -n python-module-stsci.core
Summary: Core package for stsci
Group: Development/Python

%description -n python-module-stsci.core
Core package for stsci.

%if_with python3
%package -n python3-module-%oname
Summary: distutils/packaging-related utilities used by some of STScI's packages
Group: Development/Python3
Requires: python3-module-stsci.core = %EVR
Requires: python3-module-zest.releaser

%description -n python3-module-%oname
This package contains utilities used to package some of STScI's Python
projects; specifically those projects that comprise stsci_python and
Astrolib.

It currently consists mostly of some setup_hook scripts meant for use
with distutils2/packaging and/or d2to1, and a customized easy_install
command meant for use with distribute.

This package is not meant for general consumption, though it might be
worth looking at for examples of how to do certain things with your own
packages, but YMMV.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains utilities used to package some of STScI's Python
projects; specifically those projects that comprise stsci_python and
Astrolib.

It currently consists mostly of some setup_hook scripts meant for use
with distutils2/packaging and/or d2to1, and a customized easy_install
command meant for use with distribute.

This package is not meant for general consumption, though it might be
worth looking at for examples of how to do certain things with your own
packages, but YMMV.

This package contains tests for %oname.

%package -n python3-module-stsci.core
Summary: Core package for stsci
Group: Development/Python

%description -n python3-module-stsci.core
Core package for stsci.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

touch %buildroot%python_sitelibdir/stsci/__init__.py

%if_with python3
pushd ../python3
%python3_install
touch %buildroot%python3_sitelibdir/stsci/__init__.py
popd
%endif

%files
%doc *.txt
%python_sitelibdir/stsci/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/stsci/__init__.py*
%exclude %python_sitelibdir/stsci/distutils/tests

%files tests
%python_sitelibdir/stsci/distutils/tests

%files -n python-module-stsci.core
%python_sitelibdir/stsci/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/stsci/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/stsci/__init__.py
%exclude %python3_sitelibdir/stsci/distutils/tests
%exclude %python3_sitelibdir/stsci/__pycache__

%files -n python3-module-%oname-tests
%python3_sitelibdir/stsci/distutils/tests

%files -n python3-module-stsci.core
%python3_sitelibdir/stsci/__init__.py
%python3_sitelibdir/stsci/__pycache__
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Version 0.3.7
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

