Name: ladspa-flattendynamics
Version: 0.0
Release: alt1.hg20140723
Summary: Crude pre-processing to flatten out the RMS level of a signal
License: Free
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/flattendynamics
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/flattendynamics
Source: %name-%version.tar

BuildPreReq: gcc-c++ ladspa_sdk

%description
Crude pre-processing to flatten out the RMS level of a signal. Like a
slow, unmusical dynamic compressor. Implemented as a LADSPA plugin in
C++, works in real time, so has significant lag. A possible alternative
to other normalisation techniques for pre-processing in feature
extraction.

%package src
Summary: Sources of %name
Group: Development/C++
BuildArch: noarch

%description src
Crude pre-processing to flatten out the RMS level of a signal. Like a
slow, unmusical dynamic compressor. Implemented as a LADSPA plugin in
C++, works in real time, so has significant lag. A possible alternative
to other normalisation techniques for pre-processing in feature
extraction.

This package contains sources of %name.

%prep
%setup

mkdir -p ../src
cp * ../src/

%build
%make_build

%install
install -d %buildroot%_ladspa_path
install -m644 *.so %buildroot%_ladspa_path/

install -d %buildroot%_datadir/flattendynamics
install -p -m644 ../src/* %buildroot%_datadir/flattendynamics/

%files
%_ladspa_path/*

%files src
%_datadir/flattendynamics

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.hg20140723
- Initial build for Sisyphus

