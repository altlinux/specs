%define oname hjson

Name: python3-module-%oname
Version: 1.4.1
Release: alt2

Summary: JSON for Humans, allows comments and is less error prone
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/hjson/

BuildArch: noarch

# https://github.com/laktak/hjson-py.git
Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest


%description
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

%package tests
Summary: tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install
cp -fR %oname/tests/assets %buildroot%python3_sitelibdir/%oname/tests/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests


%changelog
* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.1-alt2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4.1-alt1.git20150116.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.1-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20150116
- Initial build for Sisyphus

