%define mname xstatic
%define oname %mname-angular-bootstrap
%define pypi_name XStatic-Angular-Bootstrap

Name: python3-module-%oname
Version: 2.2.0.0
Release: alt2

Summary: Angular-Bootstrap (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.angular_bootstrap
%py3_requires %mname.pkg


%description
Angular-Bootstrap JavaScript library packaged for setuptools
(easy_install) / pip.

This package is intended to be used by any project that needs these
files.

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
%exclude %python3_sitelibdir/*.pth


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 2.2.0.0-alt1
- 2.2.0.0
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0.2-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.0.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0.2-alt1
- Initial build for Sisyphus

