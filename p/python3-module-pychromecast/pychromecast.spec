Name: python3-module-pychromecast
Version: 14.0.10
Release: alt1

Summary: Python library to communicate with the Google Chromecast
License: MIT
Group: Development/Python
URL: https://pypi.org/project/PyChromecast/
VCS: https://github.com/home-assistant-libs/pychromecast

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

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
%python3_sitelibdir/pychromecast
%python3_sitelibdir/%{pyproject_distinfo pychromecast}/

%changelog
* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 14.0.10-alt1
- 14.0.10 released

* Fri Feb 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 14.0.9-alt1
- 14.0.9 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 14.0.5-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 14.0.5-alt1
- 14.0.5 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 14.0.0-alt1
- 14.0.0 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1.0-alt1
- 13.1.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.7-alt1
- 13.0.7 released

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.4-alt1
- 13.0.4 released

* Tue Aug 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1.4-alt1
- 12.1.4 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1.2-alt1
- 12.1.2 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3.0-alt1
- 10.3.0

* Sun Sep 27 2020 Anton Midyukov <antohami@altlinux.org> 0.7-alt1
- Initial build for Sisyphus
