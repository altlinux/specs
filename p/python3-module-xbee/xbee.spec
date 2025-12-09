Name: python3-module-xbee
Version: 2.3.2
Release: alt2

Summary: XBee serial communication API 
License: BSD
Group: Development/Python
Url: https://pypi.org/project/XBee/

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest xbee/tests

%files
%python3_sitelibdir/xbee
%python3_sitelibdir/xbee-%version.dist-info

%changelog
* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.2-alt2
- moved to pyproject

* Fri Jan 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.2-alt1
- initial
