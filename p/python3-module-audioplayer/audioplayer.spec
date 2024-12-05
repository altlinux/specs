%define _unpackaged_files_terminate_build 1
%define mod_name %pypi_name
%define pypi_name audioplayer

Name: python3-module-%pypi_name
Version: 0.6
Release: alt1
Summary: is a cross platform Python 3 package for playing sounds
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/audioplayer/
Vcs: https://github.com/mjbrusso/audioplayer
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-gst1.0
BuildRequires: gstreamer1.0

%py3_provides %pypi_name

%description
audioplayer is a cross platform Python 3 package for playing sounds (mp3, wav,
...). It provides the key features of an audio player, such as opening a
media file, playing (loop/block), pausing, resuming, stopping, and setting the
playback volume.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/audioplayer_macos.py

%changelog
* Thu Dec 05 2024 Pavel Shilov <zerospirit@altlinux.org> 0.6-alt1
- initial build for Sisyphus
