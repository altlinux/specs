Name: python3-module-gpiod
Version: 2.4.3
Release: alt1

Summary: Python bindings for libgpiod
License: LGPL-2.1-or-later
Group: Development/Python
URL: https://pypi.org/project/gpiod
VCS: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
BuildRequires: pkgconfig(libgpiod)
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export LINK_SYSTEM_LIBGPIOD=1
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/gpiod
%python3_sitelibdir/gpiod-%version.dist-info

%changelog
* Tue Jun 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.3-alt1
- 2.4.3 released

* Tue Apr 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.2-alt1
- 2.4.2 released
