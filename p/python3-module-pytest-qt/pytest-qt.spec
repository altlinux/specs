%define _unpackaged_files_terminate_build 1

%define oname pytest-qt
%def_with check

Name: python3-module-%oname
Version: 4.2.0
Release: alt1
Summary: pytest plugin for Qt (PyQt4, PyQt5 and PySide) application testing
License: MIT
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-qt
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-PyQt5
%endif

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
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

# config with enabled debug logging for QT applications is needed for pyqt5 logging tests
MY_CONFIG_DIR=$PWD/temp/config/dir
mkdir -p $MY_CONFIG_DIR/QtProject
cat > $MY_CONFIG_DIR/QtProject/qtlogging.ini << __EOF__
[Rules]
*.debug=true
__EOF__
export XDG_CONFIG_DIRS="$MY_CONFIG_DIR:$XDG_CONFIG_DIRS"
export TOX_TESTENV_PASSENV="XDG_CONFIG_DIRS"

%tox_check_pyproject -e pyqt5

%files
%doc LICENSE
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/pytestqt
%python3_sitelibdir/pytest_qt-%version.dist-info

%changelog
* Wed Dec 07 2022 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- 4.0.2 -> 4.2.0
- enabled tests

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt1
- Initial build for ALT.
