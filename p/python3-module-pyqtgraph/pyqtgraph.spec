%define modulename pyqtgraph

%ifarch %arm
%def_disable check
%endif

Name: python3-module-%modulename
Version: 0.12.4
Release: alt1.1

Summary: Scientific Graphics and GUI Library for Python
License: MIT
Group: Development/Python3

Url: http://http://www.pyqtgraph.org

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-devel

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-numpy
BuildRequires: python3-module-OpenGL

%if_disabled check
%else
BuildRequires: python3-module-pytest python3-module-six
BuildRequires: python3-module-six
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-h5py
BuildRequires: python3-module-scipy
BuildRequires: python3-module-matplotlib-qt5
BuildRequires: xvfb-run
BuildRequires: python3-module-pytest-xvfb
BuildRequires: mesa-dri-drivers
%endif

# skip optional dependencies
%add_python3_req_skip jupyter_rfb
%add_python3_req_skip PyQt6
%add_python3_req_skip PySide2 PySide2.QtCore PySide2.QtGui PySide2.QtWidgets
%add_python3_req_skip PySide6.QtCore PySide6.QtGui PySide6.QtWidgets

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%modulename/canvas

%description
PyQtGraph is a pure-python graphics and GUI library built on PyQt5 / PySide2
and numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

rm -r %buildroot/%python3_sitelibdir/pyqtgraph/examples

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v -k "not (test_reload) and not (test_PolyLineROI)"

%files
%doc CHANGELOG README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.12.4-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Mar 07 2022 Anton Midyukov <antohami@altlinux.org> 0.12.4-alt1
- 0.12.4

* Thu Feb 03 2022 Anton Midyukov <antohami@altlinux.org> 0.12.3-alt1
- 0.12.3

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt3.rc0
- NMU: don't pack tests

* Sun Jan 26 2020 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt2.rc0
- skip optional dependencies (PyQt4, PySide)

* Thu Dec 26 2019 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1.rc0
- 0.11.0 release candidate 0
