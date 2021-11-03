%define oname idna

Name: python3-module-%oname
Version: 3.3
Release: alt1

Summary: A library to support the Internationalised Domain Names in Applications (IDNA)

License: BSD
Group: Development/Python3
Url: https://github.com/kjd/idna

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires: python3-module-setuptools rpm-build-python3

%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This version of the protocol is often referred
to as "IDNA2008" and can produce different results from the earlier standard from 2003.

%prep
%setup -n %oname-%version


%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Wed Nov 3 2021 Vladimir Didenko <cow@altlinux.org> 3.3-alt1
- New version

* Fri Jun 18 2021 Vladimir Didenko <cow@altlinux.org> 3.2-alt1
- New version

* Thu Mar 4 2021 Vladimir Didenko <cow@altlinux.org> 3.1-alt1
- New version

* Fri Jul 17 2020 Vladimir Didenko <cow@altlinux.org> 2.10-alt1
- New version
- Build Python3 version as separate package

* Wed Mar 18 2020 Vladimir Didenko <cow@altlinux.org> 2.9-alt1
- New version

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.org> 2.8-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 2.7-alt1
- New version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 2.6-alt1
- New version

* Wed Mar 15 2017 Vladimir Didenko <cow@altlinux.org> 2.5-alt1
- New version

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 2.4-alt1
- New version

* Thu Feb 2 2017 Vladimir Didenko <cow@altlinux.org> 2.2-alt1
- New version

* Fri Jul 22 2016 Vladimir Didenko <cow@altlinux.org> 2.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Jun 7 2015 Vladimir Didenko <cow@altlinux.ru> 2.0-alt1
- initial build for Sisyphus
