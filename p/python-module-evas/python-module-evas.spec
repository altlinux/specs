%define _name python-evas

Name: python-module-evas
Version: 1.7.0
Release: alt1

Summary: Python bindings for Evas library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module evas

BuildPreReq: libevas-devel >= 1.7.0
BuildRequires: rpm-build-python python-module-Cython
# for check
BuildRequires: python-modules-unittest

%description
Evas bindings for use with Python programms.

%package devel
Summary: Python bindings for Evas library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%package examples
Summary: Python bindings for Evas library (examples)
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package provides demo scripts using %_name.


%prep
%setup -n %_name-%version

# should be empty
> include/evas/__init__.py

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%python_sitelibdir/evas/
%doc AUTHORS README NEWS

%files devel
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%dir %_datadir/%_name

%files examples
%_datadir/%_name/examples/

%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

