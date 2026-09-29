Name: python3-module-luma-core
Version: 2.6.0
Release: alt1

Summary: Small display library core
License: MIT
Group: Development/Python
URL: https://pypi.org/project/luma.core
VCS: https://github.com/rm-hull/luma.core

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
luma.core is a component library providing a Pillow-compatible drawing canvas
for Python 3, and other functionality to support drawing primitives and
text-rendering capabilities for small displays on single board computers.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/luma
%python3_sitelibdir/%{pyproject_distinfo luma-core}/

%changelog
* Tue Sep 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.6.0-alt1
- 2.6 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 2.4.0-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt2
- require smbus2

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released
