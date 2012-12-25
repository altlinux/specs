%define _name python-e_dbus

Name: python-module-edbus
Version: 1.7.0
Release: alt1

Summary: Python bindings for E_Dbus library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module e_dbus

BuildPreReq: libedbus-devel >= 1.7.0
BuildRequires: rpm-build-python python-module-Cython
BuildRequires: python-module-dbus-devel
# for check
BuildRequires: python-modules-unittest

%description
E_Dbus bindings for use with Python programms.

%package devel
Summary: Python bindings for E_Dbus library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%package examples
Summary: Python bindings for E_Dbus library (examples)
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package provides demo scripts using %_name.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%python_sitelibdir/e_dbus.so
%doc AUTHORS README NEWS

%exclude %python_sitelibdir/*.la

%files devel
%_pkgconfigdir/python-edbus.pc


%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

