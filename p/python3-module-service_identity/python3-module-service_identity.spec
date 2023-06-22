%define oname service_identity

Name: python3-module-%oname
Version: 23.1.0
Release: alt1

Summary: Service identity verification for pyOpenSSL (Python 3)

License: MIT
Group: Development/Python3
Url: https://github.com/pyca/service_identity

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/s/service_identity/service_identity-1.0.0.tar.gz
Source: %oname-%version.tar
BuildArch: noarch
Provides: python3-module-service-identity = %version-%release
Obsoletes: python3-module-service-identity <= 18.1.0

BuildPreReq: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-fancy-pypi-readme)
BuildRequires: python3(hatch-vcs)
BuildRequires: git

%description
Use this package if you use pyOpenSSL and don't want to be MITMed.
service_identity aspires to give you all the tools you need for verifying whether
a certificate is valid for the intended purposes. In the simplest case, this means host
name verification. However, service_identity implements RFC 6125 fully and plans to add
other relevant RFCs too.

%prep
%setup -n %oname-%version

%build
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Thu Jun 22 2023 Vladimir Didenko <cow@altlinux.org> 23.1.0-alt1
- new version

* Thu May 27 2021 Vladimir Didenko <cow@altlinux.org> 21.1.0-alt1
- build python3 version as a standalone version
- rename package to python3-module-service_identity

* Fri Feb 15 2019 Vladimir Didenko <cow@altlinux.org> 18.1.0-alt1
- new version
- obsolete duplicate package (closes: #35296)

* Fri Jun 9 2017 Vladimir Didenko <cow@altlinux.org> 17.0.0-alt1
- new version

* Fri Jul 22 2016 Vladimir Didenko <cow@altlinux.org> 16.0.0-alt1
- new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 14.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 14.0.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.org> 14.0.0-alt1
- new version

* Thu Jul 31 2014 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
