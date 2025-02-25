%define _unpackaged_files_terminate_build 1

%define pypi_name snmpclitools
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1
Summary: Command-line SNMP tools
License: BSD-2-Clause
Group: Networking/Other
Url: https://pypi.org/project/snmpclitools/
Vcs: https://github.com/lextudio/snmpclitools
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# renamed from pysnmp-apps
Provides: python3-module-pysnmp-apps = %EVR
Obsoletes: python3-module-pysnmp-apps <= 0.3.4-alt2
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
A collection of command-line tools for SNMP management purposes built on top of
PySNMP package.

%prep
%setup
%python3_fix_shebang .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream doesn't have tests suite,
# check the project is importable and its version
%pyproject_run -- python -c 'from importlib.metadata import version; import %mod_name; assert (act_version := version("%pypi_name")) == "%version", f"actual version: {act_version} differs from expected: %version"'

%files
%doc README.*
%_bindir/snmpbulkwalk
%_bindir/snmpget
%_bindir/snmpset
%_bindir/snmptranslate
%_bindir/snmptrap
%_bindir/snmpwalk
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 25 2025 Stanislav Levin <slev@altlinux.org> 0.7.2-alt1
- 0.3.4 -> 0.7.2.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt2
- python2 disabled

* Fri Nov  1 2013 Terechkov Evgenii <evg@altlinux.org> 0.3.4-alt1
- Initial build for ALT Linux Sisyphus
