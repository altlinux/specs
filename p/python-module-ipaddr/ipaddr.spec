%define modname ipaddr

Name: python-module-%modname
Version: 2.2.0
Release: alt1

Summary: Library for working with IP addressess, both IPv4 and IPv6
License: Apache-2.0
Group: Development/Python

Url: https://github.com/google/ipaddr-py
Packager: Liudmila Butorina <lbutorina@altlinux.org>
BuildArch: noarch

Source: ipaddr-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-devel python-tools-2to3
BuildRequires: python-modules-unittest
BuildRequires: time

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools
BuildPreReq: python-tools-2to3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base


%description
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%package -n python3-module-%modname
Summary: Library for working with IP addressess, both IPv4 and IPv6
Group: Development/Python3
%py3_provides %modname

%description -n python3-module-%modname
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%prep
%setup -n ipaddr-%version

cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python_build

pushd ../python3
%python3_build
popd

%check
./ipaddr_test.py

%install
%python_install --record=INSTALLED_FILES

pushd ../python3
%python3_install
popd

%files -f INSTALLED_FILES
%doc README COPYING wiki/*

%files -n python3-module-%modname
%doc README COPYING wiki/*
%python3_sitelibdir/*


%changelog
* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.10-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.10-alt2.1
- NMU: Use buildreq for BR.

* Thu Aug  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.10-alt2
- Update sources to current trunk (git commit c813f47)

* Thu Aug  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.10-alt1
- 2.1.10
- Update URL
- %%check section added

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.7-alt1.1
- Added module for Python 3

* Mon Jan 30 2012 Liudmila Butorina <lbutorina@altlinux.org> 2.1.7-alt1
- Initial build
