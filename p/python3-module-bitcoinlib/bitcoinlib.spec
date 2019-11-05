%define _unpackaged_files_terminate_build 1
%define pname bitcoin
%define oname %{pname}lib

%def_disable check

Name: python3-module-%oname
Version: 0.7.0
Release: alt2

Summary: Provides an easy interface to the Bitcoin data structures and protocol
License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-bitcoinlib/
# https://github.com/petertodd/python-bitcoinlib.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/de/70/50a47e47f31fd76dcbf37f2b89b53ed1fc89898f7f0d422e1dbdfa5425d7/python-%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

Provides: python3-module-%pname = %EVR
%py3_provides %pname
%py3_requires json


%description
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

This package contains tests for %oname.

%prep
%setup -q -n python-%{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- disable python2

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20150110.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20150110.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150110
- Initial build for Sisyphus

