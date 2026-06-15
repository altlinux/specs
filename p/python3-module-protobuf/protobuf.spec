Name: python3-module-protobuf
Version: 7.35.1
Release: alt1

Summary: Protocol Buffers for Python
License: BSD-3-Clause
Group: Development/Python
URL: https://pypi.org/project/protobuf

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
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
%python3_sitelibdir/google
%python3_sitelibdir/protobuf-%version.dist-info

%changelog
* Mon Jun 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 7.35.1-alt1
- 7.35.1 released

* Wed May 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 7.35.0-alt1
- 7.35.0 released

* Tue Mar 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 7.34.1-alt1
- 7.34.1 released

* Fri Feb 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 7.34.0-alt1
- 7.34.0 released

* Tue Feb 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 6.33.5-alt1
- 6.33.5
