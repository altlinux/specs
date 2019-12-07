%define _unpackaged_files_terminate_build 1
%define oname wsrpc-tornado

Name: python3-module-%oname
Version: 0.5.5
Release: alt2

Summary: WSRPC is WebSocket Remote procedure call for tornado and javascript
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/wsrpc-tornado/
BuildArch: noarch

# https://github.com/mosquito/wsrpc.git
Source0: https://pypi.python.org/packages/c1/f0/4d263a27570697c05a9b0a89256e5d63dec55a8ed24519a3c9ae5e600886/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pycares python3-module-pytest
BuildRequires: python-tools-2to3 python3-module-zope

%py3_provides wsrpc
%py3_requires tornado


%description
Remote Procedure call through WebSocket between browser and tornado.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install
cp -fR wsrpc/static %buildroot%python3_sitelibdir/wsrpc/

%files
%doc *.rst PKG-INFO
%python3_sitelibdir/*


%changelog
* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.5-alt2
- build for python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20150119.1
- NMU: Use buildreq for BR.

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150119
- Initial build for Sisyphus

