%define _unpackaged_files_terminate_build 1

%define oname qtpy

%def_with check

Name: python3-module-%oname
Version: 2.4.0
Release: alt1
Summary: Provides an uniform layer to support PyQt5, PySide2, PyQt6, PySide6 with a single codebase
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/QtPy/
Vcs: https://github.com/spyder-ide/qtpy.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: xvfb-run
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-qt
BuildRequires: python3-module-PyQt5
%endif

%description
QtPy is a small abstraction layer that lets you write applications using
a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt6, PySide6, PySide2 using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PyQt or PySide directly,
but import Qt modules from qtpy instead of PyQt5, PySide2, PyQt6 or PySide6.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
QtPy is a small abstraction layer that lets you write applications
using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4, PySide2 and PySide
using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PySide2
but import Qt modules from qtpy instead of PySide2 (or PyQt5)

This package contains tests for %oname.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i 's/--cov=qtpy --cov-report=term-missing//' pytest.ini
sed -i 's/--color=yes//' pytest.ini
%pyproject_run -- xvfb-run pytest qtpy -k 'not test_qttexttospeech'

%files
%doc LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md
%_bindir/%oname
%python3_sitelibdir/QtPy-%version.dist-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Aug 30 2023 Anton Vyatkin <toni@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Tue Jul 11 2023 Anton Vyatkin <toni@altlinux.org> 2.3.1-alt1
- New version 2.3.1.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.0-alt1
- Updated to upstream version 1.10.0.

* Tue Aug 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt1
- Updated to upstream version 1.9.0.
- Enabled tests.

* Wed Apr 10 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt1
- Initial build for ALT.
