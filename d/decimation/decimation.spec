Name: decimation
Version: 0.0
Release: alt1.hg20131022
Summary: Compare a few different C++ implementations of audio-rate signal decimation
License: MIT
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/decimation
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/decimation
Source: %name-%version.tar

BuildPreReq: gcc-c++ libqm-dsp-devel libsndfile-devel
BuildPreReq: libsamplerate-utils libsndfile-utils

%description
Compare a few different C++ implementations of audio-rate signal
decimation for relative speed and quality. "Decimation" refers here to
downsampling a signal by an integer factor N; we only consider the case
where N is a power of two.

The principle is to use a low-pass filter to reduce the bandwidth of the
signal to below the Nyquist frequency at the target sample rate (i.e.
with the maximum frequency content being below the original rate divided
by twice N, for decimation factor N) and then to pick every Nth sample.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_bindir
install -m755 qm-dsp-decimate/decimate qm-dsp-decimate/decimate-b \
	qm-dsp-resample/resample \
	%buildroot%_bindir/

%files
%doc *.txt
%_bindir/*

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.hg20131022
- Initial build for Sisyphus

