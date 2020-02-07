%define oname taskforce

Name: python3-module-%oname
Version: 0.1.14
Release: alt2

Summary: Starts and restarts daemon processes
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/taskforce/

BuildArch: noarch

# https://github.com/akfullfo/taskforce.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml python-tools-2to3

%py3_provides %oname
%py3_requires yaml


%description
Taskforce starts and restarts daemon processes. It will detect
executable and/or module changes and automatically restart the affected
processes. Initially this supports python 2.7 on Unix derivatives.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    bin/%oname

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README* examples
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.14-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.14-alt1.git20141129.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.14-alt1.git20141129.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.14-alt1.git20141129
- Version 0.1.14

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1.git20141120
- Version 0.1.12

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt1.git20141112
- Version 0.1.11

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1.git20141112
- Initial build for Sisyphus

