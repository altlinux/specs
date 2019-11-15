%define oname tgmochikit

Name: python3-module-%oname
Version: 1.4.2
Release: alt3

Summary: MochiKit packaged as TurboGears widgets
License: AFL/MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/tgMochiKit/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
MochiKit packaged as TurboGears widgets.

%package tests
Summary: Tests for tgMochiKit
Group: Development/Python3
Requires: %name = %version-%release

%description tests
MochiKit packaged as TurboGears widgets.

This package contains tests for tgMochiKit.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc ChangeLog PKG-INFO *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.2-alt3
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4.2-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

