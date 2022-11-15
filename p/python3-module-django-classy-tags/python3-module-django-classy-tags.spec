%define _unpackaged_files_terminate_build 1
%define oname django-classy-tags

Name: python3-module-%oname
Version: 2.0.0
Release: alt1.1
Summary: Class based template tags for Django
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/django-classy-tags/
BuildArch: noarch

# https://pypi.org/project/django-classy-tags/#files
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Class based template tags for Django.

%package tests
Summary: tests for Django classytags
Group: Development/Python3
Requires: %name = %version-%release

%add_python3_self_prov_path %buildroot%python3_sitelibdir/classytags/tests

%description tests
Class based template tags for Django.

This package contains tests for Django classytags.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install
mv %buildroot%python3_sitelibdir/tests %buildroot%python3_sitelibdir/classytags/

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/classytags/tests

%files tests
%python3_sitelibdir/classytags/tests

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0
- Build python3 only

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4.1-alt1
- Version 0.3.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3.1-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3.1-alt1
- Version 0.3.3.1

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

