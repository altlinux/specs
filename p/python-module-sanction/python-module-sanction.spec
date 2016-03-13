%define oname sanction
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.1.1

Summary: A simple, lightweight OAuth2 client

License: MIT
Group: Development/Python
Url: http://code.google.com/p/psutil/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/s/sanction/sanction-0.4.tar.gz
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
Sanction is a ridiculously easy to use OAuth 2.0 client intended for rapid
development against OAuth 2.0 providers with minimal keyboard bashing. 

%if_with python3
%package -n python3-module-%oname
Summary: A simple, lightweight OAuth2 client (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Sanction is a ridiculously easy to use OAuth 2.0 client intended for rapid
development against OAuth 2.0 providers with minimal keyboard bashing. 
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
%doc README LICENSE
%python_sitelibdir/%oname/
%exclude %python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/*.egg-*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.ru> 0.4.0-alt1
- initial build for Sisyphus
