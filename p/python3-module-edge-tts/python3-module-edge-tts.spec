%define oname edge-tts
%define modulename edge_tts

Name: python3-module-%oname
Version: 7.2.8
Release: alt1

Summary: Microsoft Edge online text-to-speech (TTS) Python module and CLI

License: LGPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/rany2/edge-tts
# Source-url: https://github.com/rany2/edge-tts/archive/%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
edge-tts is a Python module that allows you to use Microsoft Edge online
text-to-speech service from within your Python code or using the provided
edge-tts and edge-playback command line utilities.

%package -n %oname
Summary: Command line client for Microsoft Edge online TTS
Group: Sound
Requires: python3-module-%oname = %EVR

%description -n %oname
edge-tts CLI utility that uses Microsoft Edge online text-to-speech
service to convert text to speech.

%package -n edge-playback
Summary: edge-tts based playback tool using mpv
Group: Sound
Requires: %oname = %EVR
Requires: /usr/bin/mpv

%description -n edge-playback
edge-playback is a wrapper around edge-tts and mpv that streams the
speech directly to the speakers.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%files -n %oname
%_bindir/edge-tts

%files -n edge-playback
%_bindir/edge-playback
%python3_sitelibdir/edge_playback/

%changelog
* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 7.2.8-alt1
- initial build for ALT Sisyphus

