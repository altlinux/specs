%define modname colorlog
%def_disable python2

Name: python-module-%modname
Version: 4.1.0
Release: alt1

Summary: Python module for log formatting with colors
Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%{?_enable_python2:
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools}

%description
colorlog.ColoredFormatter is a formatter for use with Python's logging
module that outputs records using terminal colors.


%package -n python3-module-%modname
Summary: Python3 module for log formatting with colors
Group: Development/Python3

%description -n python3-module-%modname
colorlog.ColoredFormatter is a formatter for use with Python's logging
module that outputs records using terminal colors.

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

%{?_enable_python2:
%files
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.md
}

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.md


%changelog
* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0
- disabled python2 build

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Mon Sep 25 2017 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Jul 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- first build for Sisyphus


