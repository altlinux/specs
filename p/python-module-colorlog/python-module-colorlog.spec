%define modname colorlog

Name: python-module-%modname
Version: 3.1.2
Release: alt1

Summary: Python module for log formatting with colors
Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

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
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/*.egg-info
%doc README.md


%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.md


%changelog
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


