%define oname texttable

Name: python3-module-%oname
Version: 1.6.7
Release: alt1

Summary: Module for creating simple ASCII tables

License: %lgpl3only
Group: Development/Python3
Url: https://github.com/foutaise/texttable

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
texttable is a module to generate a formatted text table, using ASCII characters.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%python3_sitelibdir/%oname.*
%python3_sitelibdir/*.egg-*
%python3_sitelibdir/__pycache__/*

%changelog
* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.ru> 1.6.7-alt1
- 1.6.7

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Tue Jan 26 2021 Vladimir Didenko <cow@altlinux.ru> 1.6.3-alt1
- 1.6.3
- build Python 3 version only

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.3-alt1
- 0.8.3
