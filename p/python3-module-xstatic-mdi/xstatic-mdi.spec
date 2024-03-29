%define mname xstatic
%define oname %mname-mdi
%define pypi_name XStatic-mdi

Name: python3-module-%oname
Version: 1.6.50.2
Release: alt1

Summary: mdi (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.mdi
%py3_requires %mname.pkg


%description
mdi javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

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
* Tue Feb 06 2024 Ilfat Aminov <aminov@altlinux.org> 1.6.50.2-alt1
- 1.6.50.2

* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.57.0-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.57.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.57.0-alt2
- build as noarch

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.57.0-alt1
- 1.4.57.0

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.70.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.70.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.70.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.70.1-alt1
- Initial build for Sisyphus
