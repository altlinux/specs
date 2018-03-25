%define modname evdev
# asyncio required
%def_disable python2

Name: python-module-%modname
Version: 0.8.1
Release: alt1

Summary: Python bindings to the generic input event interface
Group: Development/Python
License: 3-clause BSD
Url: https://pypi.python.org/pypi/%modname

Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz

BuildRequires: glibc-kernheaders

%if_enabled python2
BuildRequires: python-devel
BuildRequires: python-module-setuptools
%endif

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events generated
in the kernel directly to userspace through character devices that are
typically located in /dev/input/

%package -n python3-module-%modname
Summary: Python3 bindings to the generic input event interface
Group: Development/Python3

%description -n python3-module-%modname
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events generated
in the kernel directly to userspace through character devices that are
typically located in /dev/input/

%prep
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

%build
%{?_enable_python2:%python_build}

pushd py3build
%python3_build
popd

%install
%{?_enable_python2:%python_install}

pushd py3build
%python3_install
popd

%if_enabled python2
%files
%python_sitelibdir/%modname/
%exclude %python_sitelibdir/*.egg-info
%doc README*
%endif

%files -n python3-module-%modname
%python3_sitelibdir/%modname/
%exclude %python3_sitelibdir/*.egg-info
%doc README*

%changelog
* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.1
- exclude %%python*_sitelibdir/*.egg-info

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- first build for Sisyphus



