Name: python3-module-libsonic
Version: 1.1.1
Release: alt1

Provides: python3-module-py-sonic = %EVR

Summary: Subsonic REST API
License: GPLv3
Group: Development/Python
URL: https://pypi.org/project/py-sonic
VCS: https://github.com/crustymonkey/py-sonic

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

%files
%python3_sitelibdir/libsonic
%python3_sitelibdir/py_sonic-%version.dist-info

%changelog
* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.3-alt1
- 1.0.3 released

* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
