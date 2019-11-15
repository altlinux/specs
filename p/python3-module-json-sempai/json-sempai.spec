%define oname json-sempai

Name: python3-module-%oname
Version: 0.4.0
Release: alt2

Summary: Use JSON files as if they're python modules
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/json-sempai/
# https://github.com/kragniz/json-sempai.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides jsonsempai
%py3_requires json


%description
Use JSON files as if they're python modules.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Use JSON files as if they're python modules.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- python2 disable

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1.git20150119.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20150119.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20150119
- Initial build for Sisyphus

