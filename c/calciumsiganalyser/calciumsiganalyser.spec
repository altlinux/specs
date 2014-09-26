Name: calciumsiganalyser
Version: 2
Release: alt1.hg20110622
Summary: Calcium Signal Analyser (Vamp plugin)
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/calciumsiganalyser
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/calciumsiganalyser
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel libqm-dsp-devel

%description
The Calcium Signal Analyser is a Vamp plugin for the detection and
characterization of transients in noisy signals. It is adapted for the
analysis of calcium signals measured on zebrafish living embryos using
confocal microscopy.

%prep
%setup
rm -f *.o *.dylib

%build
%make_build

%install
install -d %buildroot%_libdir/vamp
install -m644 vamp-calcium-signal-analyser* %buildroot%_libdir/vamp/

%files
%doc CHANGELOG README.txt doc/*
%_libdir/vamp

%changelog
* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2-alt1.hg20110622
- Initial build for Sisyphus

