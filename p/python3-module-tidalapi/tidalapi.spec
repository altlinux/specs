Name: python3-module-tidalapi
Version: 0.8.11
Release: alt1

Summary: Python API for TIDAL music streaming service
License: LGPLv3
Group: Development/Python
URL: https://pypi.org/project/tidalapi
VCS: https://github.com/tamland/python-tidal

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

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

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/tidalapi
%python3_sitelibdir/tidalapi-%version.dist-info

%changelog
* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.11-alt1
- 0.8.11 released

* Tue Sep 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt1
- 0.7.3 released
