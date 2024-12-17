%def_disable snapshot
%define pypi_name dbus-deviation
%def_enable check

Name: python3-module-%pypi_name
Version: 0.6.1
Release: alt3

Summary: %pypi_name is a project for parsing and processing D-Bus introspection XML
Group: Development/Python3
License: LGPL-2.1-or-later
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/dbus-deviation/dbus-deviation.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/d/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif
Patch1: %pypi_name-%version-HEAD.patch

BuildArch: noarch

# https://bugzilla.altlinux.org/52454
%add_python3_req_skip pipes

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-sphinx python3-module-pycodestyle
%{?_enable_check:BuildRequires: python3(argparse) python3(lxml)}

%description
%pypi_name is a project for parsing D-Bus introspection XML and processing
it in various ways. Its main tool is dbus-interface-diff, which calculates the
difference between two D-Bus APIs for the purpose of checking for API breaks.

A second Python module, dbusapi, is provided for parsing D-Bus introspection
XML to produce an AST representing a D-Bus interface.

%prep
%setup -n %pypi_name-%version
%patch1 -p1
find ./ -name "*.py" -print0|xargs -r0 sed -i "s|\(\/usr\/bin\/python\)$|\13|" --

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 -m unittest

%files
%_bindir/dbus-interface-diff
%_bindir/dbus-interface-vcs-helper
%python3_sitelibdir_noarch/dbusapi
%python3_sitelibdir_noarch/dbusdeviation
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%doc README* NEWS

%changelog
* Tue Dec 17 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt3
- updated to 0.6.1-4-gf5e6774
- filtered out python3(pipes) dependency (ALT #52454)
- enabled %%check

* Sat Jul 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt2
- ported to %%pyproject* macros

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1.3
- fixed BR

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1.2
- fixed build

* Sat Aug 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1.1
- fixed BR

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus




