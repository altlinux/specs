%define _unpackaged_files_terminate_build 1

%define mname nss

Name: python3-module-%mname
Version: 1.0.1
Release: alt7

Summary: Python binding for NSS (Network Security Services) and NSPR (Netscape Portable Runtime)
License: MPL-2.0 or GPL-2.0+ or LGPL-2.0+
Group: Development/Python3
Url: http://www.mozilla.org/projects/security/pki/python-nss

# hg clone https://hg.mozilla.org/projects/python-nss
Source: %name-%version.tar
Patch0: 0001-Rename-DSA-RSA-PublicKey-to-Py-DSA-RSA-PublicKey.patch
Patch1: 0002-Fix-python-names-of-RSAPublicKey-DSAPublicKey.patch
Patch2: no-stdarg-proto-check.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: python3-module-six
# for tests
BuildRequires: nss-utils

%py3_provides %mname


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

%prep
%setup
%autopatch -p2

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 test/run_tests -i

%files
%doc LICENSE* README doc/ChangeLog
%python3_sitelibdir/*


%changelog
* Thu Nov 23 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt7
- Fixed build with python3.12.

* Thu Dec 10 2020 Stanislav Levin <slev@altlinux.org> 1.0.1-alt6
- Applied upstream fixes.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt5
- Build for python2 disabled.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 05 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt3
- Rebuild for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2.S1
- Updated build dependencies.

* Thu Dec 28 2017 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.S1
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

