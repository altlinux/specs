Name: python3-module-onvif-parsers
Version: 2.3.0
Release: alt1

Summary: Parsers for ONVIF events
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/onvif-parsers
VCS: https://github.com/openvideolibs/onvif-parsers

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
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/onvif_parsers
%python3_sitelibdir/onvif_parsers-%version.dist-info

%changelog
* Wed Apr 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.0-alt1
- 2.3.0 released
