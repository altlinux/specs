%define oname kiwisolver
Name: python3-module-%oname
Version: 1.0.1
Release: alt2
Summary: A fast implementation of the Cassowary constraint solver
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kiwisolver/
# VCS: https://github.com/nucleic/kiwi
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/nucleic/kiwi.git
Source: kiwi-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools gcc-c++
BuildRequires: python3-dev

%description
Kiwi is an efficient C++ implementation of the Cassowary constraint
solving algorithm. Kiwi is an implementation of the algorithm based on
the seminal Cassowary paper. It is not a refactoring of the original C++
solver. Kiwi has been designed from the ground up to be lightweight and
fast. Kiwi ranges from 10x to 500x faster than the original Cassowary
solver with typical use cases gaining a 40x improvement. Memory savings
are consistently > 5x.

%prep
%setup -n kiwi-%version

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Thu Dec 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Add python3-dev to build requirements.

* Tue Nov 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.
- Package as python3 module.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.git20140712.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140712
- Initial build for Sisyphus

