%define mname xstatic
%define oname %mname-angular-ui
%define pypi_name XStatic-angular-ui

Name: python3-module-%oname
Version: 0.4.0.1
Release: alt3

Summary: angular-ui (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.angular_ui
%py3_requires %mname.pkg


%description
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

This package contains tests for %oname.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/pkg/*/*/test
%exclude %python3_sitelibdir/%mname/pkg/*/*/*/test
%exclude %python3_sitelibdir/%mname/pkg/*/*/*/*/*/test
%exclude %python3_sitelibdir/*.pth

%files tests
%python3_sitelibdir/%mname/pkg/*/*/test
%python3_sitelibdir/%mname/pkg/*/*/*/test
%python3_sitelibdir/%mname/pkg/*/*/*/*/*/test


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.0.1-alt2
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0.1-alt1
- Initial build for Sisyphus

