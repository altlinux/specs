%define _name cpopen
%define py_vers_nodot %{python_version_nodots python3}

Name: python3-module-%_name
Version: 1.5
Release: alt2

Summary: A C reimplementation of the tricky bits of Python's Popen
Group: Development/Python3
License: GPLv2+
Url: http://pypi.python.org/pypi/%_name

Source: http://bronhaim.fedorapeople.org/%_name-%version.tar.gz
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel


%description
Python package for creating sub-process in simpler and safer manner by
using C code.

%prep
%setup -n %_name-%version
%patch0 -p2

%build
export CPOPEN_VERSION=%version
%python3_build_debug

%install
export CPOPEN_VERSION=%version
%__python3 setup.py install --root %buildroot

%files
%doc AUTHORS README PKG-INFO
%python3_sitelibdir/%_name/*.py
%python3_sitelibdir/%_name/%_name.cpython-%{py_vers_nodot}.so
%python3_sitelibdir/%_name/__pycache__/
%python3_sitelibdir/%_name-%version-py*.egg-info


%changelog
* Thu Mar 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt2
- Porting to python3.

* Wed Jul 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- first build for Sisyphus

