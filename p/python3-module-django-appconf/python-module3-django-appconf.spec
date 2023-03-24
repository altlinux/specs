%define oname django-appconf

Name: python3-module-%oname
Version: 1.0.5
Release: alt1

Summary: A helper class for handling configuration defaults of packaged apps gracefully

Group: Development/Python3
License: BSD
Url: http://django-appconf.readthedocs.org

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
A helper class for handling configuratio defaults of packaged Django
apps gracefully.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 1.0.5-alt1
- 1.0.5

* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.4-alt1
- 1.0.4
- Build python3 only package.

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt4.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt4.1.1
- NMU: Use buildreq for BR.

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt4.1
- Added module for Python 3

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt4
- Fix build

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3
- cleanup spec, drop direct install requires

* Fri Jul 19 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt2
- Respect Autoimports/Sisyphus version

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt1
- Initial release for Sisyphus (based on Fedora)
