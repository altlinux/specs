Name: netcmdplus
Version: 0.1.1
Release: alt1

Summary: Extended samba-tool (netcmd) version
License: GPLv3+
Group: System/Configuration/Other

Url: http://git.altlinux.org/people/manowar/packages/netcmdplus.git
Packager: Paul Wolneykien <manowar@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools

%description
netcmdplus extends samba-tool "user" and "group" commands with additional operations.

%package -n python-module-%name
Summary: Python module for samba-tool-plus (netcmdplus)
License: GPLv3+
Group: Development/Python

%description -n python-module-%name
netcmdplus extends samba-tool "user" and "group" commands with additional operations.
This package contains Python module code that extends samba.netcmd package.

%setup_python_module %name

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/samba-tool-plus

%files -n python-module-%name
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Added "group update" subcommand.

* Wed May 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
