%define unpackaged_files_terminate_build 1

%define mname jwcrypto

Name: python-module-%mname
Version: 0.4.2
Release: alt1%ubt
Summary: JWCrypto is an implementation of the Javascript Object Signing and Encryption (JOSE) Web Standards

Group: Development/Python
License: %lgpl3only
Url: https://github.com/latchset/jwcrypto

BuildArch: noarch
%py_provides %mname

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python-module-cryptography
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cryptography

%description
An implementation of the JOSE Working Group documents:
RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of Protecting Content Using JSON Object Signing and
           Encryption (JOSE)

%package -n python3-module-%mname
Summary: JWCrypto is an implementation of the Javascript Object Signing and Encryption (JOSE) Web Standards
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
An implementation of the JOSE Working Group documents:
RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of Protecting Content Using JSON Object Signing and
           Encryption (JOSE)
This is a Python3 module.

%prep
%setup
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%check
python -bb -m pytest --verbose %mname/test*.py
pushd ../python3
python3 -bb -m pytest --verbose %mname/test*.py
popd

%install
%python_install
pushd ../python3
%python3_install
popd
#do not pack docs and tests
rm -rfv %buildroot%_defaultdocdir/%mname
rm -rfv %buildroot%python_sitelibdir/%mname/tests*
rm -rfv %buildroot%python3_sitelibdir/%mname/tests*

%files
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-py2.?.egg-info

%files -n python3-module-%mname
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info

%changelog
* Tue Oct 24 2017 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1%ubt
- New 0.4.2 version

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Initial build.

