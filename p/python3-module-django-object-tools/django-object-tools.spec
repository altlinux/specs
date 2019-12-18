%define _unpackaged_files_terminate_build 1
%define oname django-object-tools

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Django app enabling painless creation of additional admin object tools
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-object-tools/
BuildArch: noarch

# https://github.com/praekelt/django-object-tools.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Django app enabling painless creation of additional admin object tools.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django app enabling painless creation of additional admin object tools.

This package contains tests for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1
- Update version to 2.0.0
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20140916.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140916
- Initial build for Sisyphus

