%define _unpackaged_files_terminate_build 1

%define oname qtpy

Name: python3-module-%oname
Version: 1.7.0
Release: alt1
Summary: Provides an uniform layer to support PyQt5, PySide2, PyQt4 and PySide with a single codebase
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/QtPy/

BuildArch: noarch

# https://github.com/spyder-ide/qtpy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
QtPy is a small abstraction layer that lets you write applications
using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4, PySide2 and PySide
using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PySide2
but import Qt modules from qtpy instead of PySide2 (or PyQt5)

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
%python3_build_debug

%install
%python3_install

%files
%doc LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Apr 10 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt1
- Initial build for ALT.
