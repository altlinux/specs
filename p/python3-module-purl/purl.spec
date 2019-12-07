%define oname purl

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: An immutable URL class for easy URL-building and manipulation
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/purl/
BuildArch: noarch

# https://github.com/codeinthehole/purl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-nose
BuildRequires: python3-module-pip python3-module-wheel
BuildRequires: python3-module-tox

%py3_provides %oname


%description
A simple, immutable URL class with a clean API for interrogation and
manipulation. Supports Python 2.6, 2.7, 3.3, 3.4 and pypy.

Also supports template URLs as per RFC 6570.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20141212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141212
- Initial build for Sisyphus

