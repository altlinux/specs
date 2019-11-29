%define oname mangoutils

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: A collection of commonly useful utilities
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/mangoutils/
BuildArch: noarch

# https://github.com/amol9/mangoutils.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python-tools-2to3

%py3_provides %oname
%py3_requires xml


%description
A collection of commonly useful utilities.

Submodules:

* web: utility classes for handling urls, list of well known cdns, top
  level domains
* html: utility class for parsing html and accessing elements via xpath
* system: platform related functions

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install
cp -fR %oname/system %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test
nosetests3 -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.git20150317.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150317.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150317
- Initial build for Sisyphus

