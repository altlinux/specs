%define oname service_identity
%define package_name service-identity
%def_with python3

Name: python-module-%package_name
Version: 14.0.0
Release: alt1.1

Summary: Service identity verification for pyOpenSSL

License: MIT
Group: Development/Python
Url: https://github.com/pyca/service_identity

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/s/service_identity/service_identity-1.0.0.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

#BuildPreReq: rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
Use this package if you use pyOpenSSL and don't want to be MITMed.
service_identity aspires to give you all the tools you need for verifying whether
a certificate is valid for the intended purposes. In the simplest case, this means host
name verification. However, service_identity implements RFC 6125 fully and plans to add
other relevant RFCs too.

%if_with python3
%package -n python3-module-%package_name
Summary: Service identity verification for pyOpenSSL (Python3)
Group: Development/Python3

%description -n python3-module-%package_name
Use this package if you use pyOpenSSL and don't want to be MITMed.
service_identity aspires to give you all the tools you need for verifying whether
a certificate is valid for the intended purposes. In the simplest case, this means host
name verification. However, service_identity implements RFC 6125 fully and plans to add
other relevant RFCs too.
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
%doc AUTHORS.rst LICENSE README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%package_name
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 14.0.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.org> 14.0.0-alt1
- new version

* Thu Jul 31 2014 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
