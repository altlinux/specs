%def_with check

Name: python3-module-xdot
Version: 1.1
Release: alt2

Summary: Interactive viewer for graphs written in Graphviz's dot language

Url: https://github.com/jrfonseca/xdot.py
License: Python license
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/jrfonseca/xdot.py/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-devel python3-module-setuptools

%if_with check
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3 libgtk+3-gir gobject-introspection-devel
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
%python3_build_debug

%install
%python3_install

%if_with check
%check
PYTHONPATH=%buildroot%python3_sitelibdir %python3_test
%endif

%files
%doc README.md
%_bindir/xdot
%python3_sitelibdir/*

%changelog
* Thu Oct 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- fix build

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Sisyphus

