%define _unpackaged_files_terminate_build 1

%define mname jwcrypto
%def_without python3

Name: python-module-%mname
Version: 0.2.1
Release: alt1
Summary: Implements JWK,JWS,JWE specifications

Group: Development/Python
License: %bsdstyle
Url: https://github.com/simo5/jwcrypto

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-cryptography

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-cryptography
%endif

%setup_python_module %mname

%description
An implementation of the JOSE Working Group documents:
RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of Protecting Content Using JSON Object Signing and
           Encryption (JOSE)

%if_with python3
%package -n python3-module-%mname
Summary: Implements JWK,JWS,JWE specifications
Group: Development/Python3

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
%endif

%prep
%setup
#patch -p1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%_defaultdocdir/%mname
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%mname
%_defaultdocdir/%mname
%python3_sitelibdir/*
%endif

%changelog
* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Initial build.

