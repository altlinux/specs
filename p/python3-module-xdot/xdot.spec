%define _unpackaged_files_terminate_build 1
%define pypi_name xdot
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4
Release: alt1
Summary: Interactive viewer for Graphviz dot files
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/xdot/
Vcs: https://github.com/jrfonseca/xdot.py
Packager: Vitaly Lipatov <lav@altlinux.ru>
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%add_pyproject_deps_runtime_filter pygobject
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pygobject
%pyproject_builddeps_metadata
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3 libgtk+3-gir gobject-introspection-devel
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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.4-alt1
- 1.1 -> 1.4.

* Thu Oct 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- fix build

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Sisyphus

