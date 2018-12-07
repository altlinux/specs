%define _unpackaged_files_terminate_build 1

%define mname jwcrypto
%def_with check

Name: python-module-%mname
Version: 0.6.0
Release: alt1
Summary: JWCrypto is an implementation of the Javascript Object Signing and Encryption (JOSE) Web Standards

Group: Development/Python
License: %lgpl3only
Url: https://github.com/latchset/jwcrypto

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-coverage
BuildRequires: python-module-cryptography
BuildRequires: python3-module-tox
BuildRequires: python3-module-coverage
BuildRequires: python3-module-cryptography
%endif

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
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%check
export PIP_INDEX_URL=http://host.invalid./
tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
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
%python_sitelibdir/%mname-%version-py*.egg-info

%files -n python3-module-%mname
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py*.egg-info

%changelog
* Fri Dec 07 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.2 -> 0.5.0

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2
- Updated build dependencies.

* Tue Oct 24 2017 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- New 0.4.2 version

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Initial build.

