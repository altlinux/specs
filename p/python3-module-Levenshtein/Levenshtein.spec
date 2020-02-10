%define oname Levenshtein

Name: python3-module-%oname
Version: 0.11.2
Release: alt2

Summary: Python extension for computing string edit distances and similarities
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-Levenshtein/

# https://github.com/ztane/python-Levenshtein.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
The Levenshtein Python C extension module contains functions for fast
computation of

* Levenshtein (edit) distance, and edit operations
* string similarity
* approximate median strings, and generally string averaging
* string sequence and set similarity

It supports both normal and Unicode strings.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|python | python3 |' ./gendoc.sh
sed -i 's|file(modname|open(modname|' genextdoc.py

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
./gendoc.sh

%check
%__python3 setup.py test

%files
%doc *.txt NEWS* *.rst Levenshtein.html
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.11.2-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.2-alt1.git20140923.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1.git20140923.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.2-alt1.git20140923.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20140923
- Initial build for Sisyphus

