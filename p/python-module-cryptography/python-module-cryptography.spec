%define oname cryptography
%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1

Summary: Cryptographic recipes and primitives to Python developers.

License: %asl
Group: Development/Python
Url: https://pypi.python.org/pypi/cryptography/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/c/cryptography/cryptography-0.5.2.tar.gz
Source: %oname-%version.tar

BuildPreReq: rpm-build-python rpm-build-licenses
BuildRequires: python-devel python-module-distribute python-module-setuptools-tests
BuildRequires: python-module-six python-module-cffi python-module-pycparser
BuildRequires: libssl-devel
BuildRequires: python-module-pyasn1
BuildRequires: python-module-enum34
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-setuptools-tests
BuildRequires: python3-module-six python3-module-cffi python3-module-pycparser
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-enum34
%endif

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
%endif

%files
%doc AUTHORS.rst  CHANGELOG.rst  CONTRIBUTING.rst  README.rst
%python_sitelibdir/%oname/
%exclude %python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/*.egg-*
%endif

%changelog
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
