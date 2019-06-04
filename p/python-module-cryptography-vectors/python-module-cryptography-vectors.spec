%define oname cryptography_vectors
%def_with python3

Name: python-module-cryptography-vectors
Version: 2.7
Release: alt1

Summary: Test vectors for the cryptography package

License: %asl
Group: Development/Python
Url: https://pypi.python.org/pypi/cryptography-vectors/

# Source-url: https://pypi.python.org/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python rpm-build-licenses
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-setuptools
%endif

%setup_python_module %oname

%description
Test vectors for the cryptography package.

%if_with python3
%package -n python3-module-cryptography-vectors
Summary: Test vectors for the cryptography package (Python 3)
Group: Development/Python3

%description -n python3-module-cryptography-vectors
Test vectors for the cryptography package.
%endif


%prep
%setup

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
%doc LICENSE
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-cryptography-vectors
%doc LICENSE
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7-alt1
- initial build for ALT Sisyphus
