Name: friture
Version: 0.49
Release: alt1

Summary: Realtime audio data visualizer
License: GPLv3
Group: Sound
Url: https://friture.org/

Source: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(numpy)
BuildRequires: python3(Cython)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: libnumpy-py3-devel

%description
Friture is an application to visualize and analyze live audio data
in real-time. Friture displays audio data in several widgets, such as
a scope, a spectrum analyzer, or a rolling 2D spectrogram.
This program can be useful to analyze and equalize the audio response
of a hall, or for educational purposes, etc.
The name *Friture* is a french word for *frying*, also used for *noise*
in a sound.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README* INSTALL* COPYING*
%_bindir/friture
%_desktopdir/friture.desktop
%python3_sitelibdir/friture
%python3_sitelibdir/friture_extensions
%python3_sitelibdir/friture-%version.dist-info

%changelog
* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.49-alt1
- initial
