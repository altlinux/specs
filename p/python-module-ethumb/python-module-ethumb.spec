%define _name python-ethumb

Name: python-module-ethumb
Version: 1.7.0
Release: alt1

Summary: Python bindings for Ethumb library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module ethumb

BuildPreReq: libethumb-devel >= 1.7.0 libedbus-devel
BuildRequires: rpm-build-python python-module-Cython
BuildRequires: python-module-evas-devel python-module-ecore-devel
# for check
BuildRequires: python-modules-unittest

%description
Ethumb bindings for use with Python programms.

%package devel
Summary: Python bindings for Ethumb library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%package examples
Summary: Python bindings for Ethumb library (examples)
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
%python_sitelibdir/ethumb/
%doc AUTHORS README NEWS

%files devel
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/python-ethumb_client.pc
%dir %_datadir/%_name

%files examples
%_datadir/%_name/examples/

%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

