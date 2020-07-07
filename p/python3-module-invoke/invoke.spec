%define _unpackaged_files_terminate_build 1
%define oname invoke

Name: python3-module-%oname
Version: 1.4.1
Release: alt1

Summary: Simple Python task execution
License: BSD-2-Clause
Group: Development/Python3
Url: https://www.pyinvoke.org/
# https://github.com/pyinvoke/invoke.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%py3_requires lexicon
%py3_requires six
%py3_requires yaml

%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%prep
%setup
%autopatch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

# remove some vendored stuff
rm -r invoke/vendor/yaml{2,3}
rm -r invoke/vendor/lexicon
rm invoke/vendor/six.py
rm invoke/vendor/decorator.py

find . -name '*.py' | xargs sed -i \
   -e 's|from invoke\.vendor\.six\(.*\) import |from six\1 import |g'

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 0.21.0 -> 1.4.1.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.21.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt1
- Updated to upstream version 0.21.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt2.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.1-alt2.git20150730
- cleanup buildreq

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150730
- Version 0.10.1

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20141113
- Initial build for Sisyphus

