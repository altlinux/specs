%define _name python-efl

Name: python-module-efl
Version: 1.8.0
Release: alt2

Summary: Python bindings for EFL libraries
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.org/rel/bindings/python/%_name-%version.tar.gz
#Source: %_name-%version.tar

%setup_python_module ecore
%setup_python_module edbus
%setup_python_module edje
%setup_python_module elementary
%setup_python_module emotion
%setup_python_module ethumb
%setup_python_module evas

Obsoletes: python-module-ecore < 1.8.0
Provides: python-module-ecore = %version-%release
Obsoletes: python-module-eldbus < 1.8.0
Provides: python-module-eldbus = %version-%release
Obsoletes: python-module-edje < 1.8.0
Provides: python-module-edje = %version-%release
Obsoletes: python-module-elementary < 1.8.0
Provides: python-module-elementary = %version-%release
Obsoletes: python-module-emotion < 1.8.0
Provides: python-module-emotion = %version-%release
Obsoletes: python-module-ethumb < 1.8.0
Provides: python-module-ethumb = %version-%release
Obsoletes: python-module-evas < 1.8.0
Provides: python-module-evas = %version-%release

BuildPreReq: efl-libs-devel >= 1.8.0 libelementary-devel >= 1.8.0
BuildRequires: python-module-Cython python-module-dbus-devel
BuildRequires: rpm-build-python3 python3-devel
# for check
BuildRequires: python-modules-unittest

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

This package provides Enlightenment Foundation Libraries bindings for use
with Python programms.

%package -n python3-module-efl
Summary: Python3 bindings for EFL libraries
Group: Development/Python3

%description -n python3-module-efl
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

This package provides Enlightenment Foundation Libraries bindings for use
with Python3 programms.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build
pushd py3build
%python3_build
popd

%install
%python_install
pushd py3build
%python3_install
popd

%files
%python_sitelibdir/e_dbus/
%python_sitelibdir/ecore/
%python_sitelibdir/edje/
%python_sitelibdir/efl/
%python_sitelibdir/elementary/
%python_sitelibdir/emotion/
%python_sitelibdir/evas/
%python_sitelibdir/python_efl-*.egg-info
%doc AUTHORS README

%files -n python3-module-efl
%python3_sitelibdir/e_dbus/
%python3_sitelibdir/ecore/
%python3_sitelibdir/edje/
%python3_sitelibdir/efl/
%python3_sitelibdir/elementary/
%python3_sitelibdir/emotion/
%python3_sitelibdir/evas/
%python3_sitelibdir/python_efl-*.egg-info
%doc AUTHORS README

%changelog
* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt2
- updated buildreqs

* Mon Dec 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for sisyphus

