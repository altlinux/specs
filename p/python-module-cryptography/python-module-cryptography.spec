%define oname cryptography
%def_with python3

Name: python-module-%oname
Version: 2.1.4
Release: alt1.1

Summary: Cryptographic recipes and primitives to Python developers.

License: %asl
Group: Development/Python
Url: https://pypi.python.org/pypi/cryptography/
Packager: Vladimir Didenko <cow@altlinux.org>
# Source-url: https://pypi.python.org/packages/source/c/cryptography/%oname-%version.tar.gz
Source: %oname-%version.tar

#BuildPreReq: rpm-build-python rpm-build-licenses
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: elfutils libcom_err-devel libkrb5-devel python-base python-devel python-module-pycparser python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: libssl-devel python-module-cffi python-module-enum34 python-module-pyasn1 python-module-setuptools python3-devel python3-module-cffi python3-module-enum34 python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute python-module-setuptools
#BuildRequires: python-module-six python-module-cffi python-module-pycparser
#BuildRequires: libssl-devel
#BuildRequires: python-module-pyasn1
#BuildRequires: python-module-enum34
#BuildRequires: python-module-ipaddress
#BuildRequires: python-module-idna
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute python3-module-setuptools
#BuildRequires: python3-module-six python3-module-cffi python3-module-pycparser
#BuildRequires: python3-module-pyasn1
#BuildRequires: python3-module-enum34
#BuildRequires: python3-module-idna
%endif

Requires: python-module-cffi

%setup_python_module %oname

%description
cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Our goal is for it to be your "cryptographic standard library". cryptography includes both high level
recipes, and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message
digests and key derivation functions.


%if_with python3
%package -n python3-module-%oname
Summary: Cryptographic recipes and primitives to Python developers (Python 3).
Group: Development/Python3
Requires: python3-module-cffi

%description -n python3-module-%oname
cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Our goal is for it to be your "cryptographic standard library". cryptography includes both high level
recipes, and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message
digests and key derivation functions.
%endif


%prep
%setup -n %oname-%version

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

%filter_from_requires /python3[(]cryptography.hazmat.bindings._commoncrypto[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._constant_time[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._openssl[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._padding[)]/d
%endif

%files
%doc AUTHORS.rst  CHANGELOG.rst  CONTRIBUTING.rst  README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Wed Oct 18 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Wed Jul 19 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Mon Mar 13 2017 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Nov 22 2016 Vladimir Didenko <cow@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Oct 18 2016 Vladimir Didenko <cow@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Aug 30 2016 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Jun 9 2016 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Mar 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 22 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Mar 21 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.3-alt1
- NMU: 1.2.1 -> 1.2.3 (fixes FTBFS).

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 10 2016 Vladimir Didenko <cow@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Oct 30 2015 Vladimir Didenko <cow@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Sep 27 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Sep 18 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt2
- Add cffi to requirements (closes: #31280)

* Mon Sep 7 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Aug 12 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sun Jun 7 2015 Vladimir Didenko <cow@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sat Apr 11 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added *.egg-info

* Tue Mar 10 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Fri Jan 16 2015 Vladimir Didenko <cow@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Dec 29 2014 Vladimir Didenko <cow@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Thu Dec 18 2014 Vladimir Didenko <cow@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Oct 16 2014 Vladimir Didenko <cow@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Oct 13 2014 Vladimir Didenko <cow@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Thu Aug 21 2014 Vladimir Didenko <cow@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Tue Jul 29 2014 Vladimir Didenko <cow@altlinux.ru> 0.5.2-alt1
- initial build for Sisyphus
