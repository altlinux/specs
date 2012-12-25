%define _name python-elementary

Name: python-module-elementary
Version: 1.7.0
Release: alt1

Summary: Python bindings for Elementary library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module elementary

BuildPreReq: libelementary-devel >= 1.7.0
BuildRequires: rpm-build-python python-module-Cython
BuildRequires: python-module-evas-devel python-module-ecore-devel
# for check
BuildRequires: python-modules-unittest

%description
Elementary bindings for use with Python programms.

%package devel
Summary: Python bindings for Elementary library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%add_python_req_skip test_bubble
%add_python_req_skip test_cursor

%package examples
Summary: Python bindings for Elementary library (examples)
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package provides demo scripts using %_name.


%prep
%setup -n %_name-%version

>include/elementary/__init__.py

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%python_sitelibdir/elementary/
%doc AUTHORS README NEWS

%files devel
%_pkgconfigdir/%_name.pc
%dir %_datadir/%_name

%files examples
%_datadir/%_name/examples/

%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

