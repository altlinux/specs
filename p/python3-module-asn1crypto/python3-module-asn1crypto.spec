%define oname asn1crypto

Name: python3-module-%oname
Version: 1.5.1
Release: alt1

Summary: Python ASN.1 parser

License: %mit
Group: Development/Python3
Url: https://pypi.python.org/pypi/asn1crypto
Packager: Vladimir Didenko <cow@altlinux.org>
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python3 python3-module-setuptools

%description
Fast ASN.1 parser and serializer with definitions for private keys, public keys,
certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509
and TSP.


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
* Tue Mar 29 2022 Vladimir Didenko <cow@altlinux.ru> 1.5.1-alt1
- New version

* Fri Sep 4 2020 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- New version
- Build Python 3 version as separate package

* Tue Jan 28 2020 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- New version

* Thu Oct 17 2019 Vladimir Didenko <cow@altlinux.ru> 1.2.0-alt1
- New version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.ru> 0.24.0-alt1
- New version

* Wed Oct 18 2017 Vladimir Didenko <cow@altlinux.ru> 0.23.0-alt1
- New version

* Mon Mar 20 2017 Vladimir Didenko <cow@altlinux.ru> 0.22.0-alt1
- New version

* Mon Mar 13 2017 Vladimir Didenko <cow@altlinux.ru> 0.21.1-alt1
- Initial build for Sisyphus
