%define _samba_mod_libdir  %_libdir/samba
%define _samba_dc_mod_libdir  %_libdir/samba-dc
%define _samba_dc_pythonarchdir  %_samba_dc_mod_libdir/python%_python3_version

Name: netcmdplus
Version: 0.1.3
Release: alt1

Summary: Extended samba-tool (netcmd) version
License: GPLv3+
Group: System/Configuration/Other

Url: https://gitlab.basealt.space/alt/netcmdplus.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

# Add conflicts due compatiblity with old samba package not provided alternative to heimdal libs
Conflicts: samba-dc < 4.14.10-alt2
# Add conflicts due compatiblity with old samba package provided python3(samba.netcmd.user)
Conflicts: python3-module-samba < 4.14

Conflicts: %name < %EVR

# samba-tool-plus: binary uses samba_tool_plus function
Requires: python3-module-samba > 4.18

%description
netcmdplus extends samba-tool "user" and "group" commands with additional operations.

%package -n python3-module-%name
Summary: python3 module for samba-tool-plus (netcmdplus)
License: GPLv3+
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
netcmdplus extends samba-tool "user" and "group" commands with additional operations.
This package contains Python3 module code that extends samba.netcmd package.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_altdir
mkdir -p %buildroot%_samba_mod_libdir/bin
mkdir -p %buildroot%_samba_dc_mod_libdir/bin

cp %buildroot%_bindir/samba-tool-plus %buildroot%_samba_dc_mod_libdir/bin/
sed -i 's!^\(import sys\)$!\1\nsys.path.insert(0, "%_samba_dc_pythonarchdir")!' -- "%buildroot%_samba_dc_mod_libdir/bin/samba-tool-plus"

cp %buildroot%_bindir/samba-tool-plus %buildroot%_samba_mod_libdir/bin/
printf "%_bindir/samba-tool-plus\t%_samba_mod_libdir/bin/samba-tool-plus\t20\n" > %buildroot%_altdir/%name

%files
%ghost %_bindir/samba-tool-plus
%_samba_dc_mod_libdir/bin/samba-tool-plus
%_samba_mod_libdir/bin/samba-tool-plus
%_altdir/%name

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}/

%changelog
* Mon Feb 19 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.3-alt1
- Add compatibility with stable releases of samba-4.18 and later (closes: 49404).
- Replace python3 build to new pyproject_build process.

* Sat Nov 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.2-alt2
- Add support samba-tool-plus alternatives for various samba-dc and
  samba-dc-mitkrb5 builds with Heimdal and MIT Kerberos respectively.

* Wed Jul 21 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.2-alt1
- Fix using obsoleted in samba-4.14 cmd_user_create class with renamed
  cmd_user_add class (closes: 40557)
- Add conflicts with old samba package provided python3(samba.netcmd.user)

* Mon Sep 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt3
- Fix: Remove self-obsoletes.

* Thu Jan 23 2020 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt2
- Transfer to python3.

* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Added "group update" subcommand.

* Wed May 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
