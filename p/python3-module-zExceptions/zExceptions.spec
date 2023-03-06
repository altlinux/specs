%define _unpackaged_files_terminate_build 1
%define oname zExceptions

%def_with check

Name: python3-module-%oname
Version: 4.3
Release: alt1

Summary: zExceptions contains common exceptions used in Zope
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zExceptions/

Source0: https://files.pythonhosted.org/packages/48/24/dcde412a61b9c30289a07a0357d5583074254f70aa7521c426e19be5579c/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-zope.testrunner
%endif

%description
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope.

%package tests
Summary: Tests for zExceptions
Group: Development/Python3
Requires: %name = %EVR

%description tests
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope.

This package contains tests for zExceptions.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests


%changelog
* Mon Mar 06 2023 Anton Vyatkin <toni@altlinux.org> 4.3-alt1
- new version 4.3

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

