Name: python3-module-av
Version: 8.1.0
Release: alt1

Summary: Python bindings for ffmpeg libraries
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pyav/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools) python3(Cython)
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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/av
%python3_sitelibdir/av-%version-*-info

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.0-alt1
- 8.1.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.0.3-alt1
- 8.0.3 released

* Wed Jan 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.0-alt1
- initial
