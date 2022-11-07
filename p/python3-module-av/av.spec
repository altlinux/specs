Name: python3-module-av
Version: 10.0.0
Release: alt1

Summary: Python bindings for ffmpeg libraries
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pyav/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/av
%python3_sitelibdir/av-%version.dist-info

%changelog
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
