%define _unpackaged_files_terminate_build 1

%define mname nss
Name: python-module-%mname
Version: 1.0.1
Release: alt2%ubt
Summary: Python binding for NSS (Network Security Services) and NSPR (Netscape Portable Runtime)
License: MPLv2.0 or GPLv2+ or LGPLv2+
Group: Development/Python
Url: http://www.mozilla.org/projects/security/pki/python-nss

# hg clone https://hg.mozilla.org/projects/python-nss
Source: %name-%version.tar

%py_provides %mname
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: python-devel
BuildRequires: python3-devel
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
BuildRequires: python-module-six
BuildRequires: python3-module-six
# for tests
BuildRequires: nss-utils
#

%description
python-nss is a Python binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an alternative
to OpenSSL and used extensively by major software projects. NSS is
FIPS-140 certified.

NSS is built upon NSPR because NSPR provides an abstraction of common
operating system services, particularly in the areas of networking and
process management. Python also provides an abstraction of common
operating system services but because NSS and NSPR are tightly bound
python-nss exposes elements of NSPR.

%package -n python3-module-%mname
Summary: Python3 binding for NSS (Network Security Services) and NSPR (Netscape Portable Runtime)
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
python-nss is a Python3 binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an alternative
to OpenSSL and used extensively by major software projects. NSS is
FIPS-140 certified.

NSS is built upon NSPR because NSPR provides an abstraction of common
operating system services, particularly in the areas of networking and
process management. Python also provides an abstraction of common
operating system services but because NSS and NSPR are tightly bound
python-nss exposes elements of NSPR.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python test/run_tests -i
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ../python3
python3 test/run_tests -i
popd

%files
%doc LICENSE* README doc/ChangeLog
%python_sitelibdir/*

%files -n python3-module-%mname
%doc LICENSE* README doc/ChangeLog
%python3_sitelibdir/*

%changelog
* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2%ubt
- Updated build dependencies.

* Thu Dec 28 2017 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1%ubt
- 1.0.0 -> 1.0.1

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.0-alt1
- Version 0.17.0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0 (ALT #30401)

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1
- Version 0.14.1

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Mon Sep 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

