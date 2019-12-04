%define oname TGScheduler

Name: python3-module-%oname
Version: 1.7.0
Release: alt2

Summary: Turbogears Scheduler
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/TGScheduler
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires dateutil


%description
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

%package tests
Summary: Tests for Turbogears Scheduler
Group: Development/Python3
Requires: %name = %EVR

%description tests
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

This package contains tests for Turbogears Scheduler.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.0-alt2
- python2 disabled

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1
- NMU update to 1.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.3-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt3
- Added necessary requirements

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt2
- Added module for Python 3

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus

