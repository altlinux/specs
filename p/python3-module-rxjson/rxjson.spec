%define oname rxjson

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: JSON RX Schema validation tool
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/rxjson/
BuildArch: noarch

# https://github.com/spiral-project/rxjson.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-d2to1 python3-module-TAP
BuildRequires: python3-module-nose

%py3_provides %oname


%description
rxjson is a python package that helps you validate your generated JSON
against a standardized json schema directly in your python app.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
pushd tests
nosetests3
popd

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.dev.git20130212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.dev.git20130212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20130212
- Initial build for Sisyphus

