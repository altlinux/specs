%define oname ffpyplayer

Name: python3-module-ffpyplayer
Version: 4.4.0
Release: alt1

Summary: A cython implementation of an ffmpeg based player

Group: Development/Python3
License: LGPL-3.0
Url: https://github.com/matham/ffpyplayer

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython
# python3-module-setuptools_scm

BuildRequires: libSDL2-devel libavdevice-devel libavfilter-devel libpostproc-devel libswresample-devel libswscale-devel

%description
FFPyPlayer is a python binding for the FFmpeg library for playing and writing media files.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/


%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt1
- new version 4.4.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.5-alt1
- new version 4.3.5 (with rpmrb script)

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.2-alt2
- initial build for ALT Sisyphus

* Sat Apr 17 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 4.3.2-alt1
- new version (4.3.2) with rpmgs script
