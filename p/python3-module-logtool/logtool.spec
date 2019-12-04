%define oname logtool

%define ver1 0
%define ver2 2
%define ver3 11

Name: python3-module-%oname
Version: %ver1.%ver2.%ver3
Release: alt2

Summary: Methods and tools that assist logging
License: GPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/logtool/
BuildArch: noarch

# https://github.com/clearclaw/logtool.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wrapt
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires wrapt


%description
Methods and tools that assist logging.

%prep
%setup

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

sed -i 's|@VERSION@|%version|' %oname/__init__.py
sed -i 's|@V1@|%ver1|' %oname/__init__.py
sed -i 's|@V2@|%ver2|' %oname/__init__.py
sed -i 's|@V3@|%ver3|' %oname/__init__.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.11-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1.git20150224.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.11-alt1.git20150224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11-alt1.git20150224
- Version 0.2.11

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20141124
- Initial build for Sisyphus

