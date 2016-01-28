%define oname iptools
%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.1

Summary: Utilities for manipulating IPv4 and IPv6 addresses

License: BSD
Group: Development/Python
Url: https://github.com/bd808/python-iptools/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/i/iptools/iptools-0.6.1.tar.gz
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
Utilities for manipulating IPv4 and IPv6 addresses including a class that
can be used to include CIDR network blocks in Django's INTERNAL_IPS setting.

%if_with python3
%package -n python3-module-%oname
Summary: Utilities for manipulating IPv4 and IPv6 addresses
Group: Development/Python3

%description -n python3-module-%oname
Utilities for manipulating IPv4 and IPv6 addresses including a class that
can be used to include CIDR network blocks in Django's INTERNAL_IPS setting.
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
%doc AUTHORS CHANGES LICENSE
%python_sitelibdir/%oname/
%exclude %python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 10 2013 Vladimir Didenko <cow@altlinux.ru> 0.6.1-alt1
- initial build for Sisyphus
