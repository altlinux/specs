Name: kodi-addon-inputstream-ffmpegdirect
Version: 20.5.0
Release: alt3

Summary: FFmpeg stream addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/inputstream.ffmpegdirect/

AutoReqProv: yes, nopython

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel
BuildRequires: libavcodec-devel libavfilter-devel libavformat-devel
BuildRequires: libavutil-devel libswscale-devel libswresample-devel
BuildRequires: libpostproc-devel bzlib-devel zlib-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/kodi/addons/*
%_datadir/kodi/addons/*

%changelog
* Fri Sep 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.5.0-alt3
- rebuilt with recent ffmpeg

* Thu Jun 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.5.0-alt2
- rebuilt with gcc13

* Thu Nov 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.5.0-alt1
- 20.5.0 released

* Tue Jan 11 2022 Michael Shigorin <mike@altlinux.org> 19.0-alt6
- build on Elbrus as well

* Mon Oct 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt5
- 19.0-Matrix released

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 1.19.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 1.17.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- initial
