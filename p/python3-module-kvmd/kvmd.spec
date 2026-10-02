Name: python3-module-kvmd
Version: 4.217
Release: alt1

Summary: Python PiKVM module
License: GPLv3
Group: Development/Python
URL: https://pikvm.org/
VCS: https://github.com/pikvm/kvmd

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps extras

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync extras pip_reqfile extras.txt

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/kvmd*
%python3_sitelibdir/kvmd
%python3_sitelibdir/kvmd-%version.dist-info

%changelog
* Tue Sep 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.217-alt1
- 4.217 released
