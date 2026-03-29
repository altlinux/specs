%define _unpackaged_files_terminate_build 1
%define pypi_name xdot
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4
Release: alt1.1
Summary: Interactive viewer for Graphviz dot files
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/xdot/
Vcs: https://github.com/jrfonseca/xdot.py
Packager: Vitaly Lipatov <lav@altlinux.ru>
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-numpy
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3
BuildRequires: libgtk+3-gir gobject-introspection-devel
BuildRequires: graphviz
BuildRequires: fonts-ttf-ms
BuildRequires: /usr/bin/xvfb-run
%endif

%description
xdot is an interactive viewer for graphs written in Graphviz's dot language.

It uses internally the GraphViz's xdot output format
as an intermediate format, Python GTK bindings, and Cairo for rendering.

xdot can be used either as a standalone application from command line,
or as a library embedded in your Python application.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/build.yml
.github/scripts/test.sh

%files
%doc README.md
%_bindir/xdot
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.4-alt1.1
- Demodernized packaging.

* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.4-alt1
- 1.1 -> 1.4.

* Thu Oct 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- fix build

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Sisyphus

