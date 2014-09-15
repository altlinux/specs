Name: vamp-silvet-plugin
Version: 1.0
Release: alt1.hg20140808
Summary: Vamp plugin for polyphonic music transcription
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/silvet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/silvet
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel libbqvec-devel libcq-devel
BuildPreReq: ladspa-flattendynamics-src libgomp-devel

%description
Silvet, or Shift-Invariant Latent Variable Transcription, is a Vamp
plugin for polyphonic music transcription (from audio to note times and
pitches).

%prep
%setup

cp -fR %_datadir/flattendynamics ./

%build
%make_build_ext -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 silvet.* %buildroot%_libdir/vamp/

%files
%doc CITATION README papers
%_libdir/vamp

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140808
- Initial build for Sisyphus

