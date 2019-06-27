Name:    pulsemixer
Version: 1.5.0
Release: alt1

Summary: CLI and curses mixer for PulseAudio
License: MIT
Group:   Sound
URL:     https://github.com/GeorgeFilipkin/pulsemixer

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

Requires: libpulseaudio

%description
%summary

%prep
%setup -n %name-%version

%install
install -Dm 755 pulsemixer %buildroot%_bindir/%name

%files
%_bindir/%name
%doc *.md

%changelog
* Thu Jun 27 2019 Ivan A. Melnikov <iv@altlinux.org> 1.5.0-alt1
- initial build
