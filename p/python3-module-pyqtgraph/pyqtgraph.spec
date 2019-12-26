%define modulename pyqtgraph

# segfault python3 on i586 and ppc64le when running tests
%ifarch x86_64 aarch64
%def_with check
%else
%def_without check
%endif

Name: python3-module-%modulename
Version: 0.11.0
Release: alt1.rc0

Summary: Scientific Graphics and GUI Library for Python
License: MIT
Group: Development/Python3

Url: http://http://www.pyqtgraph.org

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-numpy
BuildRequires: python3-module-OpenGL
# For Tests
%if_with check
BuildRequires: python3-module-pytest python3-module-six python3-module-numpy-testing
BuildRequires: python3-module-six
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-h5py
BuildRequires: python3-module-scipy
BuildRequires: xvfb-run
%endif

%add_python3_req_skip PySide2

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

rm -r %buildroot/%python3_sitelibdir/pyqtgraph/examples

%check
PYTHONDONTWRITEBYTECODE=1 xvfb-run -a py.test3 -k "not (test_ImageItem or test_ImageItem_axisorder or test_PlotCurveItem or test_getArrayRegion or test_getArrayRegion_axisorder or test_PolyLineROI or test_exit_crash)"

%files
%doc CHANGELOG README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 26 2019 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1.rc0
- 0.11.0 release candidate 0
