%define modname dbus-deviation
%def_enable check

Name: python3-module-%modname
Version: 0.6.1
Release: alt1.2

Summary: %modname is a project for parsing and processing D-Bus introspection XML
Group: Development/Python3
License: LGPL-2.1-or-later
Url: https://pypi.org/project/%modname

Vcs: https://github.com/dbus-deviation/dbus-deviation.git
Source: https://pypi.io/packages/source/d/%modname/%modname-%version.tar.gz
# setuptools_git
Source1: python3-module-%modname-eggs.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-wheel python3-module-sphinx
BuildRequires: python3-module-pycodestyle python3-module-unittest2

%description
%modname is a project for parsing D-Bus introspection XML and processing
it in various ways. Its main tool is dbus-interface-diff, which calculates the
difference between two D-Bus APIs for the purpose of checking for API breaks.

A second Python module, dbusapi, is provided for parsing D-Bus introspection
XML to produce an AST representing a D-Bus interface.

%prep
%setup -n %modname-%version -a1
find ./ -name "*.py" -print0|xargs -r0 sed -i "s|\(\/usr\/bin\/python\)$|\13|" --

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test

%files
%_bindir/dbus-interface-diff
%_bindir/dbus-interface-vcs-helper
%python3_sitelibdir_noarch/*
%doc README* NEWS

%changelog
* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1.2
- fixed build

* Sat Aug 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1.1
- fixed BR

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus




