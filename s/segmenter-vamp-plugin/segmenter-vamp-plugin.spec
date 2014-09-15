Name: segmenter-vamp-plugin
Version: 1.0
Release: alt1.hg20140806
Summary: Vamp plugin for automatic music structural segmentation
License: AGPLv3
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/segmenter-vamp-plugin
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/segmenter-vamp-plugin
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel libqm-dsp-devel boost-devel
BuildPreReq: vamp-nnls-chroma-src libhdf5-devel

%description
Segmentino is a Vamp plugin for automatic music structural segmentation,
based on an algorithm first used in Mauch et al.'s paper on Using
Musical Structure to Enhance Automatic Chord Transcription.

%prep
%setup

cp -fR %_datadir/nnls-chroma ./

%build
%make_build -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 segmentino.* %buildroot%_libdir/vamp/

%files
%doc CITATION README
%_libdir/vamp

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140806
- Initial build for Sisyphus

