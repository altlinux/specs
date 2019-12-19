%define oname ezfacebook

Name: python3-module-%oname
Version: 0.87.0
Release: alt3

Summary: Django Tools to use facebook seamlessly without having to build around it
License: ASL
Group: Development/Python3
Url: https://pypi.python.org/pypi/ezfacebook/
BuildArch: noarch

# https://github.com/explodes/ezfacebook.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

This package makes facebook integration easy for all kinds of web sites:

* Web Applications
* Facebook Page Tabs
* Facebook Applications

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The purpose of this package is to make facebook integration easy WITHOUT
having to make your whole app depend on this package.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.87.0-alt3
- build for python2 disabled

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.87.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.87.0-alt1.git20140107.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87.0-alt1.git20140107
- Initial build for Sisyphus

