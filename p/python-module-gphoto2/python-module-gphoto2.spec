%define modname gphoto2
%def_disable python2

Name: python-module-%modname
Version: 2.1.0
Release: alt1

Summary: Python bindings to GPhoto libraries
Group: Development/Python
License: GPL-3.0
Url: http://pypi.python.org/pypi/%modname

Source: http://pypi.io/packages/source/g/%modname/%modname-%version.tar.gz

%define gphoto_ver 2.5
BuildRequires: libgphoto2-devel >= %gphoto_ver swig
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools python-devel
%endif

%description
python-gphoto2 is a comprehensive Python interface (or binding) to
libgphoto2_. It is built using SWIG_ to automatically generate the
interface code. This gives direct access to nearly all the libgphoto2_
functions, but sometimes in a rather un-Pythonic manner.

%package -n python3-module-%modname
Summary: Python3 bindings to GPhoto libraries
Group: Development/Python3

%description -n python3-module-%modname
python-gphoto2 is a comprehensive Python interface (or binding) to
libgphoto2_. It is built using SWIG_ to automatically generate the
interface code. This gives direct access to nearly all the libgphoto2_
functions, but sometimes in a rather un-Pythonic manner.

%prep
%setup -n %modname-%version %{?_enable_python2:-a0
cp -a %modname-%version py2build}

%build
%python3_build

%{?_enable_python2:
pushd py2build
%python_build
popd}

%install
%python3_install

%{?_enable_python2:
pushd py2build
%python_install
popd}

%if_enabled python2
%files
%python_sitelibdir/%modname/
%doc README.rst
%python_sitelibdir/*.egg-info
%endif

%files -n python3-module-%modname
%python3_sitelibdir/%modname/
%doc README.rst
%python3_sitelibdir/*.egg-info

# examples
%exclude %_datadir/python-%modname


%changelog
* Thu Feb 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0
- disabled python2 build

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Dec 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Sun Nov 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Nov 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for Sisyphus


