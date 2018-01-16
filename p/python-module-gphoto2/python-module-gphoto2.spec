%define modname gphoto2

Name: python-module-%modname
Version: 1.8.2
Release: alt1

Summary: Python bindings to GPhoto libraries
Group: Development/Python
License: GPLv3
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/g/%modname/%modname-%version.tar.gz

BuildRequires: libgphoto2-devel swig

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

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
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

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
%python_sitelibdir/%modname/
%doc README.rst
%python_sitelibdir/*.egg-info

%files -n python3-module-%modname
%python3_sitelibdir/%modname/
%doc README.rst
%python3_sitelibdir/*.egg-info

# examples
%exclude %_datadir/python-%modname


%changelog
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


