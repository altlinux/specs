%define oname numpy-stl

Name: python3-module-%oname
Version: 3.1.2
Release: alt1

Summary: Library to make reading, writing and modifying both binary and ascii STL files easy

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/numpy-stl
VCS: https://github.com/WoLpH/numpy-stl

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-python_utils
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-docutils
BuildRequires: python3-module-sphinx
BuildRequires: xvfb-run

%py3_provides stl

%description
Simple library to make working with STL files (and 3D objects in
general) fast and easy.

Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%make -C docs html

%check
sed -i '/--flake8/d' pytest.ini
%pyproject_run_pytest

%files
%doc *.rst docs/_build/html
%_bindir/*
%python3_sitelibdir/stl
%python3_sitelibdir/*.dist-info

%changelog
* Sun Aug 18 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt1
- Automatically updated to 3.1.2.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Fixed FTBFS.

* Thu Mar 16 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Sun Oct 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.17.1-alt1
- Automatically updated to 2.17.1.

* Fri Jan 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.10.1-alt1
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.6-alt2.git20141210.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.6-alt2.git20141210
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20141210
- Version 1.3.6

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.git20141127
- Version 1.3.5

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141104
- Version 1.3.4

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.git20141024
- Initial build for Sisyphus

