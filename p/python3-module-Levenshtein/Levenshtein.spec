%define oname Levenshtein

Name: python3-module-%oname
Version: 0.12.0
Release: alt1

Summary: Python extension for computing string edit distances and similarities
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-Levenshtein/

# https://github.com/ztane/python-Levenshtein.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

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

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc NEWS* *.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 21 2020 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Build new version for python3.8.

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

