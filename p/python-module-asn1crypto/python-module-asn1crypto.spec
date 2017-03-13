%define oname asn1crypto
%def_with python3

Name: python-module-%oname
Version: 0.21.1
Release: alt1

Summary: Python ASN.1 parser

License: %mit
Group: Development/Python
Url: https://pypi.python.org/pypi/asn1crypto
Packager: Vladimir Didenko <cow@altlinux.org>
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python python-module-setuptools
%if_with python3
BuildPreReq: rpm-build-python3 python3-module-setuptools
%endif

%setup_python_module %oname

%description
Fast ASN.1 parser and serializer with definitions for private keys, public keys,
certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509
and TSP.


%if_with python3
%package -n python3-module-%oname
Summary: Python ASN.1 parser
Group: Development/Python3

%description -n python3-module-%oname
Fast ASN.1 parser and serializer with definitions for private keys, public keys,
certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509
and TSP.
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
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Mon Mar 13 2017 Vladimir Didenko <cow@altlinux.ru> 0.21.1-alt1
- Initial build for Sisyphus
