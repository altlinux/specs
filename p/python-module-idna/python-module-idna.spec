%define oname idna
%def_with python3

Name: python-module-%oname
Version: 2.2
Release: alt1

Summary: A library to support the Internationalised Domain Names in Applications (IDNA)

License: BSD
Group: Development/Python
Url: https://github.com/kjd/idna

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
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This version of the protocol is often referred
to as "IDNA2008" and can produce different results from the earlier standard from 2003.

%if_with python3
%package -n python3-module-%oname
Summary: Utilities for manipulating IPv4 and IPv6 addresses
Group: Development/Python3

%description -n python3-module-%oname
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This version of the protocol is often referred
to as "IDNA2008" and can produce different results from the earlier standard from 2003.
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
%doc HISTORY.rst LICENSE.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Feb 2 2017 Vladimir Didenko <cow@altlinux.org> 2.2-alt1
- New version

* Fri Jul 22 2016 Vladimir Didenko <cow@altlinux.org> 2.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Jun 7 2015 Vladimir Didenko <cow@altlinux.ru> 2.0-alt1
- initial build for Sisyphus
