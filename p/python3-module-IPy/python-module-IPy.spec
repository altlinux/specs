%define mname IPy
Name: python3-module-%mname
Version: 0.76
Release: alt1.git20130319.1.1
Summary: Python module for handling IPv4 and IPv6 Addresses and Networks
URL: https://github.com/haypo/python-ipy
# https://github.com/haypo/python-ipy.git
Source: %mname-%version.tar
License: BSD
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base
BuildRequires: rpm-build-python3

#BuildRequires: python3-devel python-tools-2to3

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks in
a fashion similar to perl's Net::IP and friends. The IP class allows
a comfortable parsing and handling for most notations in use for IPv4 and IPv6
Addresses and Networks.

%prep
%setup -n %mname-%version

%build
%python3_build

%install
%python3_install --compile

%files
%doc AUTHORS ChangeLog README
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.76-alt1.git20130319.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.76-alt1.git20130319.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.76-alt1.git20130319
- Initial build for Sisyphus

