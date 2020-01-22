Name: python3-module-openzwave
Version: 0.4.19
Release: alt1

Summary: Python wrapper for openzwave library
License: BSD
Group: Development/Python
Url: https://pypi.org/project/python-openzwave/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ libopenzwave-devel
BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: python3-module-Cython python3-module-pip

%description
%summary

%prep
%setup

%install
python3 setup.py install --root=%buildroot --flavor shared

%files
%doc LICENSE.* README.*
%python3_sitelibdir/libopenzwave.cpython-*.so
%python3_sitelibdir/openzwave
%python3_sitelibdir/pyozwman
%python3_sitelibdir/python_openzwave
%python3_sitelibdir/python_openzwave-%version-*-info

%changelog
* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.19-alt1
- initial
