%define modulename ipaddr

%def_with python3

Name: python-module-%modulename
Version: 2.1.10
Release: alt2.1

Summary: Library for working with IP addressess, both IPv4 and IPv6
License: Apache License, Version 2.0
Group: Development/Python
Url: https://github.com/google/ipaddr-py
Packager: Liudmila Butorina <lbutorina@altlinux.org>

BuildArch: noarch

Source0: %modulename-%version.tar

#BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-modules-unittest python-tools-2to3 rpm-build-python3 time

%description
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%package -n python3-module-%modulename
Summary: Library for working with IP addressess, both IPv4 and IPv6
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%check
./test-2to3.sh

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc README

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
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

