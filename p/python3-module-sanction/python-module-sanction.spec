%define oname sanction

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: A simple, lightweight OAuth2 client
License: MIT
Group: Development/Python3
Url: https://github.com/demianbrecht/sanction
BuildArch: noarch

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/s/sanction/sanction-0.4.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Sanction is a ridiculously easy to use OAuth 2.0 client intended for rapid
development against OAuth 2.0 providers with minimal keyboard bashing.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/*.egg-*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- python2 disabled

* Mon Jul 25 2016 Vladimir Didenko <cow@altlinux.ru> 0.4.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.ru> 0.4.0-alt1
- initial build for Sisyphus
