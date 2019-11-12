%define oname rainbow_logging_handler

%def_disable check

Name: python3-module-%oname
Version: 2.2.2
Release: alt3

Summary: Ultimate Python colorized logger
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rainbow_logging_handler/
# https://github.com/laysakura/rainbow_logging_handler.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-logutils
BuildRequires: python3-module-nose-cov python3-module-pytest

%py3_provides %oname


%description
Ultimate Python colorized logger with user-custom color.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Ultimate Python colorized logger with user-custom color.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v

%files
%doc *.rst *.txt doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.2-alt3
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.2-alt2.git20140807.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.2-alt2.git20140807.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.2.2-alt2.git20140807
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140807
- Initial build for Sisyphus

