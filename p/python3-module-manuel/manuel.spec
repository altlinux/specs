%define oname manuel

Name: python3-module-%oname
Version: 1.10.1
Release: alt2

Summary: Manuel lets you build tested documentation
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/manuel/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-zope.testing
BuildRequires: python-tools-2to3

%py3_requires six


%description
Manuel lets you build tested documentation.

%package tests
Summary: Tests for Manuel
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
Manuel lets you build tested documentation.

This package contains tests for Manuel.

%package docs
Summary: Documentation for Manuel
Group: Development/Documentation

%description docs
Manuel lets you build tested documentation.

This package contains documentation for Manuel.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*

%files tests
%python3_sitelibdir/%oname/test*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.1-alt2
- Build for python2 disabled.

* Tue Apr 23 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.10.1-alt1
- update to 1.10.1 to fix build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Version 1.7.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

