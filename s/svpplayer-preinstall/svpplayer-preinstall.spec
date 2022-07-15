Name: svpplayer-preinstall
Version: 0.1
Release: alt1

Summary: Set correct environment for SmoothVideo Project player

License: PDDL-1.0
Group: Video
Url: https://www.svp-team.com

# BuildArch: noarch
ExcludeArch: armh ppc64le

Requires: mpv
Requires: libqt5-concurrent
Requires: libqt5-svg
Requires: libqt5-qml
Requires: libmediainfo
Requires: python3-module-vapoursynth
Requires: lsof
Requires: youtube-dl
Requires: ffmpeg
Requires: libqt5-declarative
Requires: libMesaOpenCL

%description
%summary.

%files
%changelog
* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.
