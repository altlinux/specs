%def_with python3

#add_findreq_skiplist %python_sitelibdir/pyudev/*

Name: python-module-pyudev
Version: 0.16.1
Release: alt1
%setup_python_module pyudev

Group: System/Libraries
Summary: Udev bindings for Python
Url: http://packages.python.org/pyudev/
License: LGPLv2.1+

BuildArch: noarch

Source: pyudev-%version.tar

BuildRequires: libudev-devel python-devel python-module-distribute

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:      python3-devel
BuildRequires:      python3-module-distribute
%endif

%description
A Python binding to libudev, the hardware management library and service
found in modern linux systems.

%if_with python3
%package -n python3-module-pyudev
Summary:            Udev bindings for Python
Group:              Development/Python3

%description -n python3-module-pyudev
A Python3 binding to libudev, the hardware management library and
service found in modern linux systems.
%endif

%prep
%setup -q -n pyudev-%version

%build
%python_build

%if_with python3
%python3_build
%endif

%install
%if_with python3
%python3_install
%endif

%python_install

%files
%doc CHANGES.rst COPYING README.rst
%python_sitelibdir/pyudev
%python_sitelibdir/pyudev-*

%if_with python3
%files -n python3-module-pyudev
%doc CHANGES.rst COPYING README.rst
%python3_sitelibdir/pyudev
%python3_sitelibdir/pyudev-*
%endif



%changelog
* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version
- Package with Python3 too

* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.14-alt1
- initial build
