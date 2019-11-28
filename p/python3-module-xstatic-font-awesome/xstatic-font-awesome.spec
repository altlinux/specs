%define mname xstatic
%define oname %mname-font-awesome
%define pypi_name XStatic-Font-Awesome

Name: python3-module-%oname
Version: 4.7.0.0
Release: alt2

Summary: Font-Awesome (XStatic packaging standard)
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.font_awesome
%py3_requires %mname.pkg


%description
Font Awesome icons packaged for setuptools (easy_install) / pip.

This package is intended to be used by **any** project that needs these
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
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.7.0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.7.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 4.7.0.0-alt1
- 4.7.0.0
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.0.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.3.0.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 4.3.0.0-alt1
- 4.3.0.0

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0.0-alt1
- Version 4.2.0.0

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0.0-alt1
- Initial build for Sisyphus

