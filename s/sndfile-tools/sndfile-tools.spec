%def_disable snapshot
%def_enable jack
%def_enable check

Name: sndfile-tools
Version: 1.5
Release: alt1

Summary: Sample Rate Converter tools
License: BSD-2-Clause
Group: Sound
Url: http://libsndfile.github.io/sndfile-tools/

%if_disabled snapshot
Source: https://github.com/libsndfile/%name/releases/download/%version/%name-%version.tar.bz2
%else
Vcs: https://github.com/libsndfile/sndfile-tools.git
Source: %name-%version.tar
%endif

%define libsndfile_ver 1.0.19
%define samplerate_ver 0.1.5
%define jack_ver 0.100

BuildRequires: libsndfile-devel >= %libsndfile_ver
BuildRequires: libsamplerate-devel >= %samplerate_ver
BuildRequires: libfftw3-devel libcairo-devel
%{?_enable_jack:BuildRequires: libjack-devel >= %jack_ver}

%description
Sndfile-tools is a small collection of programs that use libsndfile and
other libraries to do useful things. The collection currently includes
the following programs:

* sndfile-generate-chirp
* sndfile-jackplay
* sndfile-spectrogram
* sndfile-mix-to-mono

%prep
%setup

%build
%autoreconf -I m4
%configure %{?_disable_jack:--disbale_jack}
%nil
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_bindir/sndfile-generate-chirp
%{?_enable_jack:%_bindir/sndfile-jackplay}
%_bindir/sndfile-mix-to-mono
%_bindir/sndfile-resample
%_bindir/sndfile-spectrogram
%_bindir/sndfile-waveform
%_man1dir/*
%doc AUTHORS ChangeLog NEWS COPYING README*
%doc doc/*

%changelog
* Mon May 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- first build for Sisyphus

