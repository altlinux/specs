Name: python3-module-turbojpeg
Version: 1.8.2
Release: alt1

Summary: A Python wrapper of libjpeg-turbo
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyTurboJPEG/
VCS: https://github.com/lilohuang/PyTurboJPEG

Provides: python3-module-pyturbojpeg = %EVR
Requires: libturbojpeg

Source0: %name-%version.tar
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
%python3_sitelibdir/turbojpeg.*
%python3_sitelibdir/*/turbojpeg.*
%python3_sitelibdir/pyturbojpeg-%version.dist-info

%changelog
* Thu Oct 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.2-alt1
- 1.8.2 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.7.5-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Tue Nov 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.5-alt2
- explicitly require libturbojpeg

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.5-alt1
- 1.7.5 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.7-alt1
- 1.6.7 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt1
- 1.6.6 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.5-alt1
- 1.6.5 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- initial
