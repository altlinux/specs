%define _unpackaged_files_terminate_build 1
%define oname ipyroute

%def_disable check

Name: python3-module-%oname
Version: 0.0.36
Release: alt3

Summary: Yet another interface for iproute2
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ipyroute/
# https://github.com/jta/ipyroute.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/3c/cf/98fd398c0a1393700514fd1f90e825444ae5c2787d4f92e4b1814bf44b12/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

Requires: iproute2
%py3_requires sh netaddr six

BuildRequires: python3-module-netaddr
BuildRequires: python3-module-pytest python3-module-sh


%description
Yet another interface for iproute2.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.36-alt3
- Fixed BuildRequires.

* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.36-alt2
- disable python2

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.36-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.23-alt1.git20150214.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.23-alt1.git20150214.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt1.git20150214
- Version 0.0.23

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt1.git20150211
- Version 0.0.18

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150210
- Version 0.0.16

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.13-alt1.git20150202
- Initial build for Sisyphus

