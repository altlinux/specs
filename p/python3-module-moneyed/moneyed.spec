%define _unpackaged_files_terminate_build 1
%define oname moneyed

Name: python3-module-%oname
Version: 0.7
Release: alt2

Summary: Provides Currency and Money classes for use in your Python code
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/py-moneyed/
# https://github.com/limist/py-moneyed.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-tox

%py3_provides %oname


%description
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

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
rm -fR build
py.test3 -vv

%files
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to upstream version 0.7.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150212
- Initial build for Sisyphus

