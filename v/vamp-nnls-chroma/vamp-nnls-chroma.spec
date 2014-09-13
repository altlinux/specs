Name: vamp-nnls-chroma
Version: 0.2.1
Release: alt1
Summary: Chordino and NNLS Chroma
License: GPLv2
Group: Sound
Url: http://www.isophonics.net/nnls-chroma
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel boost-devel

%description
NNLS Chroma analyses a single channel of audio using frame-wise spectral
input from the Vamp host. The plugin was originally developed to extract
treble and bass chromagrams for subsequent use in chord extraction
methods. The spectrum is transformed to a log-frequency spectrum
(constant-Q) with three bins per semitone.

%prep
%setup

%build
%make_build_ext -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 nnls-chroma.* %buildroot%_libdir/vamp/

%files
%doc README *.txt
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

