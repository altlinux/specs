%define _unpackaged_files_terminate_build 1
%define oname zExceptions

Name: python3-module-%oname
Version: 3.4
Release: alt2

Summary: zExceptions contains common exceptions used in Zope2
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zExceptions/
# https://github.com/zopefoundation/zExceptions.git

Source0: https://pypi.python.org/packages/b2/19/20c6898e8a36bd76aa32c67671ed2c5f1c5d465c4290e7005844240c6b83/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-zope.security

%py3_requires zope.interface zope.publisher zope.security


%description
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

%package tests
Summary: Tests for zExceptions
Group: Development/Python3
Requires: %name = %version-%release

%description tests
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

This package contains tests for zExceptions.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.dev0.git20150331.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.dev0.git20150331.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev0.git20150331
- Version 3.0.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt1.1
- Rebuild with Python-2.7

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

