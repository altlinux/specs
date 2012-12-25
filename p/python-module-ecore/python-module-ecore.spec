%define _name python-ecore

Name: python-module-ecore
Version: 1.7.0
Release: alt1

Summary: Python bindings for Ecore library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module ecore

BuildPreReq: libecore-devel >= 1.7.0
BuildRequires: rpm-build-python python-module-Cython python-module-evas-devel
# for check
BuildRequires: python-modules-unittest

%description
Ecore bindings for use with Python programms.

%package devel
Summary: Python bindings for Ecore library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%package examples
Summary: Python bindings for Ecore library (examples)
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package provides demo scripts using %_name.


%prep
%setup -n %_name-%version

# should be empty
>include/ecore/__init__.py
>include/ecore/win32/__init__.py
>include/ecore/imf/__init__.py
>include/ecore/evas/__init__.py
>include/ecore/x/__init__.py
>include/ecore/file/__init__.py

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%python_sitelibdir/ecore/
%doc AUTHORS README NEWS

%files devel
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/python-ecore-evas.pc
%_pkgconfigdir/python-ecore-file.pc
%_pkgconfigdir/python-ecore-imf.pc
%_pkgconfigdir/python-ecore-x.pc
%dir %_datadir/%_name

%files examples
%_datadir/%_name/examples/


%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

