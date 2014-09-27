Name: csv2wav
Version: 1
Release: alt1.hg20110622
Summary: Convert CSV text data into a WAV file
License: GPLv2+
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/csv2wav
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/csv2wav
Source: %name-%version.tar

BuildPreReq: gcc-c++ libsndfile-devel libsamplerate-devel

%description
csv2wav is a simple standalone application to convert CSV text data into
a WAV file. The data are automatically rescaled according to the
specifications of the WAV format and can also be resampled.

%prep
%setup

rm -f csv2wav *.o

%build
%make_build

%install
install -d %buildroot%_bindir
install -m755 csv2wav %buildroot%_bindir/

%files
%doc README.txt doc/*
%_bindir/*

%changelog
* Sat Sep 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1.hg20110622
- Initial build for Sisyphus

