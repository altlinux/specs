Name: python3-module-av
Version: 17.1.0
Release: alt1

Summary: Python bindings for ffmpeg libraries
License: BSD-3-Clause
Group: Development/Python
URL: https://pypi.org/project/av/
VCS: https://github.com/PyAV-Org/PyAV

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nocpp, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
%pyproject_builddeps_build
%pyproject_builddeps_metadata
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)

%python3_set_limited_api 3.11

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
%_bindir/pyav
%python3_sitelibdir/av
%python3_sitelibdir/av-%version.dist-info

%changelog
* Thu Jun 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 17.1.0-alt1
- 17.1.0 released

* Mon Apr 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 17.0.1-alt1
- 17.0.1 released

* Thu Mar 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 17.0.0-alt1
- 17.0.0 released

* Wed Jan 28 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 16.1.0-alt1
- 16.1.0 released

* Tue Nov 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 16.0.1-alt1
- 16.0.1 released

* Wed Sep 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 15.1.0-alt1
- 15.1.0 released

* Mon Jul 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.2.0-alt2
- suppressed extra reqs on ffmpeg (closes: 55369)

* Thu Jul 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.2.0-alt1
- 14.2.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.0.1-alt1
- 14.0.1 released

* Thu Oct 31 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 13.0.0-alt2
- rebuilt with gcc14

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 13.0.0-alt1
- 13.0.0 released

* Fri Jul 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 12.2.0-alt1
- 12.2.0 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0.0-alt1
- 11.0.0 released

* Mon Sep 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0.0-alt2
- rebuilt with ffmpeg-6.0

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0.0-alt1
- 10.0.0 released

* Wed May 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.2.0-alt1
- 9.2.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.0-alt1
- 8.1.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.0.3-alt1
- 8.0.3 released

* Wed Jan 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.0-alt1
- initial
