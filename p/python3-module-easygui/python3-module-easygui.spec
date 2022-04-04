%def_disable snapshot
%define modname easygui

Name: python3-module-%modname
Version: 0.98.3
Release: alt1

Summary: Python3 module for GUI programming
Group: Development/Python3
License: BSD-3-Clause
Url: http://pypi.python.org/pypi/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/robertlugg/easygui.git
Source: %modname-%version.tar
%endif
Source1: easygui-0.98.2-README.md

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
EasyGUI is a Python3 module for very simple, very easy GUI programming in Python.
EasyGUI is different from other GUI libraries in that EasyGUI is NOT
event-driven. Instead, all GUI interactions are invoked by simple
function calls.

%prep
%setup -n %modname-%version
cp %SOURCE1 README.md

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%doc README.txt
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Mon Apr 04 2022 Yuri N. Sedunov <aris@altlinux.org> 0.98.3-alt1
- 0.98.3

* Thu Aug 5 2021 Yuri N. Sedunov <aris@altlinux.org> 0.98.2-alt1
- 0.98.2

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.98.1-alt1
- first build for Sisyphus


