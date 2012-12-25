%define _name python-emotion

Name: python-module-emotion
Version: 1.7.0
Release: alt1

Summary: Python bindings for Emotion library
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.fr/releases/BINDINGS/python/%_name-%version.tar.bz2
#Source: %_name-%version.tar

%setup_python_module emotion

BuildPreReq: libemotion-devel >= 1.7.0
BuildRequires: rpm-build-python python-module-Cython
BuildRequires: python-module-evas-devel python-module-ecore-devel
# for check
BuildRequires: python-modules-unittest

%description
Emotion bindings for use with Python programms.

%package devel
Summary: Python bindings for Emotion library (development package)
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package provides development files for %_name.

%package examples
Summary: Python bindings for Emotion library (examples)
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package provides demo scripts using %_name.


%prep
%setup -n %_name-%version

>include/emotion/__init__.py

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%python_sitelibdir/emotion/
%doc AUTHORS README NEWS

%files devel
%_pkgconfigdir/%_name.pc
%dir %_datadir/%_name

%files examples
%_datadir/%_name/examples/

%changelog
* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for sisyphus

