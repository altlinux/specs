%define _unpackaged_files_terminate_build 1

%define oname pytest-qt

Name: python3-module-%oname
Version: 4.0.2
Release: alt1
Summary: pytest plugin for Qt (PyQt4, PyQt5 and PySide) application testing
License: MIT
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-qt

BuildArch: noarch

# https://github.com/pytest-dev/pytest-qt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools_scm

%description
pytest-qt is a pytest plugin that allows programmers to write tests
for PyQt5, PyQt6, PySide2 and PySide6 applications.

The main usage is to use the qtbot fixture, responsible for handling
qApp creation as needed and provides methods to simulate user interaction,
like key presses and mouse clicks.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_install

%files
%doc LICENSE
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/pytestqt
%python3_sitelibdir/pytest_qt-%version-py*.egg-info

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt1
- Initial build for ALT.
