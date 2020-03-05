%define oname pycrsltd

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Interface to CRS Ltd hardware (Bits++, ColorCal etc...).
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/%oname

BuildArch: noarch

Source: %oname-%version.tar.gz
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip psychopy


%description
PyCRSltd  is the central library for the python interface to CRS Ltd
hardware (Bits++, ColorCal etc...).

The library is very much under construction and should not be used yet
except by enthusiasts.

It is being written mostly by Jon Peirce, with support from CRS Ltd. If
you would like to contribute please get in touch!

%prep
%setup -n %oname-%version
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.txt
%python3_sitelibdir/*%{oname}*


%changelog
* Thu Mar 05 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- Porting to python3.

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build from scratch

