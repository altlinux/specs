%define modname evdev
# asyncio required
%def_disable python2

Name: python-module-%modname
Version: 1.3.0
Release: alt1

Summary: Python bindings to the generic input event interface
Group: Development/Python
License: BSD-3-Clause
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
%exclude %python_sitelibdir/*.egg-info
%doc README*
%endif

%files -n python3-module-%modname
%python3_sitelibdir/%modname/
%exclude %python3_sitelibdir/*.egg-info
%doc README*

%changelog
* Sun Jan 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.1
- exclude %%python*_sitelibdir/*.egg-info

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- first build for Sisyphus



